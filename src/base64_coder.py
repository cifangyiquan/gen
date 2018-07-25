#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: base_code.py
Author: linguanchen
Date: 2018/07/25 14:06:18
"""
import base64

class Base64_coder(object):
    """
    base64 group
    """
    
    def __init__(self):
        """ Init """
        pass

    def gen_base64(self, cmd, data):
        """ Gen base64 code """
        ret_list = []
        for item in data:
            if cmd == 'encode':
                ret = base64.urlsafe_b64encode(item)
                ret_list.append(ret)
            elif cmd == 'decode':
                ret = base64.urlsafe_b64decode(item)
                ret_list.append(ret)
            else:
                print 'cmd error: use encode/decode'
        return ret_list

if __name__ == '__main__':
    base_coder = Base64_coder()
    print base_coder.gen_base64('encode', ['abc'])
    print base_coder.gen_base64('decode', ['YQ=='])
    print base_coder.gen_base64('decode', ['YWJj'])
