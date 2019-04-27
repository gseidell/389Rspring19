#!/usr/bin/env python3

import hashlib
import string

def crack():
   	
    f= open("../hashes.txt","r")
    hashes = f.readlines()
    hashes = [a[0:-1] for a in hashes]
    f.close()

    f= open("../passwords.txt","r")
    passwords = f.readlines()
    passwords = [a[0:-1] for a in passwords]
    f.close()

    # hashes = ['a','b']# open and read hashes.txt
    # passwords = ['a','b']# open and read passwords.txt
    characters = string.ascii_lowercase
    hashes = ["8447305ebfc40a541f8503f6074444c03eeaed2610447859b39fce65ecd3a4c6"]
    for c in characters:
        for p in passwords:
            tmp = hashlib.sha256((c+p).encode("UTF-8")).hexdigest()
            # print(tmp)
            if tmp in hashes:
                print(c+p,":",tmp)
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
