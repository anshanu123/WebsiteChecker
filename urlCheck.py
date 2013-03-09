
import urllib2, time, string, smtplib, sys, argparse

parser = argparse.ArgumentParser(description='Script to check whether a site is up or down, sends an email if up.')
parser.add_argument('-u','--url', help='The URL that should be checked', required=True)
parser.add_argument('-m','--mail', help='The email address used to receive and send the notify emails', required=True)
parser.add_argument('-p','--password', help='The email password', required=True)
parser.add_argument('-w', '--wait', help ='The wait time between checking availability', required=True)
args = vars(parser.parse_args())

url = str(args['url'])
mail = str(args['mail'])
password = str(args['password'])
wait = abs(int(args['wait']))

def urlOpen(url):   
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError:
        print 'Website is down.'
        return False
    else:
        print 'Website is Up!'
        return True

        

def sendMail(): 
    SUBJECT = url + " is up! Sending notify email now."
    TO = mail
    FROM = mail
    text = "The website " + url + " is up and running! Check it out!"
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
    try:
   	 server.login(mail, password)
    except:
	print "Incorrect login credentials or 2 step verification enabled. Could not log in "
	print "Exiting now..."
	time.sleep(3)
	sys.exit()
    server.sendmail(FROM, [TO], BODY)
    server.quit()
        
if wait>100:        
	i=1
	while True:
		if i == 1:
			print "Checking availability of:  " + url
		if urlOpen(url):
			 sendMail()
		if not urlOpen(url):
			print url + " is still not up and running"
		i += 1
		print "Waiting " + str(wait) + " seconds to attempt website availabality check number " + str(i) + ".\n" 
		time.sleep(wait)
else:
    print "We don't want to spam the website do we? Enter a bigger waiting time (>100) between tries."
