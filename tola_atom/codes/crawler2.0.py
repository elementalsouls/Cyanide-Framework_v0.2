#!/usr/bin/env python

import requests
import re
import urllib.parse as urlparse
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
try:
    unknown = input(Fore.WHITE + "\n  Enter the Website (target url): ")
    target_url = "https://" + unknown
    target_links = []

    def extract_links_from(url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))

    def crawl(url):
        href_links = extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if target_url in link and link not in target_links:
                target_links.append(link)
                print (link)
                crawl(link)

    crawl(target_url)

except KeyboardInterrupt:
    print(Fore.WHITE + Back.RED +"\n\n\tKeyboardInterruption Detected")
    print(Fore.WHITE + Back.RED +"\n\n\t\tExiting")
    exit()
