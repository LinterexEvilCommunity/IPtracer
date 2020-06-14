# IPtracer

A tool to retrieve IP IPtracer information
Powered by ip-api
Requirements
Python 3.x
termcolor
colorama
Download/Installation
git clone https://github.com/LinterexEvilCommunity/IPtracer
pip3 install -r requirements.txt --user
if pip3 is missing:

apt-get install python3-setuptools
easy_install3 pip
pip3 install -r requirements.txt
Features
Retrieve IP or Domain IPtracer.
Retrieve your own IP IPtracer.
Retrieve IPtracer for IPs or Domains loaded from file. Each target in new line.
Define your own custom User Agent string.
Select random User-Agent strings from file. Each User Agent string in new line.
Proxy support.
Select random proxy from file. Each proxy URL in new line.
Open IPtracer in Google Maps using the default browser.
Export results to csv, xml and txt format.
IPtracer Information
ASN
City
Country
Country Code
ISP
Latitude
Longtitude
Organization
Region Code
Region Name
Timezone
Zip Code
Usage
$ ./ip2IPtracer.py
usage: IPtracer.py [-h] [-m] [-t TARGET] [-T file] [-u User-Agent]
                        [-U file] [-g] [--noprint] [-v] [--nolog] [-x PROXY]
                        [-X file] [-e file] [-ec file] [-ex file]

IPtracer 2.0.4

--[ Retrieve IPtracer information from ip-api.com
--[ By LinterexEvil Community
--[ ip-api.com service will automatically ban any IP addresses doing over 150 requests per minute.

optional arguments:
  -h, --help            show this help message and exit
  -m, --my-ip           Get IPtracer info for my IP address.
  -t TARGET, --target TARGET
                        IP Address or Domain to be analyzed.
  -T file, --tlist file
                        A list of IPs/Domains targets, each target in new line.
  -u User-Agent, --user-agent User-Agent
                        Set the User-Agent request header (default: IPtracer 2.0.3).
  -U file, --ulist file
                        A list of User-Agent strings, each string in new line.
  -g                    Open IP location in Google maps with default browser.
  --noprint             IPGeolocation will print IPtracer info to terminal. It is possible to tell IPtracer n
ot to print results to terminal with this option.
  -v, --verbose         Enable verbose output.
  --nolog               IPGeolocation will save a .log file. It is possible to tell IPGeolocation not to save those log
files with this option.
  -x PROXY, --proxy PROXY
                        Setup proxy server (example: http://127.0.0.1:8080)
  -X file, --xlist file
                        A list of proxies, each proxy url in new line.
  -e file, --txt file   Export results.
  -ec file, --csv file  Export results in CSV format.
  -ex file, --xml file  Export results in XML format.
