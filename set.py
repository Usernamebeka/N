import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)

def baner():
    print(Fore.CYAN+'', Style.BRIGHT)
    print('')
    print("  ___                 _             _   _               ")
    print(" |_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print("  | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print("  | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print(" |___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    res()
    
while True:
    baner()
    print(Style.BRIGHT, Fore.CYAN+"[Настройки]                                     [v2.8.0]")
    res()
    print(Fore.GREEN+"    [1] Запускать Installer вместе с Termux")
    print(Fore.GREEN+"    [2] Обновить/Проверить обновления Installer")
    print(Fore.GREEN+"    [3] Установить последнюю версию Termux")
    print(Fore.GREEN+"    [4] Переместить скачаные директории в /files/home/")
    print(Fore.GREEN+"    [5] Удалить скачаные директории")
    print(Fore.CYAN+"")
    print(Fore.YELLOW+"    [e] Назад")
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')


    
    if inp == '1':
        os.system('clear')
        baner()
        print (Fore.CYAN+'\n Запускать Installer вместе с Termux?')
        res()
        print(Fore.YELLOW+'    [1]'+Fore.YELLOW+' Включить')
        print(Fore.YELLOW+'    [2]'+Fore.YELLOW+' Выключить')
        print(Fore.YELLOW+'')
        print('    [e] выход')
        res()
        tru_101 = input(' Выбери пункт>>> ')

        if tru_101 == '1':
            os.system('clear')
            os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
            os.system('clear')
            print(Fore.GREEN+"\n  Включено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_101 == '2':
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('clear')
            print(Fore.YELLOW+"\n  Выключено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')


    
    if inp == '2':
        os.system('clear')
        baner()
        print(Fore.CYAN+'\n Вы хотите обновить/проверить обновления Installer?')
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Все установлинные вами данные удаляться')
        res()
        tru_201 = input(' Начать [y/n] >>> ')
        if tru_201 == 'y':
            os.system('mv update.py /data/data/com.termux/files/home/')
            os.system('rm ~/.bashrc')
            os.system('echo "cd && python update.py" >> ~/.bashrc')
            while True:
                os.system('clear')
                print(Fore.YELLOW+'\n Перезапустите Termux или создайте новый сезон!')
                tru_202 = input('')
        else:
            os.system('clear')


    
    if inp == '3':
        os.system('xdg-open https://t.me/SYPEXHACK_fail/51')


    
    if inp == '4':
        os.system('clear')
        baner()
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Переместить скачаные директории в /files/home ?')
        res()
        tru_401 = input(' Выбери пункт [y/n] >>> ')
        if tru_401 == 'y':
            os.system('mv PyPhisher /data/data/com.termux/files/home/')
            os.system('mv maskphish /data/data/com.termux/files/home/')
            os.system('mv IP-Tracer /data/data/com.termux/files/home/')
            os.system('mv seeker /data/data/com.termux/files/home/')
            os.system('clear')
            print(Fore.GREEN+"\n Все директории УСПЕШНО перенесены в папку /files/home/")
            res()
            tsu_402 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')

        else:
            os.system('clear')
            

    
    if inp == '5':
        os.system('clear')
        baner()
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить директории?')
        res()
        tru_501 = input(' Продолжить [y/n] >>> ')
        if tru_501 == 'y':
            os.system('clear')
            baner()
            print (Fore.CYAN+'\n Где именно удалить директории?')
            res()
            print(Fore.YELLOW+'    [1]'+Fore.YELLOW+' В папке /files/home/')
            print(Fore.YELLOW+'    [2]'+Fore.YELLOW+' В директории installer')
            print(Fore.YELLOW+'    [3]'+Fore.YELLOW+' Везде')
            print(Fore.YELLOW+'')
            print('    [e] выход')
            res()
            tru_502 = input(' Выбери пункт>>> ')
    
            if tru_502 == '1':
                os.system('clear')
                os.system('rm -fr /data/data/com.termux/files/home/PyPhisher')
                os.system('rm -fr /data/data/com.termux/files/home/maskphish')
                os.system('rm -fr /data/data/com.termux/files/home/IP-Tracerh')
                os.system('rm -fr /data/data/com.termux/files/home/seeker')
                os.system('rm -fr /data/data/com.termux/files/home/CamPhish')
                os.system('rm -fr /data/data/com.termux/files/home/zphisher')
                print(Fore.YELLOW+"\n Все директории в папке /files/home/ УСПЕШНО удалены!")
                res()
                tsu_503 = input(' [Нажмите enter чтобы выйти]')
                os.system('clear')

            if tru_502 == '2':
                os.system('clear')
                os.system('rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                os.system('rm -fr /data/data/com.termux/files/home/installer/maskphish')
                os.system('rm -fr /data/data/com.termux/files/home/installer/IP-Tracer')
                os.system('rm -fr /data/data/com.termux/files/home/installer/seeker')
                os.system('rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                os.system('rm -fr /data/data/com.termux/files/home/installer/zphisher')
                print(Fore.YELLOW+"\n Все директории в директории installer УСПЕШНО удалены!")
                res()
                tsu_503 = input(' [Нажмите enter чтобы выйти]')
                os.system('clear')
                
            if tru_502 == '3':
                os.system('clear')
                os.system('rm -fr /data/data/com.termux/files/home/PyPhisher && rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                os.system('rm -fr /data/data/com.termux/files/home/maskphish && rm -fr /data/data/com.termux/files/home/installer/maskphish')
                os.system('rm -fr /data/data/com.termux/files/home/IP-Tracerh && rm -fr /data/data/com.termux/files/home/installer/IP-Tracer')
                os.system('rm -fr /data/data/com.termux/files/home/seeker && rm -fr /data/data/com.termux/files/home/installer/seeker')
                os.system('rm -fr /data/data/com.termux/files/home/CamPhish && rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                os.system('rm -fr /data/data/com.termux/files/home/zphisher && rm -fr /data/data/com.termux/files/home/installer/zphisher')
                print(Fore.YELLOW+"\n Все директории УСПЕШНО удалены!")
                res()
                tsu_503 = input(' [Нажмите enter чтобы выйти]')
                os.system('clear')
                
            else:
                os.system('clear')
            
        else:
            os.system('clear')
    
    
    if inp == 'e':
        res()
        os.system('clear')
        break
