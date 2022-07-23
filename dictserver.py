import socket               # Import socket module
import json


s = socket.socket()      # Create a socket object
host = "localhost"     
print(host)              # Get local machine name
port = 1233              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send('Thank you for connecting'.encode('utf-8'))

# State the dictionary
   dict = {'Common Name':'Otter', 'Scientific Name':'Mustelidae', 'Type':'Mammal', 'Size':'2 to 6 feet', 'Weight':'10 to 75 pounds'}
# Serializing the dictionary to send to client
   if __name__=='__main__':
    json_dict = json.dumps(dict)
    print(type(json_dict)) # Print the class type
    print(json_dict) 
  
