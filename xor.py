#!/usr/bin/env python
import sys

if len(sys.argv)==3:
        b = bytearray(open(sys.argv[1], 'rb').read())
        for i in range(len(b)):
                b[i] ^= int(sys.argv[2], 16)
        open("xor'd_"+sys.argv[2]+"_"+sys.argv[1], 'wb').write(b)
