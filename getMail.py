import imaplib
import email

imap_server = 'imap-mail.outlook.com	'
email_address = 
password = 

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password); 