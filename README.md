Use this script to send ASCII art out as DNS queries or HTTP GETs.  Each line of the supplied ASCII art text file will be sent out as a packet, which results in the whole ASCII art content being visible when viewing the packets in Wireshark/tcpdump/etc.  Here is an example of the output being viewed through tcpdump:

23:49:18.815374 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A?                       /^--^\     /^--^\     /^--^\             . (81)
23:49:18.876086 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A?                       \____/     \____/     \____/             . (81)
23:49:18.942638 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A?                      /      \   /      \   /      \            . (81)
23:49:18.994269 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A?                     |        | |        | |        |           . (81)
23:49:19.073964 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A?                      \__  __/   \__  __/   \__  __/            . (81)
23:49:19.126097 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A? |^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|. (81)
23:49:19.181415 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A? | | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | |. (81)
23:49:19.256649 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A? ########################/ /######\ \###########/ /#############. (81)
23:49:19.309872 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A? | | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | |. (81)
23:49:19.368287 IP 1.1.1.1.domain > 2.2.2.2.domain: 0+ A? |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|. (81)



