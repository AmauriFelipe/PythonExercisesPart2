import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('\033[1;31;mO site pudim.com.br não está acessível no momento.\033[m')

else:
    print('\033[1;32;mO site pudim.com.br está acessível no momento.\033[m')
    print(site.read)
