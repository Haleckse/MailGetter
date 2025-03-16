import imaplib
import email
import imap_tools as it
import os
import sqlite3
from email.header import decode_header

EMAIL = "votre email"
PASSWORD = "votre mot de passe d'application" # Mot de passe d'application à activer depuis le compte google 
SERVER = "imap.gmail.com"

print(os.environ)
pw = os.environ.get(['PW'])
print(pw)



connection = sqlite3.connect("email_storage.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE emails")

# Creation de la base de données
create_table = """
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_email TEXT NOT NULL,
    to_email TEXT NOT NULL,
    subject TEXT,
    date_received TEXT NOT NULL,
    body TEXT
); """
cursor.execute(create_table)


mb = it.MailBox(SERVER).login(EMAIL, PASSWORD, "Inbox")
print(mb.folder.get())

for email in mb.fetch(limit=200, reverse=True, mark_seen=True):
    #print("Title : " + email.subject + "\nContent : " + email.text + "\nDate : " + email.date)
    print(email)
    print('\n')
    print(email.text)

    title = email.subject
    content = email.text
    date = email.date

    cursor.execute("""
            INSERT INTO emails (from_email, to_email, subject, date_received, body)
            VALUES (?, ?, ?, ?, ?)
        """, (email.from_, ', '.join(email.to), email.subject, str(email.date), email.text))
        
    connection.commit()
    print("✅ Email enregistré dans la base SQLite !")

    cursor.execute("SELECT subject FROM emails WHERE subject LIKE ?", ('%Call%',))
    result = cursor.fetchall()
    print(result)