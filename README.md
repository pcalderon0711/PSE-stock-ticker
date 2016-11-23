## PSE stock ticker

This is a command line app to monitor your stocks in the Philippine stock exchange. I wrote this because I am too lazy to even press the refresh button.

Data source : www.pesobility.com/stock

Dependencies : (Python 3) sys, re, os, datetime, requests, bs4

Usage : 

Command line arguments are the symbol names of the stocks in your portfolio. Ex: I own TEL, ALI, AGI, 2GO. Then I run the code in the Terminal as:

python clticker.py TEL ALI AGI 2GO