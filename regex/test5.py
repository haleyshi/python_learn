import re

output = '''Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
br-swift: 126576053933 152926151    0 3617    0     0          0       257 136335890613 155766591    0    0    0     0       0          0
br-prv: 1531328101 21923798    0    0    0     0          0         0        0       0    0    0    0     0       0          0
ovs-system:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
br-fw-admin: 19316023347 254840613    0   19    0     0          0         0 78391343850 250989188    0    0    0     0       0          0
br-int: 66277190  568670    0    0    0     0          0         0        0       0    0    0    0     0       0          0
eth1.13: 123467244043 120445959    0  119    0     0          0       126 132744341723 123244168    0    0    0     0       0          0
eth1.12: 481215410 6310994    0    0    0     0          0        49 558917170 6209923    0    0    0     0       0          0
eth3.13: 3108809890 32480192    0 3498    0     0          0       131 3591548890 32522423    0    0    0     0       0          0
eth3.11: 485253354 6352470    0    0    0     0          0        59 641709046 6216969    0    0    0     0       0          0
  eth0: 7517857586 53223976    0    0    0     0          0  20520388 47174111869 57841807    0    0    0     0       0          0
  eth1: 130531005457 199604660    0    0    0     0          0       175 138076709685 201779103    0    0    0     0       0          0
  eth2: 12316169620 21976082    0    0    0     0          0   9427351 9386310895 14637402    0    0    0     0       0          0
  eth3: 4149357566 39008981    0    0    0     0          0       190 4249101764 38979450    0    0    0     0       0          0
  eth4: 1054475449881 4601558089    0    1   52     0          0   4525875 1269177160761 3972421084    0    0    0     0       0          0
  eth5: 346442945 5053953    0    0    0     0          0   4534585        0       0    0    0    0     0       0          0
br-ex-hapr: 145822857388 56801722    0  252    0     0          0         0 45081166979 49903375    0   10    0     0       0          0
  eth6:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
br-mgmt: 1021445518138 4139759929    0   11    0     0          0         0 1178414664940 3534001778    0    0    0     0       0          0
  eth7:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
    lo: 360083351482 711753302    0    0    0     0          0         0 360083351482 711753302    0    0    0     0       0          0
 br-ex: 17314869257 46233065    0    0    0     0          0         0 53986894099 41047822    0    0    0     0       0          0
virbr0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
hapr-host:    1556      21    0    0    0     0          0         0      634       9    0    0    0     0       0          0
br-mgmt-hapr: 1695337835375 5357947934    0    0    0     0          0         0 1808110165568 5463421964    0    0    0     0       0          0'''


def readIfTxRxStats(ifname):
    ifstats = {}
    ifstats["name"] = ifname

    regex_result = re.search(r'\b%s:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)' %ifname, output)

    if regex_result:
        ifstats["rx_bytes"] = regex_result.group(1)
        ifstats["rx_packets"] = regex_result.group(2)
        ifstats["rx_errors"] = regex_result.group(3)
        ifstats["rx_dropped"] = regex_result.group(4)
        ifstats["tx_bytes"] = regex_result.group(9)
        ifstats["tx_packets"] = regex_result.group(10)
        ifstats["tx_errors"] = regex_result.group(11)
        ifstats["tx_dropped"] = regex_result.group(12)
        ifstats["collisions"] = regex_result.group(14)
    else:
        print "Failed to read rx tx statistic for interface: %s" %ifname

    return ifstats

print readIfTxRxStats("eth0")
print readIfTxRxStats("eth1")
print readIfTxRxStats("1")
print readIfTxRxStats("th3")
print readIfTxRxStats("eth1.12")

