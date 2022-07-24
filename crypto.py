import rsa

# generate public and private keys with rsa.newkeys method.
# this method accepts key length as its parameter.
# key length should be at least 16
public_key, private_key = rsa.newkeys(512, accurate=False)


def encrypt_data(plain_text):
    return rsa.encrypt(plain_text.encode(),
                       public_key)


def decrypt_data(encoded_text):
    return rsa.decrypt(encoded_text, private_key).decode()
