#!/usr/bin/env python
import subprocess
import time

def main():
    start = time.time()
    ip_target = "10.0.2."
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
        output = output.decode("utf-8")
        output = output.split(" ",2)
        ip_result = output[0]
        if ip_result == "":
            ip_response = ""
        elif ip_result != "":
            ip_response = output[2]
            print(ip_result + " is detected online. Response time(s) were: " + ip_response)
            ip_list.append(ip_result)
    seconds = time.time() - start
    milliseconds = seconds * 1000 #Convert to milliseconds.
    print("The following hosts were found to be online and responding to ping requests:")
    print("\n""Detected Hosts:")
    print("==============")
    print("\n".join(ip_list))
    print("\n""Total time to scan took: " + str(milliseconds) + "ms")
    
if __name__ == "__main__":
    main()