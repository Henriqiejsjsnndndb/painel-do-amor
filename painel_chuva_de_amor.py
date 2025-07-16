import time
import sys
import webbrowser
from colorama import init, Fore, Back, Style

init(autoreset=True)

def type_effect(text, delay=0.03, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blinking(text, times=6, delay=0.4, color=Fore.RED + Style.BRIGHT):
    for _ in range(times):
        sys.stdout.write(color + text + Style.RESET_ALL + '\r')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(delay)
    print(color + text + Style.RESET_ALL)

def progress_bar(duration=3, length=30):
    sys.stdout.write(Fore.CYAN + "[")
    sys.stdout.flush()
    for i in range(length):
        time.sleep(duration/length)
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
    sys.stdout.write(Fore.CYAN + "]\n" + Style.RESET_ALL)
    sys.stdout.flush()

def hacker_ascii_art():
    art = f"""
{Fore.GREEN}
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗ █████╗ ██████╗ ██╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
███████║███████║██║     █████╔╝ █████╗  ███████║██████╔╝ ╚████╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██║██╔═══╝   ╚██╔╝  
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██║        ██║   
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝   

{Style.RESET_ALL}
"""
    print(art)

def main():
    # Limpa a tela e fundo preto
    print(Back.BLACK + Fore.GREEN + Style.BRIGHT + "\033c", end="")

    hacker_ascii_art()

    type_effect("INICIANDO SEQUÊNCIA DE INVASÃO...", delay=0.06, color=Fore.LIGHTGREEN_EX)
    time.sleep(0.7)
    type_effect("[+] Conectando à rede oculta...", delay=0.04, color=Fore.YELLOW)
    time.sleep(0.6)
    type_effect("[+] Estabelecendo túnel seguro...", delay=0.04, color=Fore.YELLOW)
    time.sleep(0.6)
    type_effect("[!!!] AUTENTICANDO... AGUARDE", delay=0.06, color=Fore.RED + Style.BRIGHT)
    time.sleep(1.5)

    print(Fore.CYAN + "="*60 + "\n")

    blinking("VOCÊ FOI HACKERADO! 💀", times=10, delay=0.25, color=Fore.RED + Style.BRIGHT)

    print(Fore.CYAN + "\n[ INICIANDO ABERTURA DE LINK SECRETO ]\n")

    progress_bar(duration=4, length=40)

    # Aqui vc coloca o LINK que quiser abrir
    LINK = "https://seulinkaqui.com"  # <<< COLOQUE SEU LINK AQUI <<<

    type_effect(f"Abrindo link secreto: {LINK}", delay=0.03, color=Fore.LIGHTGREEN_EX)
    time.sleep(1)

    webbrowser.open(LINK)

    type_effect("\nSequência finalizada. Até a próxima ;)", delay=0.04, color=Fore.MAGENTA + Style.BRIGHT)

if __name__ == "__main__":
    main()
