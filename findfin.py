#!/usr/bin/env python
"""
 Used with
 Find the part and used with part
 Takes one filename as argument

    python usedwith.py data.xml

 @author    Ye Chuah
 @copyright invenn.com.au
 @created   24/03/2012
 @license   GPL

"""

import re
import sys

def main():
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        filename = 'data.xml'

    try:
        f = open(filename, 'r')
        data = f.read()
        f.close()
        print "Using %s" % filename
    except Exception:
        print "Couldn't open %s" % filename
        sys.exit(0)

    matches = re.findall('<ITEM.+?EIN.+?</ITEM', data, re.S)

    """ Folowing pattern extracts part number and used with part number with submatches"""
    partpattern = re.compile('PNR [^>]+>(.+?)</PNR', re.S)
    finpattern = re.compile('EIN [^>]+>(.+?)</EIN', re.S)

    print "Part Number\tFIN Number"

    for match in matches:

        """ Need to find where to start submatch from because gross match will
        erroneously return first PNR used with UWP. Use last item found """
        for m in re.finditer('<ITEM', match, re.S):
            start =  m.start()

        part =  partpattern.search(match[start:]).group(1).strip()

        for m in re.finditer('<EIN', match, re.S):
            start = m.start()
            fin = finpattern.search(match[start:]).group(1).strip()
            print "%s\t%s" % (part, fin)

if __name__ == "__main__":
    main()