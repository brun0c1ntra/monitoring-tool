from asyncio.windows_events import NULL
from time import sleep
import psutil
import math
import os

process_name = "firefox.exe"#"Code.exe"
_paths = [ 
          "C:\Crows\Monitoring",
          "C:\\Logs\\2022"
          ]

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def getUsedSpace(paths):
    size = 0
    totalSize = 0
    
    for rootPath in paths:
        for path, dirs, files in os.walk(rootPath):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
    
        print("\nPath ['"+path+"'] "+ convert_size(size))
        totalSize += size
    
    print("\n\ntotal size ==>: "+str(convert_size(totalSize)))
    
    print("============================")
    

def monitorProcess(process_name):
    
        procs = find_procs_by_name(process_name)

        usedCPU = 0
        usedRAM = 0

        if psutil.WINDOWS:
            print("============================\nWindows OS detected")
            
            for process in procs:
                usedCPU += process.cpu_percent(interval=None)/10
                usedRAM += process.memory_percent(memtype="rss")
            
        elif psutil.LINUX:
            print("LINUX")
        elif psutil.POSIX:
            print("POSIX")
        elif psutil.MACOS:
            print("MACOS")
        elif psutil.FREEBSD:
            print("FREEBSD")
        elif psutil.NETBSD:
            print("NETBSD")
        elif psutil.OPENBSD:
            print("OPENBSD")
        elif psutil.BSD:
            print("BSD")
        elif psutil.SUNOS:
            print("SUNOS")
        elif psutil.AIX:
            print("AIX")
        else:
            print("Unknown OS")
            
        print("\nCPU: {:.2f}%".format(usedCPU) + " Mem: {:.2f}%".format(usedRAM))

while True:

    monitorProcess(process_name)

    getUsedSpace(_paths)
    
    sleep(1)