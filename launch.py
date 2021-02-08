open("date.js","w").close()

f=open("date.js","a")
f.write("var jtt=new Date('")
f.close()

from urllib.request import urlopen
res=urlopen("http://just-the-time.appspot.com/")

result=res.read().strip()
result

result_str=result.decode("utf-8")
result_str

f=open("date.js","a")
f.write(result_str)
f.close()

f=open("date.js","a")
f.write("');")
f.close()

f=open("date.js","r")
print(f.read())

import webbrowser
url='C:/bot/clock2.html'
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)