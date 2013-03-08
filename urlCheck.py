
import urllib2, time, string, smtplib

url = 'http://www.domain.com'                             #The website you want to check
mail = 'youremail@gmail.com'                              #The gmail account you want the mail to be delivered
password = 'yourpassword'                           #Your gmail password so you can send mail to yourself
wait = 300;                                                 #The waiting time between tries. It has to be bigger than 100 sec

def urlOpen(url):   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        print 'Website is down...'
        return False
    else:
        print 'Website is Up!'
        return True

        

def sendMail(): 
    SUBJECT = url + " is up!"
    TO = mail
    FROM = mail
    text = "The website " + url + " is up and running"
    BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mail, password)
    server.sendmail(FROM, [TO], BODY)
    server.quit()
        
if wait>100:        
	i=1
	while True:
		print "Waiting " + str(wait) + " seconds to attempt website availability check number " + str(i) + ".\n"
		i+=1
		time.sleep(wait)
		if urlOpen(url):
			sendMail()
			break
else:
    print "We don't want to spam the website do we? Enter a bigger waiting time between tries."