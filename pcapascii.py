#!/usr/bin/env python

from pprint import pprint
from optparse import OptionParser
from scapy.all import send, IP, UDP, TCP, DNS, DNSQR, Ether, Dot1Q
import random

parser = OptionParser()
parser.add_option("-s", "--source", type=str, default="1.1.1.1")
parser.add_option("-d", "--destination", type=str, default="2.2.2.2")
parser.add_option("-n", "--num-repeats", type=int, default=1)
parser.add_option("-u", "--use-http", action="store_false")

class WireFaker(object):
    def __init__(self, source, destination, use_http):
        self.source = source
        self.destination = destination
        if use_http:
            self.send = self.send_http
        else:
            self.send = self.send_dns

    def send_dns(self, payload):
        send(
		IP(src=self.source, dst=self.destination) /
                UDP() /
                DNS(rd=1, qd=DNSQR(qname=payload)))

    def send_http(self, payload):
        send(
                IP(src=self.source, dst=self.destination) /
                TCP(sport=random.randrange(1024, 65536), dport=80) /
                "GET {0} HTTP/1.0\r\n\r\n".format(payload))

    def send_file(self, filename):
        lines = open(filename).readlines()
        max_len = max(len(line) for line in lines)
        lines = [l.rstrip() + " " * (max_len - len(l)) for l in lines]
        pprint(lines)
        for line in lines:
            self.send(line)

    def send_item(self, item):
        try:
                self.send_file(item)
        except IOError:
                self.send(item)

if __name__ == "__main__":
    opts, args = parser.parse_args()
    faker = WireFaker(opts.source, opts.destination, opts.use_http)
    for _ in xrange(opts.num_repeats):
        for arg in args:
            faker.send_item(arg)
