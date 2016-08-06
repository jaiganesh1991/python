#!/usr/bin
#This is program for map location
import webbrowser, sys
url = "https://www.google.com/maps/place/"
if len(sys.argv) > 1:


    address = "".join(sys.argv[1:])
    webbrowser.open(url+address)
    print url+address
