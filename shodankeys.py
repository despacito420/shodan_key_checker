#!/usr/bin/python3
# coding: utf-8
# Quick script I wrote for sorting and categorizing Shodan API
# keys 'borrowed' en masse from Github.
# The reason for discerning between paid and unpaid keys, is we
# can do more with a paid key, so its best to not burn those on
# just blasting out queries all day erry day.
#
# Author: skyhighatrist \ @dailydavedavids \ 0x27.me
#         despacito420 - quick adapt to python3
# Licence: WTFPL \ http://wtfpl.net
# BTC: 1F3sPdKSEL9mM8LBnymGG8Dv3QCPDSRYeh
# Ver: 05102015.1
# https://github.com/0x27

import shodan
import sys


def test(key):
    api = shodan.Shodan(key)
    print("Testing Key: {}".format(key))
    try:
        info = api.info()
    except Exception:
        print("Key {} is invalid!".format(key))
        return False, False
    # this seems to be how they are categorized
    if info['plan'] == 'dev' or info['plan'] == 'edu':
        print("Key {} appears to be valid, and bonus, paid!".format(key))
        return True, True
    elif info['plan'] == 'oss':  # however I might be wrong. oh well.
        print("Key {} appears to be valid! Not paid for though!".format(key))
        return True, False


def main(args):
    if len(args) != 2:
        sys.exit(
            "Shodan API Key List Checker (for testing githubbed keys)\nusage: {} keys-to-test.txt".format(args[0]))
    f = open(args[1], "r")
    keys = f.readlines()
    valid_keys = []
    paid_keys = []
    comm_keys = []
    for key in keys:
        key = key.strip()
        is_valid, is_paid = test(key=key)
        if is_valid == True:
            valid_keys.append(key)
            if is_paid == True:
                paid_keys.append(key)
            else:
                comm_keys.append(key)
        else:
            pass
    print("Acquired {} valid keys".format(len(valid_keys)))
    print("Acquired {} paid-keys".format(len(paid_keys)))
    print("Acquired {} community-keys".format(len(comm_keys)))
    print("Paid Keys...")
    for key in paid_keys:
        print(key)
    print("Community Keys...")
    for key in comm_keys:
        print(key)


if __name__ == '__main__':
    main(sys.argv)
