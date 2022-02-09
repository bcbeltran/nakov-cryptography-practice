from Crypto.Hash import keccak
import hashlib, binascii
# import whirlpool

text = 'hello'
data = text.encode('utf8')

sha224hash = hashlib.sha224(data).digest()
print("SHA-224: ", binascii.hexlify(sha224hash))
print('ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193')
print('')

sha256hash = hashlib.sha256(data).digest()
print("SHA-256: ", binascii.hexlify(sha256hash))
print('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
print('')

sha3_224hash = hashlib.sha3_224(data).digest()
print("SHA3-224:", binascii.hexlify(sha3_224hash))
print('b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81')
print('')

sha3_384hash = hashlib.sha3_384(data).digest()
print("SHA3-384:", binascii.hexlify(sha3_384hash))
print('720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887')
print('')

keccak384 = keccak.new(data=b'hello', digest_bits=384).digest()
print("Keccak384: ", binascii.hexlify(keccak384))
print('dcef6fb7908fd52ba26aaba75121526abbf1217f1c0a31024652d134d3e32fb4cd8e9c703b8f43e7277b59a5cd402175')
print('')

blake2s = hashlib.new('blake2s', data).digest()
print('BLAKE2s: ', binascii.hexlify(blake2s))
print('')
print('')

ripemd160 = hashlib.new('ripemd160', data).digest()
print('RIPEMD-160: ', binascii.hexlify(ripemd160))
print('')
print('')

# whirlpool512 = whirlpool.new(b'hello').hexdigest()
# print('Whirlpool512: ', binascii.hexlify(whirlpool512))