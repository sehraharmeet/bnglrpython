from colorama import  Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.CYAN + "\n====================================")
    print(Fore.GREEN + "     SMART PORTFOLIO MANAGER")
    print(Fore.CYAN + Style.BRIGHT + "     Share Market Simulator")
    print(Fore.CYAN + "====================================")

if __name__ == "__main__":
    main()