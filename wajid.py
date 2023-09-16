#coding=utf-8
import os, sys, platform

os.system('rm -rf Wsjid.so Ali32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Wajid.so Ali32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '32bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/WA-143/executables/blob/main/Wajidali.cpython-311.so?raw=true -o Wajidali.so') 
        import Wajid
    else:
        import Wajid

elif bit == '32bit':
    if not os.path.isfile('Sarfraz32.so'):
        os.system('curl -L https://github.com/WA-143/executables/blob/main/Wajid32.cpython-311.so?raw=true -o Wajidz32.so') 
        import Wajid32
    else:
        import Wajid32