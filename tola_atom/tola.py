#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass

target_url = input("Enter a website URL link: ")
with open("wordlist1","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered URL ==> ",test_url)
            with open("wordlist2", "r") as wordlist_file2:
                for line1 in wordlist_file2:
                    word2 = line1.strip()
                    new_test_url = test_url + "/" + word
                    response = request(test_url)
                    if response:
                        print("[+] Discovered URL ==> ", new_test_url)

with open("wordlist2","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL ==> ",test_url)
