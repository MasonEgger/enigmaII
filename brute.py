from enigmaII import decrypt
import itertools
import re
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enigma II Encryption/Decryption brute force.')
    parser.add_argument('-m', '--message', help='Message to encrypt or decrypt')
    args = parser.parse_args()

    if args.message is None:
        parser.print_help()

    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    order = ['5', '6', '7']
    order_perms = list(itertools.permutations(order))
    key_perms = list(itertools.combinations_with_replacement(key, 3))
    alpha_regex = re.compile('[^a-zA-Z]')

    message = alpha_regex.sub('', args.message).lower()

    for x in order_perms:
        for y in key_perms:
            print "ORDER: %s KEY: %s MESSAGE: %s" % (x, y, decrypt(x, y, message).replace(" ", ""))
