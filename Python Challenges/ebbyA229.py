import random

def gen_ip4():
    if choice == 0:
        address = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    return address

def gen_ip6():
    if choice == 0:
        address = ":".join(map(str, (random.randint(0, 255) for i in range(6))))
    return address

choice = int(input("IPv4(0) or IPv6(1)? "))
num = int(input("How many addresses? "))

type = {0:gen_ip4,1:gen_ip6}
addresses = []
while len(addresses) < num:
    address = type[choice]()
    if address not in addresses: addresses.append(address)

print(addresses)
