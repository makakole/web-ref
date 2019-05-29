import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

msg = MIMEText('I  believe that this week is the last week for most of you. May you please make sure that you have signed the attendance register for April and May, as this is one of the requirements to obtain your qualification')

me = 'owen.mafane@umuzi.org'
you = 'makakole74@gmail.com'
msg['Subject'] = 'The contents of textfile'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()