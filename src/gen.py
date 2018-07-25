#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gen main file
"""
import argparse
import sys
import os
import path

HOME = os.path.dirname(os.path.realpath(__file__))
sys.path.append(HOME + '/./')
import addr
import base64_coder

def addr_func(args):
    """addr commands"""
    addr_item = addr.Addr()
    if len(args.path) == 0:
        args.path = ['./']
    for ret in addr_item.gen_addr(args.protocal, args.path):
        print ret


def echo(args):
    """echo"""
    for greeting in args.greetings:
        sys.stdout.write(greeting + ' ')
    sys.stdout.write('\n')


def base64coder_func(args):
    """base64 coder"""
    coder = base64_coder.Base64_coder()
    for ret in coder.gen_base64(args.command, args.data):
        print ret


def main():
    """ main function"""
    parser = argparse.ArgumentParser(description="Gen data for wanting")
    subparsers = parser.add_subparsers(help='commands')

    # addr command
    addr_parser = subparsers.add_parser('addr', help='gen an address')
    addr_parser.add_argument('protocal', action='store', help='the address protocal')
    addr_parser.add_argument('path', action='store', nargs='*', help='the path')
    addr_parser.set_defaults(func=addr_func)

    # echo command
    echo_parser = subparsers.add_parser('echo', help='gen echo')
    echo_parser.add_argument('greetings', action='store', nargs='*', help='greetings')
    echo_parser.set_defaults(func=echo)

    # base64 command
    base64coder_parser = subparsers.add_parser('base64', help='gen base64 code')
    base64coder_parser.add_argument('command', action='store', help='encode/decode')
    base64coder_parser.add_argument('data', action='store', nargs='*', help='data to code')
    base64coder_parser.set_defaults(func=base64coder_func)

    args = parser.parse_args()
    args.func(args)
        

if __name__ == '__main__':
    main()
