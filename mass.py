#!/usr/bin/python3
# A script to ask for domain for the amass tool and check if it is alive

import os

domain = input("Enter domain: ")
port = input("Enter port(s), seperated by comma. (e.g: 80,443) ")
extra_args = input("Enter extra arguements if any (e.g: '-iface eth0'), otherwise leave empty: ")

os.system(f"fping {domain} > /tmp/.amass.tmp 2>&1")

with open("/tmp/.amass.tmp", "r") as f:
	output = f.read().strip()
    
if f"{domain} is alive" in output:
	pass
else:
	print(f"{domain} is not reachable, Exiting.")
	exit(1)


print("  enumerating...")

os.system(f"amass enum -active -iface enp2s0 -norecursive -brute -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -d {domain} -p {port} {extra_args}")
