import sys
import re

shorthands = { "A" : "Ala", "R" : "Arg", "N" : "Asn", "D" : "Asp", "C" : "Cys", "Q" : "Gln", "E" : "Glu", "G" : "Gly", "H" : "His", "I" : "Ile", "L" : "Leu", "K" : "Lys", "M" : "Met", "F" : "Phe", "P" : "Pro", "S" : "Ser", "T" : "Thr", "W" : "Trp", "Y" : "Tyr", "V" : "Val" }

polar       = ["W", "Y", "S", "C", "M", "D", "Q", "T", "H", "K", "R"]
nonpolar    = ["A", "G", "V", "L", "I", "F", "P"]

hydrophilic = ["D", "E", "H", "K", "Q", "R", "S", "T"]
hydrophobic = ["A", "I", "L", "F", "M", "P", "V", "W", "Y"]

positive    = ["R", "H", "K"]
negative    = ["D", "E"]

def is_polar(n):
    if n in polar:
        return 'polar'
    elif n in nonpolar:
        return 'nonpolar'
    else:
        return 'X'

def is_hydrophilic(n):
    if n in hydrophilic:
        return 'hydrophilic'
    elif n in hydrophobic:
        return 'hydrophobic'
    else:
        return 'X'

def is_positive(n):
    if n in positive:
        return 'positive'
    elif n in negative:
        return 'negative'
    else:
        return 'X'


for line in open(sys.argv[1]):
    arr = re.split('\s+', line.strip())
    a = arr[1]
    b = arr[3]
    print is_polar(a) + '-' + is_polar(b) + ', ' + is_hydrophilic(a) + '-' + is_hydrophilic(a) + ', ' + is_positive(a) + '-' + is_positive(b)
