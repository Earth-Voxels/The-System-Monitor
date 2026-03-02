import psutil
import time
from colorama import Fore, Style, init

init(autoreset=True)


print(Fore.MAGENTA + ">>>>>>>>>>>>>>>>>System>>>>>>>>>>>>>>>>>>")
print(Fore.MAGENTA + "<<<<<<<<<<<<<<<Monitor<<<<<<<<<<<<<<<<<<<")
print(Fore.CYAN + "Made by Earth Voxels :D")
print(Fore.RED + "CPU: ")
print(Fore.GREEN + "RAM: ")
print(Fore.BLUE + "DISK: ")

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    print("\033[3A", end="")

    print(Fore.RED + f"CPU:  {cpu}%      ")
    print(Fore.GREEN + f"RAM:  {ram}%      ")
    print(Fore.BLUE + f"DISK: {disk}%     ")

    time.sleep(0.5)
