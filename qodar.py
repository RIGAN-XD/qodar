import os, sys, time
from time import sleep as waktu

h = '\x1b[1;92m'  # Hijau
xxx = '\33[m'

def animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
        
if __name__=="__main__":
        os.system('git pull')
        animasi(f'\n{xxx}   ({h}ANJING SEMUA{xxx})')
        waktu(3)
