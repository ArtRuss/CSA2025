#master_secret.py
import random
def gen_master_secret(order):
    return random.randint(2, order - 1)


if __name__ == "__main__":
    print(gen_master_secret(13))