from struct import *
import binascii
#store data as bytes

packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# get byte data back to normal
original_data = unpack("iif", packed_data)
print(original_data)

print(unpack("iif", b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))
