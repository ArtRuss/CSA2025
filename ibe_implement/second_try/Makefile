
PY_SCRIPT := basicident.py
SAGE_DIR := /data/sage
MANIFEST := basicident.manifest
MANIFEST_TEMPLATE := $(MANIFEST).template
SGX_SIGNED_MANIFEST := $(MANIFEST).sgx
#Used for remote attestation
#SGX_TOKEN := $(PY_SCRIPT).token
#Must generate before using the enclave
SIGNER_KEY := /home/kfox24/.config/gramine/enclave-key.pem

.PHONY: all direct sgx clean
all:
ifeq ($(SGX),1)
	@$(MAKE) sgx
else
	@$(MAKE) direct
endif

direct: $(MANIFEST)
	#Generates manifest for direct
sgx: $(SGX_SIGNED_MANIFEST)
	#Generates manifest and signiture file

$(MANIFEST): $(MANIFEST_TEMPLATE)
	gramine-manifest -Dpy_script=$(PY_SCRIPT) -Dsage_dir=$(SAGE_DIR) $< $@

$(SGX_SIGNED_MANIFEST): $(MANIFEST)
	gramine-sgx-sign --key $(SIGNER_KEY) --manifest $< --output $@

clean:
	rm -f $(MANIFEST) $(MANIFEST).sgx