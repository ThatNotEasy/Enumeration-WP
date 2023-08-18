# Author: Pari Malam

import os
import random
import requests
from bs4 import BeautifulSoup
import warnings
import concurrent.futures
from sys import stdout
from colorama import Fore, Style, init
warnings.filterwarnings("ignore")
init(autoreset=True)

FY = Fore.YELLOW
FG = Fore.GREEN
FR = Fore.RED
FC = Fore.CYAN
FW = Fore.WHITE

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def dirdar():
    if not os.path.exists('Results'):
        os.mkdir('Results')
dirdar()

def banners():
    clear()
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╗    ██╗██████╗       ███████╗███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║    ██║██╔══██╗      ██╔════╝████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║ █╗ ██║██████╔╝█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║███╗██║██╔═══╝ ╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚███╔███╔╝██║           ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║\n")
    stdout.write(""+Fore.LIGHTRED_EX +" ╚══╝╚══╝ ╚═╝           ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦══════════════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n")
    print(f"{FY}[Wordpress-Enumeration] - {FG}Perform With Massive Wordpress Enumeration {FR}[Plugin/Theme]{Style.RESET_ALL}\n")
banners()

def load_user_agents():
    with open("lib/ua.txt", "r") as ua_file:
        user_agents = ua_file.readlines()
    user_agents = [ua.strip() for ua in user_agents if ua.strip()]
    return user_agents

def add_http_prefix(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url

def get_wordpress_info(url):
    target = add_http_prefix(url)
    headers = {'user-agent': random.choice(load_user_agents())}

    try:
        response = requests.get(target, headers=headers, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")

        version_meta = soup.find("meta", {"name": "generator"})
        version = None
        if version_meta and "content" in version_meta.attrs:
            content = version_meta["content"].split()
            if len(content) > 1:
                version = content[1]

        plugins = []
        for link in soup.find_all("link", {"rel": "stylesheet"}):
            href = link.get("href")
            if href and "plugins" in href:
                plugins.append(href.split("plugins/")[1].split("/")[0])

        theme_link = soup.find("link", {"rel": "stylesheet"})
        theme = None
        if theme_link and "href" in theme_link.attrs:
            href = theme_link["href"]
            theme_parts = href.split("themes/")
            if len(theme_parts) > 1:
                theme = theme_parts[1].split("/")[0]

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

    return version, plugins, theme

def scan_site(url):
    version, plugins, theme = get_wordpress_info(url)

    if version:
        output = (
            f".++==========[Pari Malam]==========++.\n"
            f"URL: {url}\n"
            f"WordPress Version: {version}\n"
            f"Installed Plugins: {', '.join(plugins)}\n"
            f"Active Theme: {theme}\n"
            f".++==========[Pari Malam]==========++.\n\n"
        )
        print(Fore.YELLOW + "[WORDPRESS-ENUM]" + Fore.RED + " .:" + Fore.GREEN + f" [W00T!] - {Fore.WHITE}{url}\n")
        print(Fore.YELLOW + "[WORDPRESS-ENUM]" + Fore.RED + " .:" + Fore.GREEN + f" WordPress Version: {Fore.WHITE}{version}")
        print(Fore.YELLOW + "[WORDPRESS-ENUM]" + Fore.RED + " .:" + Fore.GREEN + f" Installed Plugins: {Fore.WHITE}{', '.join(plugins)}")
        print(Fore.YELLOW + "[WORDPRESS-ENUM]" + Fore.RED + " .:" + Fore.GREEN + f" Active Theme: {Fore.WHITE}{theme}")
        with open('Results/Results.txt', 'a') as results_file:
            results_file.write(output)
    else:
        print(Fore.YELLOW + "[WORDPRESS-ENUM]" + Fore.GREEN + " .:" + Fore.RED + f" [NOT FOUND!] - {Fore.WHITE}{url}")

if __name__ == '__main__':
    input_file = input(f"{Fore.YELLOW}[URL/IP LIST] {Fore.RED}.: {Fore.WHITE}")
    threads = int(input(f"{Fore.YELLOW}[THREAD: 10-30] {Fore.RED}.: {Fore.WHITE}"))

    try:
        with open(input_file, mode='r') as f:
            target = [i.strip() for i in f.readlines()]
    except FileNotFoundError:
        exit('\n  WHUT ARE YOU DOIN? FILE NOT FOUND! ' + input_file)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_site, site) for site in target]

        for future in concurrent.futures.as_completed(futures):
            future.result()