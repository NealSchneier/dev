import imaplib
from email.parser import HeaderParser

class Gmail:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.m = imaplib.IMAP4_SSL('imap.gmail.com')
        self.m.login(username, password)
        self.m.select()

    def getGooglePlay(self):
        typ, data = self.m.search(None, '(FROM "googleplay-noreply@google.com")')
        for num in data[0].split():
            typ, data = self.m.fetch(num, '(RFC822)')
            #print 'Message %s\n%s\n' % (num, data[0][1])
            msg = HeaderParser().parsestr(data[0][1])
            
            print msg['From']
            print msg['To']
            print msg['Subject']
            print msg.get_payload()
  	
  	def close(self):
  		self.m.close()
		self.m.logout()
