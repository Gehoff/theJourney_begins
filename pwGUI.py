# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:45:20 2020

@author: Jeff

GUI FOR PASSWORD STORAGE
"""

import hashish as hsh

import tkinter as tk
mainWin = tk.Tk("It's A Secret to Everyone", className = "PW PROTECT")

#STRING VARIABLES 
res = tk.StringVar(mainWin, value = None, name = "Results")
strPass = tk.StringVar(mainWin, value = None, name = "Pass")
strSite = tk.StringVar(mainWin, value = None, name = "Site")
chkPass = tk.IntVar(mainWin)

#OTHER VARIABLES
WIN_WIDTH = 400
WIN_HEIGHT = 150
MAX_INPUT = 5


def show_pass():
    print("chk: " + str(chkPass.get()))
    if chkPass.get():
        enPass.config(show = "")
    else:
        enPass.config(show = "*")

def clear_field():
    enSite.delete(0, 'end')
    enPass.delete(0, 'end')
    res.set("")
    
 ##btn = int: 1 stores, 2 will get plaintext maybe, 3 tests   
def send_pass(btn):
    pw =  str(strPass.get())
    site = str(strSite.get())
    clear_field()
    if pw == "" or site == "":
        res.set("SOMETHING FEELS EMPTY...")
        return
    if btn == 1:
        hsh.store_pass(pw, site)
        res.set("PASSWORD STORED")
        return
    if btn == 3:
        ans = hsh.get_pass(pw, site)
        if ans == "ACCESS GRANTED!":
            res.set(ans)
        else:
            res.set(ans)
        return

#WIDGETS
enPass = tk.Entry(mainWin, show = '*', textvariable = strPass)
enSite = tk.Entry(mainWin, textvariable = strSite)

lblRes = tk.Label(mainWin, textvariable = res)
lblPass = tk.Label(mainWin, text = "Enter Password: ")
lblSite = tk.Label(mainWin, text = "Enter Site: ")

btnGetPass = tk.Button(mainWin, text = "Get Password")
btnGetPass.config(state = "disabled")
btnStorePass = tk.Button(mainWin, text = "Store Password", 
                         command = lambda : send_pass(1))
btnTestPass = tk.Button(mainWin, text = "Test Password", 
                        command = lambda : send_pass(3))
btnClear = tk.Button(mainWin, text = "Clear", command = clear_field)

chkShowPw = tk.Checkbutton(mainWin, text = "SHOW", variable = chkPass,
                           command = show_pass)

#Set widgets in grid
enSite.grid(row = 3, column = 2)
enPass.grid(row = 4, column = 2)
lblPass.grid(row = 4, column = 1)
lblSite.grid(row = 3, column = 1)
btnStorePass.grid(row = 5, column = 1)
btnGetPass.grid(row = 5, column = 2)
btnTestPass.grid(row = 5, column = 3)
btnClear.grid(row = 5, column = 6)
lblRes.grid(row = 6, columnspan = 5)
chkShowPw.grid(row = 4, column = 3)
mainWin.lift()
mainWin.minsize(WIN_WIDTH, WIN_HEIGHT)
mainWin.grid_anchor(anchor = "center")
mainWin.mainloop()



