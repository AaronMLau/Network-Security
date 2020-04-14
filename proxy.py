'''
Aaron Lau
CS 494: Network Security
University of Illinois at Chicago

Malicious Proxy

https://piazza.com/class_profile/get_resource/k5e9lfd8gzp1eo/k8gw74g7joo7hh
python proxy.py [-m [active/passive] listening ip listening port
• -m: The mode you want your proxy to operate, which will either be active or passive.
• listening ip: The IP address your proxy will listen on connections on.
• listening port: The port your proxy will listen for connections on.
'''
import sys
import re


def main():
    mode,ip,port = None,None,None
    if len(sys.argv) == 5:
        mode = sys.argv[3]
        ip = sys.argv[4]
        port = sys.argv[5]
    else:
        exit



if __name__ == '__main__':
    main()