#################################
#                               #
#     Author: Anoop S           #
#                               #
#################################


from bs4 import BeautifulSoup
import requests


keywords={"http":'http',
          "end":"html",
          "style":'margin-left:10px;margin-right:10px;',
          "Lyricsend":"</div",
          "drive":"L://lyrics//",
          "input":'y'
        }
while(keywords['input'].lower()=='y'):
    song = raw_input("enter song's name\n")

    r = requests.get("http://www.google.com/search?q="+song.replace(' ','+')+'+lyrics')
    asciiText = r.text.encode('ascii','ignore') # converting to ascii
    r.close()
    soup = BeautifulSoup(asciiText)
    slink=''
    elms = soup.select("h3 a")
    
    for each in elms:
        if str(each.attrs["href"]).find('azlyrics')>0:
            slink = str(each.attrs["href"])
            slink = slink[slink.find(keywords['http']):slink.find(keywords["end"])+len(keywords['end'])]

    if slink:
        r = requests.get(slink)
        page = r.text.encode('ascii','ignore') # converting to ascii
        r.close()
        soup = BeautifulSoup(page)
        whole = soup.find("div",{'style':keywords['style']})
        fileName = raw_input("enter the file name to which you wanna save: ")
        
        with open(keywords['drive']+fileName+'.txt','w+') as f:
            f.write(str(whole.text))
        print "your file has been saved to "+keywords['drive']+fileName+'.txt'
        print
    else:
        print "Sorry, couldn't locate on server"

    keywords['input'] = raw_input('do you wanna check any other song y/n: ').lower()
