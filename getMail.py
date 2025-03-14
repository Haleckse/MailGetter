import imaplib
import email
import imap_tools as it
from email.header import decode_header

EMAIL = "haleckse@gmail.com"
PASSWORD = "xaov azte glnk zydh"
SERVER = "imap.gmail.com"


# Connexion au serveur IMAP (ex: Gmail)
"""mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)

# Sélectionner la boîte de réception
mail.select("inbox")

# Récupérer les IDs des e-mails
status, messages = mail.search(None, "ALL")

print(mail)

# Décoder et afficher les e-mails
for num in messages[0].split():
    status, msg_data = mail.fetch(num, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    
    print(f"📩 Sujet : {subject}")

mail.close()
mail.logout()"""


mb = it.MailBox(SERVER).login(EMAIL, PASSWORD, "Inbox")
print(mb.folder.get())

for email in mb.fetch(limit=5, reverse=True, mark_seen=True):
    #print("Title : " + email.subject + "\nContent : " + email.text + "\nDate : " + email.date)
    print(email)
    print('\n')
    print(email.text)

    input("Passer au suivant ?")