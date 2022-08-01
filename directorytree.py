import os

path = os.getcwd()

for root, dirname, files in os.walk(path):
    for x in files:
        print(os.path.join(root, x))