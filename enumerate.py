# Author: Pari Malam

import requests
import os
import re
import sys
from sys import stdout
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Linux':
    os.system('clear')
    
def banners():
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI PARI-MALAM                               "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://GITHUB.COM/PARI-MALAM                 "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://DRAGONFORCE.IO                        "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   HTTPS://TELEGRAM.ME/DRAGONFORCEIO             "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[HackerTarget] - {Fore.GREEN}Perform With DNS Emuration & Reverse Lookup\n")
banners()
    
def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

def URLdomain(site):
    if site.startswith("http://"):
        site = site.replace("http://","")
    elif site.startswith("https://"):
        site = site.replace("https://","")
    else:
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def Version(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    version = soup.find("meta", {"name": "generator"})["content"].split()[1]

    plugins = []
    for link in soup.find_all("link", {"rel": "stylesheet"}):
        href = link.get("href")
        if "plugins" in href:
            plugins.append(href.split("plugins/")[1].split("/")[0])

    theme_link = soup.find("link", {"rel": "stylesheet"})
    theme = None
    if theme_link:
        href = theme_link.get("href")
        theme_parts = href.split("themes/")
        if len(theme_parts) > 1:
            theme = theme_parts[1].split("/")[0]

    return version, plugins, theme

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <list.txt>')

output_file = open('Results/Results.txt', 'w')
for site in target:
    url = 'https://' + URLdomain(site)
    try:
        version, plugins, theme = Version(url)
        output = "URLs: {}\nWordPress Version: {}\nInstalled Plugins: {}\nActived Themes: {}\n{}\n".format(url, version, ", ".join(plugins), theme, '-' * 100)
        output_file.write(output)
        print(Style.BRIGHT + Fore.GREEN + output)
        open('output.txt', 'a').write("URLs: " + url + "\nWordPress Version: " + version + "\nInstalled Plugins: " + ", ".join(plugins) + "\nActived Themes: " + theme + "\n" + '-' * 100 + "\n")
    except:
        print(Style.BRIGHT + Fore.RED+"[!] Error occurred while scanning", url)
        print("-" * 50)
output_file.close()
