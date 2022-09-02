# Bitwise operators #
a, b = 5, 3
print("a & b\t\t=>\t", a&b)  # 1 # AND # Sets each bit to 1 if both bits are 1
print("a | b\t\t=>\t", a|b)  # 7 # OR # Sets each bit to 1 if one of two bits is 1
print("a ^ b\t\t=>\t", a^b)  # 6 # XOR # Sets each bit to 1 if only one of two bits is 1
print("~a\t\t=>\t", ~a)      # -6 # Bitwise NOT operator: Returns one’s complement of the number.
a >>= 2     # 1     # Signed right shift # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print("a >>= 2\t\t=>\t", a)  # 1
b = b << 2  # 12    # Zero fill left shift # Shift left by pushing zeros in from the right and let the leftmost bits fall off
print("b = b << 2\t=>\t", b) # 12
print("------------------------------------------------------------------------")

# Bitwise not operator: Returns one’s complement of the number.
# Example:
print(~10, ~4, ~15)
# a = 10 = 1010 (Binary)
# ~a = ~1010
#    = -(1010 + 1)
#    = -(1011)
#    = -11 (Decimal)
