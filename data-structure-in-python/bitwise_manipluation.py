# Bits are the most basic form of data in a computer.
# Bitwise operations are performed on binary numbers or bits of a number.

# Usage:
# 1. Bitwise operations are used in low-level programming (embedded systems) for setting, clearing, and toggling flags
# 2. Storing and manipulating small pieces of data such as, states, or small configurations
# 3. Solving certain mathematical problems when manipulating bits is more efficient than using arithmetic operations.

# Bitise Operators:
# Bitwise operations are fast and are performed directly on the processor.
# Bitwise operators can only be applied to integers. When applied to floats or other types, Python raises a TypeError.
# 1. AND: &
print(5 & 3) # 0101 & 0011 = 0001 = 1
# 2. OR: |
print(5 | 3) # 0101 | 0011 = 0111 = 7
# 3. XOR: ^
print(5 ^ 3) # 0101 ^ 0011 = 0110 = 6
# 4. NOT: ~
# When performing NOT operations, Python uses signed integers. 
# The result of a NOT operation might seem counterintuitive because Python uses an unlimited number of bits for integers, 
# so the result of ~x is -x-1.
print(~5) # ~0101 = 1010 = -6 (2's complement) 
# 5. Left Shift: <<
print(5 << 1) # 0101 << 1 = 1010 = 10
# 6. Right Shift: >>
print(5 >> 1) # 0101 >> 1 = 0010 = 2