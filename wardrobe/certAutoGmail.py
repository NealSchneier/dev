import oauth2 as oauth
import oauth2.clients.imap as imaplib
from email.parser import HeaderParser
import temp as oauth2

# Set up your Consumer and Token as per usual. Just like any other
# three-legged OAuth request.

email = 'neal.schneier@gmail.com'
client_id="977739430087-iul45rh0o6qjp6bq3sdhhrjuth5f61rv.apps.googleusercontent.com"
client_secret="7TI2GD3ANT537Yyi_yF0fwM-"
token = oauth.Token(client_id, client_secret)
consumer = oauth.Consumer('anonymous', 'anonymous')
url = "https://mail.google.com/mail/b/" + email +"/imap/"

 
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.authenticate(url, consumer, token)
#M.authenticate('XOAUTH2', lambda x: oauth2string)
#M.login('neal.schneier@gmail.com', 'Yankswin272009')
M.select()
typ, data = M.search(None, '(FROM "googleplay-noreply@google.com")')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    #print 'Message %s\n%s\n' % (num, data[0][1])
    msg = HeaderParser().parsestr(data[0][1])
    
    print msg['From']
    print msg['To']
    print msg['Subject']
    print msg.get_payload()
    
M.close()
M.logout()