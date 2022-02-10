from Crypto.Hash import keccak
from backports.pbkdf2 import pbkdf2_hmac
import hashlib, hmac, binascii, os
# import whirlpool


# PRACTICING DIFFERENT HASHING ALGORITHMS
# text = 'hello'
# data = text.encode('utf8')

# sha224hash = hashlib.sha224(data).digest()
# print("SHA-224: ", binascii.hexlify(sha224hash))
# print('ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193')
# print('')

# sha256hash = hashlib.sha256(data).digest()
# print("SHA-256: ", binascii.hexlify(sha256hash))
# print('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
# print('')

# sha3_224hash = hashlib.sha3_224(data).digest()
# print("SHA3-224:", binascii.hexlify(sha3_224hash))
# print('b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81')
# print('')

# sha3_384hash = hashlib.sha3_384(data).digest()
# print("SHA3-384:", binascii.hexlify(sha3_384hash))
# print('720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887')
# print('')

# keccak384 = keccak.new(data=b'hello', digest_bits=384).digest()
# print("Keccak384: ", binascii.hexlify(keccak384))
# print('dcef6fb7908fd52ba26aaba75121526abbf1217f1c0a31024652d134d3e32fb4cd8e9c703b8f43e7277b59a5cd402175')
# print('')

# blake2s = hashlib.new('blake2s', data).digest()
# print('BLAKE2s: ', binascii.hexlify(blake2s))
# print('')
# print('')

# ripemd160 = hashlib.new('ripemd160', data).digest()
# print('RIPEMD-160: ', binascii.hexlify(ripemd160))
# print('')
# print('')

# whirlpool512 = whirlpool.new(b'hello').hexdigest()
# print('Whirlpool512: ', binascii.hexlify(whirlpool512))








# # PRACTICING MAC AND HMAC

# # mac = hmac.new(b'keystone', b'light', hashlib.sha256).digest()
# # print("HMAC-SHA256: ", binascii.hexlify(mac))

# # def hmac_sha256(key, msg):
# #   return hmac.new(key, msg, hashlib.sha256).digest()

# # key = b"12345"
# # msg = b"the tomatoes are coming"
# # print("HMAC-SHA256: ", binascii.hexlify(hmac_sha256(key, msg)))

# def hmac_sha384(key, msg):
#     return hmac.new(key, msg, hashlib.sha384).digest()

# key = b"cryptography"
# msg = b"hello"
# print("HMAC-SHA384: ", binascii.hexlify(hmac_sha384(key, msg)))
# print('Expected output is: 83d1c3d3774d8a32b8ea0460330c16d1b2e3e5c0ea86ccc2d70e603aa8c8151d675dfe339d83f3f495fab226795789d4')

# key = b"again"
# msg = b"hello"
# print("HMAC-SHA384: ", binascii.hexlify(hmac_sha384(key, msg)))
# print('Expected output is: 4c549a549aa037e0fb651569bf271faa23cfa20e8a9d21438a6ff5bf6be916bebdbaa48001e0cd6941ec74cd02be70e5')







# PRACTICING KEY DERIVATION FUNCTIONS

# PBKDF2
# key = pbkdf2(password, salt, iterations-count, hash-function, derived-key-len)

##    password – array of bytes / string, e.g. "p@$Sw0rD~3" (8-10 chars minimal length is recommended)
##    salt – securely-generated random bytes, e.g. "df1f2d3f4d77ac66e9c5a6c3d8f921b6" (minimum 64 bits, 128 bits is recommended)
##    iterations-count, e.g. 1024 iterations
##    hash-function for calculating HMAC, e.g. SHA256
##    derived-key-len for the output, e.g. 32 bytes (256 bits)

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "p@$Sw0rD~1".encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 100000, 32)
print("Derived key:", binascii.hexlify(key))