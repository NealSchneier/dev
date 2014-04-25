import imaplib
from email.parser import HeaderParser
from HTMLParser import HTMLParser
from django.http import HttpResponse
from HTMLtoJSONParser import HTMLtoJSONParser
from htmlentitydefs import name2codepoint
from MyHTMLParser import MyHTMLParser
from bs4 import BeautifulSoup
import webbrowser
import urllib2 as urllib
import cStringIO
import PIL

class Gmail:
	
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.m = imaplib.IMAP4_SSL('imap.gmail.com')
        self.m.login(username, password)
        self.m.select()

    def getGooglePlay(self):
        typ, data = self.m.search(None, '(FROM "googleplay-noreply@google.com")')
        messages = []
        for num in data[0].split():
            typ, data = self.m.fetch(num, '(RFC822)')
            msg = HeaderParser().parsestr(data[0][1])
            payload = msg.get_payload()
            payload = self.parsePayload(payload)
            
            messages.append({"from":msg['From'], "to":msg['To'], "subject":msg['Subject'], "payload":payload})
            soup = BeautifulSoup(payload)
            #print(soup.prettify())
            #for link in soup.find_all('a'):
            #    print(link.get('href'))

            #for link in soup.find_all('img'):
                #webbrowser.open(link.get('src'))

            for meta in soup.find_all('meta'):
                if meta.get('itemprop') == 'orderNumber':
                    print meta.get('content')
                elif meta.get('itemprop') == 'price':
                    print meta.get('content')
                elif meta.get('itemprop') == 'image':
                    file = open(num, 'w+')
                    #file.write(meta.get('content'))
                    file = cStringIO.StringIO(urllib.urlopen(meta.get('content')).read())
                    img = Image.open(file)
                

        return messages    

    def getSquare(self):
        typ, data = self.m.search(None, '(FROM "noreply@messaging.squareup.com")')
        messages = []
        for num in data[0].split():
            typ, data = self.m.fetch(num, '(RFC822)')
            #print 'Message %s\n%s\n' % (num, data[0][1])
            msg = HeaderParser().parsestr(data[0][1])
            payload = msg.get_payload()
            payload = self.parsePayload(payload)
            messages.append({"from":msg['From'], "to":msg['To'], "subject":msg['Subject'], "payload":payload})

            # print msg['From']
            # print msg['To']
            # print msg['Subject']
            # print msg.get_payload()
        return messages    

    def getAmazon(self):
        typ, data = self.m.search(None, '(FROM "auto-confirm@amazon.com")')
        messages = []
        for num in data[0].split():
            typ, data = self.m.fetch(num, '(RFC822)')
            #print 'Message %s\n%s\n' % (num, data[0][1])
            msg = HeaderParser().parsestr(data[0][1])
            payload = msg.get_payload()
            payload = self.parsePayload(payload)
            messages.append({"from":msg['From'], "to":msg['To'], "subject":msg['Subject'], "payload":payload})

            
        return messages    
    def parsePayload(self, payload):
        start = payload.partition("<html>")
        end = start[2].partition("</html>")
        string = start[1] + end[0] + end[1]
        # string = string.replace("= ","")
        string = string.replace("=\r\n","")
        string = string.replace('3D"', '"')
        string = string.replace('=3D', '=')
        return string

  	def closeGmail(self):
  		self.m.close()
		self.m.logout()


    