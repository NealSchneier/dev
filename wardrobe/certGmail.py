import oauth2 as oauth
import oauth2.clients.imap as imaplib
import imaplib
from email.parser import HeaderParser
import temp as oauth2

# Set up your Consumer and Token as per usual. Just like any other
# three-legged OAuth request.


client_id="977739430087-iul45rh0o6qjp6bq3sdhhrjuth5f61rv.apps.googleusercontent.com"
client_secret="7TI2GD3ANT537Yyi_yF0fwM-"
print 'To authorize token, visit this url and follow the directions:'
print ' %s' % oauth2.GeneratePermissionUrl(client_id)
authorization_code = raw_input('Enter verification code: ')
response = oauth2.AuthorizeTokens(client_id,client_secret,authorization_code)

print "Refresh Toke :",response['refresh_token']
print "Access Token :",response['access_token']
print "Expires in :",response['expires_in']
oauth2string = oauth2.GenerateOAuth2String('neal.schneier@gmail.com', response['access_token'], base64_encode=False)
#consumer = oauth.Consumer('977739430087-iul45rh0o6qjp6bq3sdhhrjuth5f61rv.apps.googleusercontent.com', '7TI2GD3ANT537Yyi_yF0fwM-')
#token = oauth.Token('your_users_3_legged_token', 
#    'your_users_3_legged_token_secret')

 
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.authenticate('XOAUTH2', lambda x: oauth2string)
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