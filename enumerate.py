#Author: Pari Malam

import requests
import os
import re
import sys
import colorama
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup

def banners():
    print(f"""{Style.BRIGHT + Fore.RED}
    ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
    ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
    ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
    ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                                
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
    {Style.BRIGHT + Fore.YELLOW}  
                                                    Coded By Pari Malam\n
                                [+] Wordpress Version, Plugins & Themes Enumeration [+]
                                                   
                                               Forum: https://dragonforce.io
                                        Telegram: https://telegram.me/DragonForceIO
                                        
                                    Get Started With (pip install -r requirements.txt)
                                            Usage: python enumerate.py list.txt\n
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
    """)
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

output_file = open('output.txt', 'w')
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
