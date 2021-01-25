#!/usr/bin/env python
import scapy.all as scapy
import optparse

def get_ip():
    parser = optparse.OptionParser()
    parser.add_option("-s","--IP","--ip",dest="IP_Add",help="Put the IP Address")
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #Here
    # we have used "[0]" because we only want to print the answered list,
    # as we know that there are two lists which are returned from "SRP", so
    # we are going to print answered list as list indexing begins from 0
    # hence printing the answered list. USING FOR LOOP

    client_list = []
    for elements in answered_list:
        client_dict = {"ip":elements[1].psrc, "mac": elements[1].hwsrc}
        client_list.append(client_dict)
        # Note we have elements[1] because we want the second part of the
        # list, i.e. second sub list of the main list.
    return client_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n--------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


print_result(scan("192.168.29.1/24"))