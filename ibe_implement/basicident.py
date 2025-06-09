#!/usr/bin/env sage -python
# -*- coding: utf-8 -*-
"""
basicident_demo.py
~~~~~~~~~~~~~~~~~~

Small implementation of Boneh–Franklin IBE (the “BasicIdent”
variant) that runs under Python ≥ 3.10 and SageMath ≥ 9.5.

Run:   sage -python basicident_demo.py
"""

import os
import random
from copy import deepcopy

from sage.crypto.cryptosystem import PublicKeyCryptosystem
from sage.all import (
    EllipticCurve, Hom, Zmod, FiniteField, Integer, GF
)


# ----------------------------------------------------------------------
# 1.  Boneh–Franklin BasicIdent class
# ----------------------------------------------------------------------
class BasicIdent(PublicKeyCryptosystem):
#class BasicIdent:
    """
    Boneh & Franklin “BasicIdent” identity‑based encryption.

    Parameters
    ----------
    ec : EllipticCurve
        A supersingular curve E / 𝔽_q.
    P : EllipticCurvePoint
        A point of prime order n on `ec`.
    dmap : callable
        Distortion map Ψ : E(𝔽_q^k) → E(𝔽_q^k).
    order : int, optional
        Explicit order of P (computed automatically if omitted).
    pairing : str, {"weil", "tate"}
        Choice of bilinear pairing.
    k : int, optional
        Embedding degree (computed automatically if omitted).
    seed : int, optional
        Seed for Python's RNG (only for reproducible *demos*).
    """

    # ------------------------------------------------------------------
    # Constructor & helpers
    # ------------------------------------------------------------------
    def __init__(self, ec, P=None, dmap=None, order=None,pairing="weil", k=None, seed=None):
        # Curve and subgroup generator
        self.ec = ec
        self.P = P
        self.order = order or P.order()

        # (Weak!) RNG for demonstration purposes
        random.seed(seed)

        # Distortion map handling
        self.distortion = self._decorate(dmap) if dmap else self._identity_ext

        # Pairing type (Weil or Tate)
        self.pairing = pairing.lower()

        # Embedding degree k
        q = self.ec.base_ring().cardinality()
        self.k = k or Zmod(self.order)(q).multiplicative_order()

        # Master secret t ∈ [2, n‑1]
        self.t = random.randint(2, self.order - 1)

        # Lift curve to 𝔽_{q^k}
        self.base_ext = FiniteField(q ** self.k, 'β')
        self.hom = Hom(self.ec.base_ring(), self.base_ext)(self.base_ext.gen() ** ((q ** self.k - 1) // (q - 1)))
        self.ec_ext = EllipticCurve(list(map(int, self.ec.a_invariants()))).change_ring(self.base_ext)

    # ---------- helper to lift P to extension field -------------------
    def _ext(self, P):
        """
        Lift a point P ∈ E(𝔽_q) to the extension curve E(𝔽_{q^k})
        by embedding each coordinate with the field homomorphism.
        """
        if P.is_zero():                       # handle the point at infinity
            return self.ec_ext(0)

        x, y = P.xy()                         # affine coordinates
        return self.ec_ext(self.hom(x), self.hom(y))

    # ---------- trivial distortion if none supplied -------------------
    def _identity_ext(self, P):
        """Fallback distortion map: identity on E(𝔽_{q^k})."""
        return self._ext(P)

    # ---------- wraps user‑provided distortion with field‑lift --------
    def _decorate(self, raw_map):
        def wrapped(point):
            return raw_map(self._ext(point))
        return wrapped

    # ------------------------------------------------------------------
    # Two hash / KDF stubs (replace for real crypto!)
    # ------------------------------------------------------------------
    def H1(self, identity: str):
        """
        Map an arbitrary identity string to a curve point of order n.

        The logic here is *extremely* cheap – for demos only.
        """
        try:
            idx = int(identity) % (self.order - 2)
        except ValueError:
            idx = 0
            for ch in identity.encode():
                idx = (idx * 256 + ch) % (self.order - 2)
        return (idx + 2) * self.P          # avoid 0,1 multiples

    def H2(self, element, length: int):
        """
        Weak KDF turning `element` into `length` pseudorandom bits.
        (Python's hash() is *not* deterministic across processes unless
        PYTHONHASHSEED is fixed, but fine for a single demo run.)
        """
        random.seed(hash(element))
        return [random.randint(0, 1) for _ in range(length)]

    # ------------------------------------------------------------------
    # One‑time‑pad helper
    # ------------------------------------------------------------------
    def _mask(self, msg_bits, element):
        mask = self.H2(element, len(msg_bits))
        return ''.join(str((b ^ m) & 1) for b, m in zip(msg_bits, mask))

    # ------------------------------------------------------------------
    # Public / private key extraction
    # ------------------------------------------------------------------
    def public_key(self, identity):
        """Return [Q_ID, t·P]"""
        return [self.H1(identity), self.t * self.P]

    def private_key(self, identity):
        """Return d_ID = t · Q_ID (only PKG can compute)."""
        return self.t * self.H1(identity)

    # ------------------------------------------------------------------
    # Encryption / decryption
    # ------------------------------------------------------------------
    def encrypt(self, message, pubkey, *, seed=None, text=False):
        """
        Encrypt `message` for holder of `pubkey` (= [Q_ID, tP]).
        If `text=True`, treat message as UTF‑8 string.
        """
        random.seed(seed)

        # 1) Serialise message → bit list (LSB first)
        if text:
            m_int = int.from_bytes(message.encode(), 'big')
        else:
            m_int = int(message)
        msg_bits = Integer(m_int).digits(2)
        msg_bits.reverse()                    # LSB first

        # 2) Ephemeral scalar
        r = random.randint(2, self.order - 1)

        # 3) Pairing computation
        Q_ID, tP = pubkey
        if self.pairing == "tate":
            pair_val = self._ext(Q_ID).tate_pairing(
                self.distortion(tP), self.order,
                self.k, self.ec_ext.base_ring().cardinality()
            )
        else:
            pair_val = self._ext(Q_ID).weil_pairing(
                self.distortion(tP), self.order
            )

        # 4) Ciphertext
        C1 = r * self.P
        C2 = self._mask(msg_bits, pair_val ** r)
        return C1, C2

    # ------------------------------------------------------------------
    def decrypt(self, ciphertext, d_ID, *, text=False):
        """Recover message using private key d_ID."""
        C1, C2 = ciphertext

        if self.pairing == "tate":
            pair_val = self._ext(d_ID).tate_pairing(self.distortion(C1), self.order,self.k, self.ec_ext.base_ring().cardinality())
        else:
            pair_val = self._ext(d_ID).weil_pairing(self.distortion(C1), self.order)

        # Unmask bitstring → integer
        plain_bits = [int(b) for b in C2]
        m_int = int(self._mask(plain_bits, pair_val), 2)

        if text:
            m_len = (m_int.bit_length() + 7) // 8
            return m_int.to_bytes(m_len, 'big').decode()
        return m_int


# ----------------------------------------------------------------------
# 2.  Minimal distortion map for a supersingular curve
# ----------------------------------------------------------------------
def simple_distortion(Q):
    """
    Toy distortion map for a supersingular curve y² = x³ + 1

        ψ : (x, y)  ↦  (x, −y)

    •   Works because (x,−y) still satisfies y² = x³ + 1.
    •   Keeps the point at infinity unchanged.
    """
    if Q.is_zero():              # identity point maps to itself
        return Q
    x, y = Q.xy()                # affine coordinates
    return Q.curve()(x, -y)      # *same* curve, flipped y


# ----------------------------------------------------------------------
# 3.  Self‑contained demo
# ----------------------------------------------------------------------
def main():
    print("\n╔═══════════════════════════════════════════════════════╗")
    print("║  Boneh–Franklin BasicIdent demo (Python 3 + Sage)     ║")
    print("╚═══════════════════════════════════════════════════════╝\n")

    # -- 0) System‑wide setup -----------------------------------------
    q = 10177
    E = EllipticCurve(GF(q), [0, 1])               # y² = x³ + 1
    P = next(pt for pt in (E.random_point() for _ in range(500))
             if pt.order().is_prime())
    
    # while True:
    #     P = EllipticCurve(GF(q), [0, 1]).random_point()
    #     n = P.order()
    #     if n.is_prime() and n > 1000:
    #         break

    ibe = BasicIdent(E, P=P, dmap=simple_distortion,pairing="weil", seed=42)

    print(f"[setup]  q = {q},  n = {ibe.order},  k = {ibe.k}")
    print(f"         Master secret t = {ibe.t}\n")

    # -- 1) Key extraction for Alice ----------------------------------
    ID = "alice@example.com"
    d_ID = ibe.private_key(ID)
    pub_ID = ibe.public_key(ID)

    print("[PKG]    Issued private key for identity:", ID, "\n")

    # -- 2) Bob encrypts ---------------------------------------------
    message = "The quick brown fox jumps over the lazy dog."
    print("[Bob]    Plaintext:", repr(message))
    C1, C2 = ibe.encrypt(message, pub_ID, seed=99, text=True)
    print("[Bob]    Ciphertext:")
    print("         C1 =", C1)
    print("         C2 =", C2, "\n")

    # -- 3) Alice decrypts -------------------------------------------
    recovered = ibe.decrypt((C1, C2), d_ID, text=True)
    print("[Alice]  Decrypted:", repr(recovered)) 
    #repr() function shows the string most accurately as it is written in code

    assert recovered == message
    print("\n✓ demo successful – plaintext recovered intact.")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
