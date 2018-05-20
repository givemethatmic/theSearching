#!/usr/bin/env python
# coding = utf-8
import urllib
import re

def cbk(a, b, c):
    per = 100.0*a*b/c
    if per > 100:
        per = 100
    print '%.2f%%' % per

year = input('input the year:\n')
web_address = 'http://www.nanoscience.gatech.edu/publications/papers/' + str(year) + '.php'
address = urllib.urlopen(web_address)
text = address.read()
package = re.findall(r"<a href=\"../../paper/(.*).pdf\">", text)
for a in package:
    tager = 'http://www.nanoscience.gatech.edu/paper/' + a + '.pdf'
    local_ = '/Users/zengfangyuan/Desktop/the_papers/' + a + '.pdf'
    urllib.urlretrieve(tager, local_, cbk)

