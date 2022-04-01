import os, socket, subprocess, time, threading, urllib, wmi, base64, hashlib, requests, sys
import pyautogui as spam
import urllib.request
import urllib.parse
from googletrans import Translator
from pytube import YouTube
from datetime import datetime
from queue import Queue
from bs4 import BeautifulSoup
from tampilan import *
from menu import *
import platform



if platform.system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'


jawab = 'y'
tampilan()
print("")
print("")
print(" =======================================================================")
print(" |")

pass1 = input(" |= Enter Password => ")
print("")

password = "25e6ee973cf86bc5cf810bc9aff780df19ae4d79"
sha = hashlib.sha1()
sha.update(pass1.encode("utf-8"))

if(sha.hexdigest() == password):
    while(jawab == 'y'):
        tampilan()
        infouser()
        menu()
        print("")
        jawab = input(" Lanjut Lagi? (y/n) ")
        if(jawab == 'n'):
            print("")
            print(" Thank You for Your Visit")
            exit()
        elif(jawab == ""):
            os.system(hapus)
            os.system("color c")
            print(" =====================================================")
            print(" |                                                   |")
            print(" |            Password cannot be empty               |")
            print(" |                                                   |")
            print(" =====================================================")

elif(pass1 == ""):
    os.system("color c")
    print(" =====================================================")
    print(" |                                                   |")
    print(" |            Password cannot be empty               |")
    print(" |                                                   |")
    print(" =====================================================")
else:
    os.system("color c")
    print(" =====================================================")
    print(" |                                                   |")
    print(" |==========> password (",pass1,") is wrong          ")
    print(" |                                                   |")
    print(" =====================================================")
    exit()
