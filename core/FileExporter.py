#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of IPtracer tool.
    https://github.com/LinterexEvilCommunity/IPtracer
    
    IPtracer - Retrieve IP Geolocation information 
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

__author__ = 'LinterexEvil Community'

import csv
from xml.etree import ElementTree as etree
from collections import OrderedDict

class FileExporter:
    
    def __init__(self):
        pass
    
    def ExportListToCSV(self, IPtracerObjs, filename):
        return self.__ExportToCSV(IPtracerObjs, filename)
        
    def ExportToCSV(self, IPtracerObj, filename):
        return self.__ExportToCSV([IPtracerObj], filename)
    
    def ExportListToXML(self, IPtracerObjs, filename):
        return self.__ExportToXML(IPtracerObjs, filename)
    
    def ExportToXML(self, IPtracerObj, filename):
        return self.__ExportToXML([IPtracerObj], filename)

    def ExportListToTXT(self, IPtracerObjs, filename):
        return self.__ExportToTXT(IPtracerObjs, filename)
        
    def ExportToTXT(self, IPtracerObj, filename):
        return self.__ExportToTXT([IPtracerObj], filename)
    
    def __ExportToTXT(self, IPtracerObjs, filename):
        try:
            with open(filename, 'w') as txtfile:
                txtfile.write('Results IPtracer\n')
                for IPtracerObj in IPtracerObjs:
                    if IPtracerObj:
                        txtfile.write('Target: {}\n'.format(IPtracerObj.Query))
                        txtfile.write('IP: {}\n'.format(IPtracerObj.IP))
                        txtfile.write('ASN: {}\n'.format(IPtracerObj.ASN))
                        txtfile.write('City: {}\n'.format(IPtracerObj.City))
                        txtfile.write('Country: {}\n'.format(IPtracerObj.Country))
                        txtfile.write('Country Code: {}\n'.format(IPtracerObj.CountryCode))
                        txtfile.write('ISP: {}\n'.format(IPtracerObj.ISP))
                        txtfile.write('Latitude: {}\n'.format(IPtracerObj.Latitude))
                        txtfile.write('Longtitude: {}\n'.format(IPtracerObj.Longtitude))
                        txtfile.write('Organization: {}\n'.format(IPtracerObj.Organization))
                        txtfile.write('Region: {}\n'.format(IPtracerObj.Region))
                        txtfile.write('Region Name: {}\n'.format(IPtracerObj.RegionName))
                        txtfile.write('Timezone: {}\n'.format(IPtracerObj.Timezone))
                        txtfile.write('Zip: {}\n'.format(IPtracerObj.Zip))
                        txtfile.write('Google Maps: {}\n'.format(IPtracerObj.GoogleMapsLink))
                        txtfile.write('\n')
            return True
        except:
            return False
        
        
    def __ExportToXML(self, IPtracerObjs, filename):
        try:
            root = etree.Element('Results')
            
            for IPtracerObj in IPtracerObjs:
                if IPtracerObj:
                    orderedData = OrderedDict(sorted(IPtracerObj.ToDict().items()))
                    self.__add_items(etree.SubElement(root, 'IPtracer'),
                      ((key.replace(' ', ''), value) for key, value in orderedData.items()))
        
                    tree = etree.ElementTree(root)

            tree.write(filename, xml_declaration=True, encoding='utf-8')
                        
            return True
        except:
            return False
        
        
    def __ExportToCSV(self, IPtracerObjs, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Results', 'IPtracer'])
                for IPtracerObj in IPtracerObjs:
                    if IPtracerObj:
                        writer.writerow(['Target', IPtracerObj.Query])
                        writer.writerow(['IP', IPtracerObj.IP])
                        writer.writerow(['ASN', IPtracerObj.ASN])
                        writer.writerow(['City', IPtracerObj.City])
                        writer.writerow(['Country', IPtracerObj.Country])
                        writer.writerow(['Country Code', IPtracerObj.CountryCode])
                        writer.writerow(['ISP', IPtracerObj.ISP])
                        writer.writerow(['Latitude', IPtracerObj.Latitude])
                        writer.writerow(['Longtitude', IPtracerObj.Longtitude])
                        writer.writerow(['Organization', IPtracerObj.Organization])
                        writer.writerow(['Region', IPtracerObj.Region])
                        writer.writerow(['Region Name', IPtracerObj.RegionName])
                        writer.writerow(['Timezone', IPtracerObj.Timezone])
                        writer.writerow(['Zip', IPtracerObj.Zip])
                        writer.writerow(['Google Maps', IPtracerObj.GoogleMapsLink])
                        writer.writerow([])
            return True
        except:
            return False
        
    
    def __add_items(self, root, items):
        for name, text in items:
            elem = etree.SubElement(root, name)
            elem.text = text

