from sage.all import Integer

if __name__ == "__main__":
    x1 = Integer(504)
    print(x1.digits(2))
    #print(x1.digits(2).reverse())
    print(x1.digits(2)[::-1])  # Reverse the list of bits
    