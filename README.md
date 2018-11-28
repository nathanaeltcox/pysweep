# pysweep
Python ping sweep command line utility.

Asks for a Class C network IP address to scan, and pings all possible 256 addresses using fping function. Sends
5 requests to each host and records latency times. Only returns alive hosts. Once finished, prints list of all
hosts found and total time for scan.

To install: Place a copy in the directory where you keep your scripts.

To run: Run in command line using command "python pysweep.py". You will be prompted to input the first three octets
of the network address you wish to scan. To stop the scan before it is finished, press ctrl + c.
