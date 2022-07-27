import rsa
import base64

pub, priv = rsa.newkeys(512)

message_to_send = "Hello Vlad!"
b_message = message_to_send.encode()
encrypted = rsa.encrypt(b_message, pub)
encrypted_b64 = base64.b64encode(encrypted)
encrypted_b64_string = encrypted_b64.decode()
print(type(b_message))
# -- sending via socket --
message_to_recieve = encrypted_b64_string
encrypted_b64 = message_to_recieve.encode()
encrypted = base64.b64decode(encrypted_b64)
b_final_message = rsa.decrypt(encrypted, priv)
final_message = b_final_message.decode()