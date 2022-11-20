import os
import time
import webbrowser
while True:
    print(f"--------------------------------------------------------------------------------------------------------------")
    print("                                        Wellcome to Linux tool                                                 ")
    print("                                         create by Hoang Phuc                                                   ")
    print("                                        Mail:binbuop@gmail.com                                                  ")
    print("                                        Phone number:+8436900376                                                ")
    print(f"--------------------------------------------------------------------------------------------------------------")
    time.sleep(2)
    print('Please wait...')
    time.sleep(5)
    os.system('clear')
    print(f"--------------------------------------------------------------------------------------------------------------")
    print("                                            1.Update system                                                       ")
    print("                                            2.Check info os                                                       ")
    print("                                         3.Change keyboard langue                                                 ")
    print("                                            4.Run app window                                                      ")
    print("                                   5.Check info computer, cpu, ram, screen")
    print("                                                6.Exit                                                            ")
    print(f"--------------------------------------------------------------------------------------------------------------")
    s = input("$ ")
    if s == "1":
        print("Ok, I'm checking...")
        time.sleep(3)
        os.system('sudo apt-get upgrade')
        time.sleep(1)
    elif s == "2":
        print("Get app checking...")
        os.system('sudo apt install neofetch')
        os.system('neofetch')
    elif s == "3":
        print("Ok")
        time.sleep(1)
        print("If you not a Vietnamese, please open translate")
        url = "https://vinasupport.com/bo-go-tieng-viet-ibus-bamboo-tren-ubuntu-20-04-lts/"
        webbrowser.open(url, new=0, autoraise=True)
    elif s == "4":
        print("Please wait 3 second")
    elif s == "5":
        print("Connect")
        time.sleep(3)
        print("UPDATE APP...")
        time.sleep(2)
        print("GET APP...")
        time.sleep(2)
        print("Install...")
        time.sleep(1)
        os.system('sudo apt install screenfetch')
        os.system('clear')
        time.sleep(1)
        print("Run app")
        os.system('screenfetch')
    elif s == "6":
        print("Close app...")
        time.sleep(1)
        exit()
