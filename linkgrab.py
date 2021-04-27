#!/usr/bin/env python
# -*- coding: utf8 -*-

"""


        =^.~= linkgrab =~.^= 

		a simple scripts which dumps all links
		from a given website. little example 
        for basic functionality of beautifulsoup.
		
        Version: 0.1
            + initial version
		
		Written by Peter Bartels
        
        https://www.kangafoo.de
		
"""

import sys
import argparse
import os
import requests
from bs4 import BeautifulSoup


def clear():
    """
    
    clear() -> no return
    
    just clear screen for linux and windows
    
    """
    os.system("cls" if os.name == "nt" else "clear")	


def infoheader():
    """
    
    infoheader() -> no return
    
    prints header logo and avatar target name and CID
    
    """
    clear()
    print("=^.~= linkgrab =~.^=")
    print("-"*50)
    print("->>  Target: %s" %(target))
    print("-"*50)


def printhelp():
    """
    
    printhelp() -> no return
    
    prints header logo and displays help parameters
    
    """
    clear();
    print("=^.~= linkgrab =~.^=")
    parser.print_help()



def get_links(wwwlink):
    """
    
    get_links(string) -> list
    
    takes a link and retrieves all links within
    
    """
    lst = list()
    html = requests.get(wwwlink)
    soup = BeautifulSoup(html.text, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lst.append(tag.get('href', None))
    return lst
    


if __name__=="__main__":
    parser = argparse.ArgumentParser("%prog [options] arg1 arg2")
    parser.add_argument("-t", "--target", dest="target",default="",help="specify the website to scan e.g. https://www.google.de")
    options = parser.parse_args()
    if len(sys.argv) < 2:
        printhelp()
        quit()
    else:
        target = options.target
        infoheader()
        for line in get_links(target):
            print(" - "+line)
        