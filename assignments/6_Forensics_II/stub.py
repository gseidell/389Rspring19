# !/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

index = 8
# print (data[index:4])

time= struct.unpack("<L", data[index:index+4])
index = index+4
print("Time: ",time[0])

author = struct.unpack("<ssssssss", data[index:index+8])
index = index+8
tmp = ""
for c in author:
    tmp += str(c)[2]
print("Author",tmp)

sections = struct.unpack("<L", data[index:index+4])[0]
index = index+4

count = 0
f = open('./out.png', 'wb')
while count < sections:
    stype,length = struct.unpack("<LL", data[index:index+8])
    index = index+8

    curr = 0
    print("TYPE",stype)
    print("LENGTH",length)
    tmp = ""
    while(curr<length):
        sectionData = struct.unpack("c", data[index+curr:index+curr+1])
        curr=curr+1
        if(stype == 8):
            f.write(sectionData[0])
        if(length<100):
            tmp = tmp + chr(ord(sectionData[0]))

    index = index+ length
    count= count +1
    print(tmp)
f.close()
