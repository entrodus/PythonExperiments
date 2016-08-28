import urllib.request
with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read();

print(s);