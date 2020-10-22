# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:11:57 2020

@author: Jeff

Hashing
"""

import hashlib

def create_hash(inp):
    inp = hashlib.sha256(inp.encode())
    return inp.hexdigest()

def check_hash(inp, priv):
    inp = create_hash(inp)
    if inp == priv:
        return True
    else:
        return False

def err_check(pw, site):
    if pw == "" or site == "":
        return False
    else:
        return True
    
def store_pass(pw, site):
    with open("storedhash.txt", "a") as F:
        if not err_check(pw, site):
            return
        pw = create_hash(pw)
        info = site + ':' + pw + "\n"
        F.write(info)
        return 

## Check if the hashed Site, Password inputed = Password stored
## UGLY CODE 
def get_pass(pWord, pSite):
    if not err_check(pWord, pSite):
        return
    with open("storedhash.txt", "r") as F:
        for line in F:
            res = line.split(":")
            res[1] = res[1].strip()
            if pSite in res[0]:
                if len(pSite) != len(res[0]):
                    continue
                if check_hash(pWord, res[1]):
                    return "ACCESS GRANTED!"
                else:
                    return "Uh uh uh, your forget to say the magic word"
    return "THE SITE HAS NOT BEEN LOGGED"
