#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: addr.py
'''
import socket
import os
import getpass

class Addr(object):
    """
    Addr group
    """

    def __init__(self):
        """ Init Addr """
        self.host = socket.gethostname()
            
    def gen_addr(self, protocal, paths=['.']):
        """ Gen addr """
        ret_list = []
        for path in paths:
            path = os.path.realpath(path)
            if protocal == 'ftp':
                ret = 'ftp://' + self.host + path
                ret_list.append(ret)
            elif protocal == 'scp':
                ret = getpass.getuser() + '@' + self.host + ':' + path
                ret_list.append(ret)
        return ret_list

if __name__ == '__main__':
    addr = Addr()
    print addr.gen_addr('ftp')
    print addr.gen_addr('scp')
