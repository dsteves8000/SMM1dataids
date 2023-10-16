import struct
import hashlib
import hmac
key = hashlib.md5(b"9f2b4678").digest()

id = 1008512
data = struct.pack("<Q", id)
checksum = hmac.HMAC(key, data).digest()
hex_string = format(id, '08X')
formatted_hex = '-'.join([hex_string[:4], hex_string[4:]])
print(str(id) + ": " + checksum[3:1:-1].hex() + "-0000-" + formatted_hex)
