import os, time

from colorama import Fore, Style

os.system('clear')

print(f'\33]0; Installer - Настройки\a',
                  end='', flush=True)


def res():
    print(Style.RESET_ALL)



def baner():
    os.system('clear')
    print(Fore.CYAN+'', Style.BRIGHT)
    print('')
    print("  ___                 _             _   _               ")
    print(" |_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print("  | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print("  | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print(" |___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    res()



def delet():
    if os.path.exists(filename):
      baner()
      print(Fore.YELLOW+" Утилита "+led+" успешно удалена!")
      res()
      del_tool = input(' [Нажмите enter чтобы выйти]')
      os.system('clear')

    else:
      baner()
      print(Fore.YELLOW+" Утилита "+led+" еще не установлена!")
      res()
      del_tool = input(' [Нажмите enter чтобы выйти]')
      os.system('clear')
      


while True:
    os.chdir('/data/data/com.termux/files/home/installer')
    baner()
    print(Style.BRIGHT, Fore.CYAN+"[Github.com/777-FOXik-777/installer]        ["+Fore.YELLOW+"Настройки"+Fore.CYAN+"]")
    res()
    print(Fore.GREEN+"    [1] Запускать Installer вместе с Termux")
    print(Fore.GREEN+"    [2] Обновить/Переустановить Installer")
    print(Fore.GREEN+"    [3] Установить последнюю версию Termux")
    print(Fore.GREEN+"    [4] Переместить скачаные директории в "+Fore.YELLOW+"/files/home/")
    print(Fore.GREEN+"    [5] Добавить утилиту в Installer")
    print(Fore.GREEN+"    [6] Удалить скачаные директории")
    res()
    print(Fore.YELLOW+"    [h] Сообщить об ошибке")
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
        res()
        print(Fore.YELLOW+'    [e] выход')
        res()
        tru_101 = input('  Выбери пункт>>> ')

        if tru_101 == '1':
            os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
            os.system('clear')
            baner()
            res()
            print(Fore.GREEN+"\n  Включено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_101 == '2':
            os.system('rm ~/.bashrc')
            os.system('clear')
            baner()
            res()
            print(Fore.YELLOW+"\n  Выключено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')


    
    if inp == '2':
        os.system('clear')
        baner()
        print(Fore.CYAN+'\n  Вы хотите Обновить/Переустановить Installer?')
        res()
        print(Fore.YELLOW+"  [e] Выход")
        res()
        tru_201 = input('  Продолжить? [y/n] >>> ')
        if tru_201 == 'y':
            os.system('mv update.py /data/data/com.termux/files/home/')
            os.system('rm ~/.bashrc')
            os.system('echo "cd && python update.py" >> ~/.bashrc')
            print(f'\33]0; Создайте новый сезон!\a',
                    end='', flush=True)  
            while True:
                os.system('clear')
                print(Fore.YELLOW+"\n["+Fore.CYAN+"i"+Fore.YELLOW+"] Перезапустите Termux или создайте новый сезон!")
                tru_202 = input('')
        else:
            os.system('clear')


    
    if inp == '3':
        os.system('xdg-open https://t.me/SYPEXHACK_fail/51')
        os.system('clear')


    
    if inp == '4':
        os.system('clear')
        baner()
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Переместить скачаные директории в /files/home ?')
        res()
        tru_401 = input('  Выбери пункт [y/n] >>> ')
        if tru_401 == 'y':
            os.system('mv PyPhisher /data/data/com.termux/files/home/')
            os.system('mv zphisher /data/data/com.termux/files/home/')
            os.system('mv maskphish /data/data/com.termux/files/home/')
            os.system('mv seeker /data/data/com.termux/files/home/')
            os.system('mv CamPhish /data/data/com.termux/files/home/')
            os.system('mv TigerVirus /data/data/com.termux/files/home/')
            os.system('mv CamHacker /data/data/com.termux/files/home/')
            os.system('mv Telephish /data/data/com.termux/files/home/')
            os.system('mv Dnnme2 /data/data/com.termux/files/home/')
            os.system('mv VidPhisher /data/data/com.termux/files/home/')
            os.system('mv Discord-Nitro-Generator-and-Checker /data/data/com.termux/files/home/')
            os.system('clear')
            baner()
            res()
            print(Fore.GREEN+"\n Все директории УСПЕШНО перенесены в папку /files/home/")
            res()
            tsu_402 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')

        else:
            os.system('clear')


    
    if inp == '5':
        os.system('xdg-open https://forms.gle/vMHny8Yp24HQZqLV9')
        os.system('clear')


    
    
    if inp == '6':
            baner()
            print (Fore.CYAN+'\n Где именно удалить директории?')
            res()
            print(Fore.YELLOW+'    [1]'+Fore.YELLOW+' В папке /files/home/')
            print(Fore.YELLOW+'    [2]'+Fore.YELLOW+' В директории installer')
            print(Fore.YELLOW+'    [3]'+Fore.YELLOW+' Везде')
            print(Fore.YELLOW+'')
            print('    [e] выход')
            res()
            tru_602 = input('  Выбери пункт>>> ')
    
            if tru_602 == '1':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить директории в папке /files/home/?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('clear')
                    os.system('rm -fr /data/data/com.termux/files/home/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/VidPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/Telephish')
                    os.system('rm -fr /data/data/com.termux/files/home/Dnnme2')
                    os.system('rm -fr /data/data/com.termux/files/home/Discord-Nitro-Generator-and-Checker')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории в папке /files/home/ УСПЕШНО удалены!")
                    res()
                    tsu_603 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')
        
            if tru_602 == '2':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить директории в директории installer?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/VidPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/Telephish')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/Dnnme2')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/Discord-Nitro-Generator-and-Checker')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории в директории installer УСПЕШНО удалены!")
                    res()
                    tsu_503 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')

    
            if tru_602 == '3':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить все директории?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('rm -fr /data/data/com.termux/files/home/PyPhisher && rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/zphisher && rm -fr /data/data/com.termux/files/home/installer/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/maskphish && rm -fr /data/data/com.termux/files/home/installer/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/seeker && rm -fr /data/data/com.termux/files/home/installer/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/CamPhish && rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/TigerVirus && rm -fr /data/data/com.termux/files/home/installer/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/CamHacker && rm -fr /data/data/com.termux/files/home/installer/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/VidPhisher && rm -fr /data/data/com.termux/files/home/installer/VidPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/Telephis && rm -fr /data/data/com.termux/files/home/installer/Telephis')
                    os.system('rm -fr /data/data/com.termux/files/home/Dnnme2 && rm -fr /data/data/com.termux/files/home/installer/Dnnme2')
                    os.system('rm -fr /data/data/com.termux/files/home/Discord-Nitro-Generator-and-Checker && rm -fr /data/data/com.termux/files/home/installer/Discord-Nitro-Generator-and-Checker')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории УСПЕШНО удалены!")
                    res()
                    tsu_503 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')

            else:
                os.system('clear')


  
    if inp == '55':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')

        filename = "ngrok"
        if os.path.exists(filename):
          Ngrok = ""+Fore.RED+"X"
        else:
          Ngrok = ""+Fore.GREEN+"✓"

        filename = "lochost"
        if os.path.exists(filename):
          Localhost = ""+Fore.RED+"X"
        else:
          Localhost = ""+Fore.GREEN+"✓"
      
        filename = "IP"
        if os.path.exists(filename):
          IPTracer = ""+Fore.RED+"X"
        else:
          IPTracer = ""+Fore.GREEN+"✓"

      
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
      
        filename = "PyPhisher"
        if os.path.exists(filename):
          PyPhisher = ""+Fore.GREEN+"✓"
        else:
          PyPhisher = ""+Fore.RED+"X"

        filename = "zphisher"
        if os.path.exists(filename):
          Zphisher = ""+Fore.GREEN+"✓"
        else:
          Zphisher = ""+Fore.RED+"X"

        filename = "k-fuscator"
        if os.path.exists(filename):
          Kfuscator = ""+Fore.GREEN+"✓"
        else:
          Kfuscator = ""+Fore.RED+"X"

        filename = "TigerVirus"
        if os.path.exists(filename):
          TigerVirus = ""+Fore.GREEN+"✓"
        else:
          TigerVirus = ""+Fore.RED+"X"

        filename = "maskphish"
        if os.path.exists(filename):
          Maskphish = ""+Fore.GREEN+"✓"
        else:
          Maskphish = ""+Fore.RED+"X"

        filename = "seeker"
        if os.path.exists(filename):
          Seeker = ""+Fore.GREEN+"✓"
        else:
          Seeker = ""+Fore.RED+"X"

        filename = "CamHacker"
        if os.path.exists(filename):
          CamHacker = ""+Fore.GREEN+"✓"
        else:
          CamHacker = ""+Fore.RED+"X"

        filename = "VidPhisher"
        if os.path.exists(filename):
          VidPhisher = ""+Fore.GREEN+"✓"
        else:
          VidPhisher = ""+Fore.RED+"X"

        filename = "Telephish"
        if os.path.exists(filename):
          Telephish = ""+Fore.GREEN+"✓"
        else:
          Telephish = ""+Fore.RED+"X"

        filename = "Dnnme2"
        if os.path.exists(filename):
          Dnnme2 = ""+Fore.GREEN+"✓"
        else:
          Dnnme2 = ""+Fore.RED+"X"

        filename = "Discord-Nitro-Generator-and-Checker"
        if os.path.exists(filename):
          Discord = ""+Fore.GREEN+"✓"
        else:
          Discord = ""+Fore.RED+"X"
      
      
        while True:
          baner()
          print(Style.BRIGHT, Fore.CYAN+"   Выбери какую именно удалить Утилиту?")
          res()
          print(Fore.YELLOW+"    [1] Ngrok        ("+Ngrok+""+Fore.YELLOW+")  [11] CamHacker      ("+CamHacker+""+Fore.YELLOW+")")
          print(Fore.YELLOW+"    [2] Localhost    ("+Localhost+""+Fore.YELLOW+")  [12] VidPhisher     ("+VidPhisher+""+Fore.YELLOW+")")
          print(Fore.YELLOW+"    [3] PyPhiser     ("+PyPhisher+""+Fore.YELLOW+")  [13] Telephish      ("+Telephish+""+Fore.YELLOW+")")
          print(Fore.YELLOW+"    [4] Zphisher     ("+Zphisher+""+Fore.YELLOW+")  [14] Dnnme2         ("+Dnnme2+""+Fore.YELLOW+")")
          print(Fore.YELLOW+"    [5] K-fuscator   ("+Kfuscator+""+Fore.YELLOW+")  [15] Discord        ("+Discord+""+Fore.YELLOW+")")
          print(Fore.YELLOW+"    [6] TigerVirus   ("+TigerVirus+""+Fore.YELLOW+")  ")
          print(Fore.YELLOW+"    [7] Maskphish    ("+Maskphish+""+Fore.YELLOW+")  ")
          print(Fore.YELLOW+"    [8] IP-Tracer    ("+IPTracer+""+Fore.YELLOW+")  ")
          print(Fore.YELLOW+"    [9] Seeker       ("+Seeker+""+Fore.YELLOW+")  ")
          res()
          print(Fore.RED+"    [a] Выбрать все утилиты")
          res()
          print(Fore.YELLOW+"    [e] Назад")
          res()
          tsu_501 = input('  Выбери пункт>>> ')
          os.system('clear')



          if tsu_501 == '1':
              baner()
              print(Fore.YELLOW+" Не возмжно удалить Ngrok! \n (Так как он устанавливается напримую в Termux)")
              res()
              del_tool = input(' [Нажмите enter чтобы выйти]')
              os.system('clear')
          
          if tsu_501 == '2':
              baner()
              print(Fore.YELLOW+" Не возмжно удалить Localhost! \n (Так как он устанавливается напримую в Termux)")
              res()
              del_tool = input(' [Нажмите enter чтобы выйти]')
              os.system('clear')

          if tsu_501 == '8':
              baner()
              print(Fore.YELLOW+" Не возмжно удалить IP-Tracer! \n (Так как он устанавливается напримую в Termux)")
              res()
              del_tool = input(' [Нажмите enter чтобы выйти]')
              os.system('clear')

          
          
          if tsu_501 == '3':
              filename = "PyPhisher"
              led = "PyPhish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PyPhisher')
              PyPhisher = ""+Fore.RED+"X"

          if tsu_501 == '4':
              filename = "zphisher"
              led = "Zphisher"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/zphisher')
              Zphisher = ""+Fore.RED+"X"

          if tsu_501 == '5':
              filename = "k-fuscator"
              led = "K-fuscator"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/k-fuscator')
              Kfuscator = ""+Fore.RED+"X"

          if tsu_501 == '6':
              filename = "TigerVirus"
              led = "TigerVirus"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/TigerVirus')
              TigerVirus = ""+Fore.RED+"X"

          if tsu_501 == '7':
              filename = "maskphish"
              led = "Maskphish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/maskphish')
              Maskphish = ""+Fore.RED+"X"

          if tsu_501 == '9':
              filename = "seeker"
              led = "Seeker"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/seeker')
              Seeker = ""+Fore.RED+"X"

          if tsu_501 == '11':
              filename = "CamHacker"
              led = "CamHacker"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/CamHacker')
              CamHacker = ""+Fore.RED+"X"

          if tsu_501 == '12':
              filename = "VidPhisher"
              led = "VidPhisher"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/VidPhisher')
              VidPhisher = ""+Fore.RED+"X"

          if tsu_501 == '13':
              filename = "Telephish"
              led = "Telephish"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Telephish')
              Telephish = ""+Fore.RED+"X"

          if tsu_501 == '14':
              filename = "Dnnme2"
              led = "Dnnme2"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Dnnme2')
              Dnnme2 = ""+Fore.RED+"X"

          if tsu_501 == '15':
              filename = "Discord-Nitro-Generator-and-Checker"
              led = "Discord"
              delet()
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Discord-Nitro-Generator-and-Checker')
              Discord = ""+Fore.RED+"X"


          
          if tsu_501 == 'a':
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/PyPhisher')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/maskphish')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/seeker')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/CamPhish')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/zphisher')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/TigerVirus')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/CamHacker')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/VidPhisher')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Telephish')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Dnnme2')
              os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/Discord-Nitro-Generator-and-Checker')
              PyPhisher = "X"
              Zphisher = "X"
              Kfuscator = "X"
              TigerVirus = "X"
              Maskphish = "X"
              Seeker = "X"
              CamHacker = "X"
              VidPhisher = "X"
              Telephish = "X"
              Dnnme2 = "X"
              Discord = "X"

              baner()
              print(Fore.YELLOW+" Утилиты успешно удалены! \n (Кроме: Ngrok, Localhost и IP-Tracer)")
              res()
              del_tool = input(' [Нажмите enter чтобы выйти]')
              os.system('clear')


          if tsu_501 == 'e':
              break

















  
    if inp == 'h':
        os.system('xdg-open https://t.me/SYPEXHACK_help_bot')
        os.system('clear')

    
    
    if inp == 'e':
        res()
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('clear')
        break
