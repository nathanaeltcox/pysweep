#!/usr/bin/env python
import subprocess
import time
import sys

def main():
    start = time.time()
    ip_get = input("Please enter IP network address to scan (xxx.xxx.xxx.): ")
    dots = 0
    for char in ip_get: #For loop makes it so that it works whether user inputs IP as "x.x.x." or forgets the last period and puts "x.x.x"
        if char == ".":
            dots += 1
        if dots == 3:
            ip_target = ip_get
        else:
            ip_target = ip_get + "."
    ip_result = [] #Stores the active IP addresses that are returned.
    ip_response = [] #Stores the time for each ping.
    ip_list = [] #Stores the active IP addresses as a list to be printed.
    for ip in range(0,256):
        output = b""
        ip_call = ip_target + str(ip)
        argument = "fping -a -C 5 -q " + ip_call
        try:
            output = subprocess.check_output(argument, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as error:
            e = error.output  #Thanks to Matt Gluck for figuring out this part of the code.
        except KeyboardInterrupt:
            print("\n""User interrupted scan.")
            sys.exit()
        output = output.decode("utf-8")
        output = output.split(" ",2)
        ip_result = output[0]
        if ip_result == "":
            ip_response = ""
        else:
            ip_response = output[2]
            print("{} is detected online. Response time(s) were: {}".format(ip_result, ip_response))
            ip_list.append(ip_result)
    seconds = time.time() - start
    milliseconds = seconds * 1000 #Convert to milliseconds.
    print("The following hosts were found to be online and responding to ping requests:")
    print("\n""Detected Hosts:")
    print("==============")
    print("\n".join(ip_list))
    print("\n""Total time to scan took: {} ms".format(milliseconds))
    
if __name__ == "__main__":
    main()