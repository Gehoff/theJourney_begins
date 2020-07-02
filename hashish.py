# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:11:57 2020

@author: Jeff "There are no 2s" Barrett

Hashing
"""

import random
import hashlib

def create_hash(inp):
    random.randint(1, 100) #Useless line to remove Warning
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
    with open("storedhash.txt", "a+") as F:
        if not err_check(pw, site):
            return
        pw = create_hash(pw)
        info = site + ':' + pw + "\n"
        F.write(info)
        return
        

## Check if the hashed Site, Password inputed = Password stored
## UGLY CODE 
def get_pass(pWord, pSite):
    """Returns true or false tuple with splantion string
    arg1 pWord = password, arg2 pSite = website """
    if not err_check(pWord, pSite):
        return (False, "Empty Field")
    ### Test to modularize get_sites, get_pwords and get_all
    sites = get_sites()
    if pSite in sites:
            print(sites)
    with open("storedhash.txt", "r") as F:     
        for line in F:
            #Split the site and password and strip all whitespace
            #or escape characters out
            res = line.split(":")
            res[1] = res[1].strip()
            if pSite in res[0]:
                #if the inputted site is in the file check to 
                #verify it is the same length.
                if len(pSite) != len(res[0]):
                    continue
                if check_hash(pWord, res[1]):
                    return (True, "ACCESS GRANTED!")
                else:
                    return (False, "Uh uh uh, your forget to say the magic word")
    return (False, "THE SITE HAS NOT BEEN LOGGED")

def get_sites():
    sites = []
    try:
        with open("storedhash.txt", "r") as F:
            for line in F:
                res = line.split(":")
                res[0] = res[0].strip()
                sites.append(res[0])
    except:
        sites.append("Empty")
    return sites

def get_pwords():
    pwords = []
    with open("storedhash.txt", "r") as F:
        for line in F:
            res = line.split(":")
            res[1] = res[1].strip()
            pwords.append(res[1])
    return pwords

def get_all():
    data = (get_sites(), get_pwords())
    return data

