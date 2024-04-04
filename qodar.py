import requests,json,os,sys,random,datetime,time,re,platform,subprocess
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich import print as cetak
from rich.panel import Panel as nel
x = '\33[m'
h = '\x1b[1;92m'
def asu():
        animasi(f'\n{x}   ({h}SEDANG ADA PERBAIKAN JALAN TOL HARAP SABAR GAK BISA JALAN DULU{x})')
def animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
if __name__=="__main__":
        os.system('git pull')
        asu()
