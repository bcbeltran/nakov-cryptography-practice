import pyscrypt
import argon2
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

##    password ??? array of bytes / string, e.g. "p@$Sw0rD~3" (8-10 chars minimal length is recommended)
##    salt ??? securely-generated random bytes, e.g. "df1f2d3f4d77ac66e9c5a6c3d8f921b6" (minimum 64 bits, 128 bits is recommended)
##    iterations-count, e.g. 1024 iterations
##    hash-function for calculating HMAC, e.g. SHA256
##    derived-key-len for the output, e.g. 32 bytes (256 bits)

# salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
# passwd = "p@$Sw0rD~1".encode("utf8")
# key = pbkdf2_hmac("sha256", passwd, salt, 100000, 32)
# print("Derived key:", binascii.hexlify(key))





## Scrypt

# key = Scrypt(password, salt, N, r, p, derived-key-len)

# password??? the input password (8-10 chars minimal length is recommended)
# salt ??? securely-generated random bytes (64 bits minimum, 128 bits recommended)
# N ??? iterations count (affects memory and CPU usage), e.g. 16384 or 2048
# r ??? block size (affects memory and CPU usage), e.g. 8
# p ??? parallelism factor (threads to run in parallel - affects the memory, CPU usage), usually 1
# derived-key-length - how many bytes to generate as output, e.g. 32 bytes (256 bits)


# salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
# passwd = b'shAmaLamAD1ngD0ng!'
# key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)
# print("Derived key:", key.hex())





### USING ARGON2 TO REGISTER, LOGIN AND CHANGE PASSWORD ###

# Argon2

# password P: the password (or message) to be hashed
# salt S: random-generated salt (16 bytes recommended for password hashing)
# iterations t: number of iterations to perform
# memorySizeKB m: amount of memory (in kilobytes) to use
# parallelism p: degree of parallelism (i.e. number of threads)
# outputKeyLength T: desired number of returned bytes

# time_cost = number of iterations
# memory_cost = memory to use in KB
# parallelism = how many parallel threads to use
# hash_len = size of the derived key
# salt_len = size of the random generated salt, typically 128 bits/ 16 bytes
# import json

# with open('users.json') as f:
#    data = json.load(f)


# def register_user(username, password, data):
#     for i in data['users']:
#         if i['username'] == username:
#             return print('This user already exists')
#     hash = argon2.hash_password_raw(
#         time_cost=20, memory_cost=2**18, parallelism=2, hash_len=32, password=password.encode(), salt=b'some salt', type=argon2.low_level.Type.ID)
#     print('Argon2 raw hash: ', binascii.hexlify(hash))

#     argon2Hasher = argon2.PasswordHasher(
#         time_cost=20, memory_cost=2**18, parallelism=2, hash_len=32, salt_len=16)
#     argHash = argon2Hasher.hash(password)
#     print("Argon2 hash (random salt): ", argHash)

#     new_user = {"username": username, "password": argHash}

#     data['users'].append(new_user)

#     print(json.dumps(data))

# def login(username, password, data):
#     for i in data['users']:
#         if i['username'] == username:
#             userPassword = i['password']

#     argon2Hasher = argon2.PasswordHasher(
#         time_cost=20, memory_cost=2**18, parallelism=2, hash_len=32, salt_len=16)
#     argHash = argon2Hasher.hash(password)
#     print("Argon2 hash (random salt): ", argHash)

#     verifyValid = argon2Hasher.verify(userPassword, password)

#     if verifyValid:
#         return print("Correct login")
#     else:
#         return print("Incorrect login")


# def change_password(username, old_password, new_password, data):
#     for i in data['users']:
#         if i['username'] == username:
#             oldPassword = i['password']
#             print('original user: ', i['username'] , i['password'])


#     argon2Hasher = argon2.PasswordHasher(
#         time_cost=20, memory_cost=2**18, parallelism=2, hash_len=32, salt_len=16)

#     verifyValid = argon2Hasher.verify(oldPassword, old_password)

#     if verifyValid:
#         print("Correct login")
    
#     newArgHash = argon2Hasher.hash(new_password)

#     for i in data['users']:
#         if i['username'] == username:
#             i['password'] = newArgHash
#             print('updated user: ', i['username'], i['password'])
        
#     return data['users']



# change_password('bob', 'bob', 'bobo', data)



# register_user('bob', 'bob', data)
# login('bob', 'bob', data)







### RANDOM NUMBER GENERATORS ###


import random, time, secrets

#print(random.randrange(1000000, 9999999))


# EXAMPLE OF WHY NORMAL PRNG ARE LESS SECURE THAN CSPRNG
# random.seed(time.time())
# r1 = random.randrange(1e49, 1e50-1)

# random.seed(time.time())
# r2 = random.randrange(1e49, 1e50-1)

# print("r1 ", r1)
# print("r2 ", r2)



### USING SECRETS LIBRARY FOR A CSPRNG

import secrets
print(secrets.randbelow(int(1e50)))