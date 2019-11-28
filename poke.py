import urllib.request
int i =0;
print i;
for i in range(10,90) :
    s=str(i)
    url = "http://www.serebii.net/xy/pokemon/0"+s+".png"
    urllib.request.urlretrieve (url,s+".png")
