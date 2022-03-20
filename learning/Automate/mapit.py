#!/usr/bin/python


import webbrowser, sys

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

webbrowser.open(f"https://www.google.com/maps/place/{address}")