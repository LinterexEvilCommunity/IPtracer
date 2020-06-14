#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of IPtracer tool.
    https://github.com/LinterexEvilCommunity/IPtracer
    
    IPtracer - Retrieve IPtracer information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = 'LinterexEvil Community(Shellstar)'

from datetime import datetime
import os
from termcolor import colored
from sys import platform as _platform


if _platform == 'win32':
    import colorama
    colorama.init()

def Red(value):
        return colored(value, 'red', attrs=['bold'])
    
def Green(value):
    return colored(value, 'green', attrs=['bold'])
    
          
class Logger:
    
    def __init__(self, nolog=False, verbose=False):
        self.NoLog = nolog
        self.Verbose = verbose
        
        
    def WriteLog(self, messagetype, message):
        filename = '{}.log'.format(datetime.strftime(datetime.now(), "%Y%m%d"))
        path = os.path.join('.', 'logs', filename)
        with open(path, 'a') as logFile:
            logFile.write('[{}] {} - {}\n'.format(messagetype, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"), message))
              
              
    def PrintError(self, message):
        """Print/Log error message"""
        if not self.NoLog:
            self.WriteLog('ERROR', message)
        
        print('[{}] {}'.format(Red('ERROR'), message))
    
    
    def PrintResult(self, title, value):
        """print result to terminal"""
        print('{}: {}'.format(title, Green(value)))
    
    
    def Print(self, message):
        """print/log info message"""
        if not self.NoLog:
            self.WriteLog('INFO', message)
            
        if self.Verbose:
            print('[{}] {}'.format(Green('**'), message))
    
    
    def PrintIPtracer(self, IPtracer):
        """print IPtracer information to terminal"""
        self.PrintResult('\nTarget', IPtracer.Query)
        self.PrintResult('IP', IPtracer.IP)
        self.PrintResult('ASN', IPtracer.ASN)
        self.PrintResult('City', IPtracer.City)
        self.PrintResult('Country', IPtracer.Country)
        self.PrintResult('Country Code', IPtracer.CountryCode)
        self.PrintResult('ISP', IPtracer.ISP)
        self.PrintResult('Latitude', str(IPtracer.Latitude))
        self.PrintResult('Longtitude', str(IPtracer.Longtitude))
        self.PrintResult('Organization', IPtracer.Organization)
        self.PrintResult('Region Code', IPtracer.Region)
        self.PrintResult('Region Name', IPtracer.RegionName)
        self.PrintResult('Timezone', IPtracer.Timezone)
        self.PrintResult('Zip Code', IPtracer.Zip)
        self.PrintResult('Google Maps', IPtracer.GoogleMapsLink)
        print()
        #.encode('cp737', errors='replace').decode('cp737')
    
