# Enigma_Machine

This is a project I did for fun. This is a working Enigma Machine. The Enigma.py script is the entire "machine" part of the original Enigma Machine (i.e. the rotors, the peg boards, and the mechanics of how it worked). The script use_enigma.py provides a script for anyone interested to run. This script includes other necessary inputs for the machine to correctly encrypt and decrypt a message. 

Using the Enigma Machine:
You should only need to edit the use_enigma.py to encrypy and decrypt a message.

First you need to set the rotors. This entails creating a rotor object, setting the rotor encoding, and naming the rotor. At the top of the script there are 5 actual rotor encodings that were used during WWII, however you can create your own rotor encodings. You can do with with the rotors() class. 

You can now create an enigma machine object using the enig_machine() class. Once you've created your rotor objects you need to install the rotors using the install_rotor() method in the enig_machine() class. Here you will need to specify the rotor object (what you called the variable), and the position within the enigma machine you wish to install the rotor (there are currently three possible positions).

Once you've installed the rotors you can now begin encrypting and decrypting messages. Simply call the encode_decode() method within you engima machine object, with a message as a complete text string. It is importantthat this text string only enclude letters, no numbers, or other special characters (spaces are okay). Encrypted and decrypted messages will be in all caps and have no spaces. 

Lastly, for some extra scrabbling of your codes you can set the "plug board". These are letter pairs that you wish to swap positions (for example, 'AB' means you swap every 'A' with a 'B'). You can set up to 10 pairs of letters to swap.
