import imaplib  
obj = imaplib.IMAP4_SSL('imap.gmail.com', '993') 
obj.login('xxxxx@gmail.com','xxxxxxx')  
obj.select() 
unreadcount=len(obj.search(None,'UnSeen')[1][0].split())
print(unreadcount)

