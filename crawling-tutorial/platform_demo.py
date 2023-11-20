import platform

def printOsInfo():
    Os = 'OS'
    OsVersion = 'OS Version'
    print(f'{Os:10s} : ', platform.platform())
    print(f'{Os:10s} : ', platform.system())
    print(f'{OsVersion:10s} : ', platform.version())

printOsInfo()

info = platform.uname()
# print(info)

print(info.processor)

import os

print(os.cpu_count())

import psutil

def printSystemInfo():
    print('Process information  : ', platform.processor())
    print('Process Architecture : ', platform.machine())
    print('CPU Cores            : ', os.cpu_count())
    print('RAM Size             : ', str(round(psutil.virtual_memory().total / (1024.0 **3))) + "(GB)")

printSystemInfo()