import re
import sys
import argparse

wheelV = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wheelVI = ['a', 'c', 'e', 'd', 'f', 'h', 'g', 'i', 'k', 'j', 'l', 'n', 'm', 'o', 'q', 'p', 'r', 't', 's', 'u', 'w', 'v', 'x', 'z', 'y', 'b']
wheelVII = ['a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']
wheels = {"5": wheelV, "6": wheelVI, "7": wheelVII}


def rotate(l, n):
    return l[n:] + l[:n]


def encrypt(order, code, message):
    enc1 = rotate(wheels[order[0]], wheels[order[0]].index(code[0]))
    enc2 = rotate(wheels[order[1]], wheels[order[1]].index(code[1]))
    key = rotate(wheels[order[2]], wheels[order[2]].index(code[2]))

    enc_message = ""
    gear = 0
    num_letters = 1
    for let in message:
        if gear == 0:
            index = key.index(let)
            enc_message += enc1[index]
            gear = 1
        elif gear == 1:
            index = key.index(let)
            enc_message += enc2[-index]
            gear = 0
        if num_letters == 4:
            enc_message += " "
            num_letters = 1
        else:
            num_letters += 1

    return enc_message.upper()


def decrypt(order, code, message):
    enc1 = rotate(wheels[order[0]], wheels[order[0]].index(code[0]))
    enc2 = rotate(wheels[order[1]], wheels[order[1]].index(code[1]))
    key = rotate(wheels[order[2]], wheels[order[2]].index(code[2]))

    dec_message = ""
    gear = 0
    num_letters = 1
    for let in message:
        if gear == 0:
            index = enc1.index(let)
            dec_message += key[index]
            gear = 1
        elif gear == 1:
            index = enc2.index(let)
            dec_message += key[-index]
            gear = 0
        if num_letters == 4:
            dec_message += " "
            num_letters = 1
        else:
            num_letters += 1

    return dec_message.upper()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enigma II Encryption/Decryption device.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt a message')
    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt a message')
    parser.add_argument('-k', '--key', help='3 letter key made of alpha characters')
    parser.add_argument('-m', '--message', help='Message to encrypt or decrypt')
    parser.add_argument('-o', '--order', help='Gear order. Must be a permutation of the numbers 5, 6, and 7')

    args = parser.parse_args()

    if args.order is not None or args.key is not None or args.message is not None:
        alpha_regex = re.compile('[^a-zA-Z]')

        # get and validate order
        if len(args.order) != 3 or '5' not in args.order or '6' not in args.order or '7' not in args.order:
            print "Invalid order. Must be a permutation of the numbers 5, 6, and 7"
            sys.exit(1)

        # get and validate code
        key = alpha_regex.sub('', args.key).lower()
        if len(key) != 3:
            print "Invalid key. Must be a 3 letter key made of alpha characters."
            sys.exit(1)

        # get and sanitate message to encrypt
        message = alpha_regex.sub('', args.message).lower()

        if args.encrypt:
            print encrypt(args.order.lower(), key, message)
            sys.exit(0)

        if args.decrypt:
            print decrypt(args.order.lower(), key, message)
    else:
        parser.print_help()
        sys.exit(1)
