# clientserver
## Project
This project builds a client server network allowing different capabilities. Features include a selection menu for a user, sending a dictionary formatted in JSON and the ability to send an encrypted text file. This is written in PEP standards and includes exception handling. 
## What is included
This repository contains the following files.

server.py - The server file for the client server network.

client.py - The client file for the client server network.

main.py - To be ran  with the server file. Contains a user selection menu.

generators.py - This file creates random pieces of data that can be used for the client server network.

file_handler.py - This code handles the files based on the user selection and uses the randomly generated data from generators.py.

unittest.py - Code showing two tests. Test one to show the expected data is being generated. Test two is testing the use of json.dumps. 

directorytree.py - organises files into directories.

requirements.txt - shows all the packages needed to install for the running of the client server network. 

## Language
The language used was Python3
## Run and installation
To run the code ensure you have installed the packages on the requirements.txt.

To install the package type    pip install -r requirements.txt into your command line.

To clone, type the below into your command line.      
-git clone https://github.com/MollyBaxt/clientserver.git
This will save the folder containing all the files within the repository. 

In one terminal run the server.py file, in a separate terminal run the main.py file.

## License
Copyright [2022] [TARIQ ABUSAQRI, MOLLY-ROSE BAXTER, KARL DAVIS]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

