# enigmaII
A simple 2 wheel enigma encryption/decryption script.

usage: enigmaII.py [-h] [-d | -e] [-k KEY] [-m MESSAGE] [-o ORDER]

Enigma II Encryption/Decryption device.

optional arguments:
  -h, --help            show this help message and exit
  -d, --decrypt         Decrypt a message
  -e, --encrypt         Encrypt a message
  -k KEY, --key KEY     3 letter key made of alpha characters
  -m MESSAGE, --message MESSAGE
                        Message to encrypt or decrypt
  -o ORDER, --order ORDER
                        Gear order. Must be a permutation of the numbers 5, 6,
                        and 7

Modled after the EnigmaII machine made by Creative Crafthouse
http://www.creativecrafthouse.com/index.php?main_page=product_info&cPath=143&products_id=964
