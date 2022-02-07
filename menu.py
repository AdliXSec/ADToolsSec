from isi import *
from error import error



def menu():
    print("\n")
    print(" ============== MENU ===================")
    print(" |                                     |")
    print(" | [1] Get IP From Host Name           |")
    print(" | [2] TRACEROUTE IP                   |")
    print(" | [3] Spam WA #for windows            |")
    print(" | [4] Extracting wifi password        |")
    print(" | [5] YouTube Download mp4            |")
    print(" | [6] Port Scanning                   |")
    print(" | [7] Hash Md5                        |")
    print(" | [8] Hash sha1                       |")
    print(" | [9] Md5 Cracking                    |")
    print(" | [10] Sha1 Cracking                  |")
    print(" | [11] Wordpress BruteForce           |")
    print(" | [12] TCP Sweep                      |")
    print(" | [13] Chek sinyal                    |")
    print(" | [14] YouTube Download mp4           |")
    print(" | [15] Google translate               |")
    print(" | [16] YouTube Download mp3           |")
    print(" | [x] Installing                      |")
    print(" | [0] LogOut :)                       |")
    print(" |                                     |")
    print(" =======================================")
    print("")
    print(" =======================================")
    print(" |")
    pilih = input(" |= Select Menu => ")
    print("\n")

    if pilih == str(1):
        getIP()
    elif pilih == str(2):
        tracerouter()
    elif pilih == str(3):
        spamwapc()
    elif pilih == str(4):
        wifipw()
    elif pilih == str(5):
        ytdown()
    elif pilih == str(6):
        pscan()
    elif pilih == str(7):
        hashmd5()
    elif pilih == str(8):
        hashsha1()
    elif pilih == str(9):
        md5crack()
    elif pilih == str(10):
        sha1crack()
    elif pilih == str(11):
        wpbf()
    elif pilih == str(12):
        tcpsweep()
    elif pilih == str(13):
        ceksinyal()
    elif pilih == str(14):
        ytdown()
    elif pilih == str(15):
        gtrans()
    elif pilih == str(16):
        ytdownmp3()
    elif pilih == "x":
        install()
    elif pilih == str(0):
        print(" Thank You for Your Visit")
        exit()
    else:
        print(" Command not found ",pilih)