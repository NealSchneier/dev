import imaplib
from email.parser import HeaderParser
 
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login('neal.schneier@gmail.com', 'Yankswin272009')
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
