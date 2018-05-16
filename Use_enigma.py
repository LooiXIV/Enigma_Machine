#!/anaconda3/bin/env python3
# -*-utf-8-*-

import Enigma

# different rotor encodings
I_K_encoding = 'PEZUOHXSCVFMTBGLRINQJWAYDK'

II_K_encoding = 'ZOUESYDKFWPCIQXHMVBLGNJRAT'

III_K_encoding = 'EHRVXGAOBQUSIMZFLYNWKTPDJC'

UKW_K_encoding = 'IMETCGFRAYSQBZXWLHKDVUPOJN'

ETW_K_encoding = 'QWERTZUIOASDFGHJKPYXCVBNML'

# creating rotor objects for the enigma machine
I_K = Enigma.rotors()
I_K.init(I_K_encoding, 'I_K')

II_K = Enigma.rotors()
II_K.init(II_K_encoding, 'II_K')

III_K = Enigma.rotors()
III_K.init(III_K_encoding, 'III_K')

# create the enigma machine and set the rotors into
# the enigma machine
enig = Enigma.enig_machine()
enig.install_rotor(I_K, pos=1)
enig.install_rotor(II_K, pos=2)
enig.install_rotor(III_K, pos=3)
# set the plug board
enig.set_plug_board(plug_board=
        ['AA', 'BB', 'CC', 'DD', 'EE',
        'FF', 'GG', 'HH', 'II', 'JJ'])

message = 'The Brown Fox Jumped Over the Lazy Dog'

encrypted = enig.encode_decode(message, [0,0,0])
print(message, encrypted)

decrypted = enig.encode_decode(encrypted, [0,0,0])

print(encrypted, decrypted)
