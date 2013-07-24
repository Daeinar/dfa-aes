#!/usr/bin/env python
#
# Licensed by "The MIT License". See file LICENSE.
#
# Script to simulate fault injections on AES-128.
# Prints correct and corresponding faulty ciphertext.
#
# Usage: ./inject nr_of_example fault_location
#
# fault_location must be in {0,...,15}.
#
import sys
from aes import *

# (plaintext,key,fault_value)
vectors = [
   (0x00000000000000000000000000000000,0x00000000000000000000000000000000,0x01), # 0
   (0xffffffffffffffffffffffffffffffff,0xffffffffffffffffffffffffffffffff,0xff), # 1
   (0x1234567890abcdef1234567890abcdef,0x1234567890abcdef1234567890abcdef,0x02), # 2
   (0xfedcba0987654321fedcba0987654321,0xfedcba0987654321fedcba0987654321,0x02), # 3
   (0x636f64656d696c6573636f64656d696c,0x6a6d736a75657475736a6d7374756574,0x02), # 4
   (0xbaddecafbaddecafbaddecafbaddecaf,0xbaddecafbaddecafbaddecafbaddecaf,0xba), # 5
   (0xdeadc0dedeadc0dedeadc0dedeadc0de,0xdeadc0dedeadc0dedeadc0dedeadc0de,0xde), # 6
   (0x1234567890abcdef1234567890abcdef,0x10000005200000063000000740000008,0x02)] # 7

if __name__ == '__main__':

  assert int(sys.argv[1]) < len(vectors)
  assert int(sys.argv[1]) >= 0

  v = vectors[int(sys.argv[1])]

  p = v[0]
  key = v[1]
  c = encrypt(p,key)
  ct = encrypt(p,key,fault=v[2],floc=int(sys.argv[2]))
  print "{:032x} {:032x}".format(c,ct)
