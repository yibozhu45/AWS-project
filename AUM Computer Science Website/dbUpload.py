#!/usr/bin/python3.6
#-*- coding: UTF-8 -*-
# enable debugging

import boto3
import cgitb
import cgi
import os
import shutil  




#********************************************************************************************** CGI
cgitb.enable()

print ("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()   


name = form.getfirst("name", "0") # 0 is optional - if no 
Student_Number = form.getfirst("Student_Number", "0")
email = form.getfirst("email", "0")
fileitem = form['fileToUpload']



if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('files/' + fn, 'wb').write(fileitem.file.read())
    message = 'Your application was uploaded successfully'

else:
    message = 'No file was uploaded'


#################################################################################
errormessage = 'no error'
try:
    file = open("files/"+fn, 'rb')
except IOError:
    errormessage = 'error could not open'

s3 = boto3.client('s3',region_name='us-east-2')
#with open('files/'+fn, "rb") as f:
s3.upload_fileobj(file, "xxxxxxx", fn)#xxxxx change to yours


########################################################################################  Database
region_name='us-east-1',
aws_access_key_id='xxxxxxxxxxxxx', #change to yours
aws_secret_access_key='xxxxxxxxxxxxxxxxxx'#change to yours



dynamodb = boto3.resource('dynamodb',region_name='us-east-2')

#this is the table name
table = dynamodb.Table('Applications')


#this puts the item in the table
table.put_item(
   Item={
        'Snumber': Student_Number,
	'Name': name,
	'Email': email,
    }
)

#pulls data back off the table to show that you can search using just the
#primary key that is the student number
response = table.get_item(
    Key={
        'Snumber': Student_Number
            }
)


item = response['Item']  # item from database











#########################################################################################

#print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<body>")
#print ("<p>%s</p>" % item)
print ("<p>%s</p>" % message)
print ("<p>%s</p>" % errormessage)
print ("</body>")
print ("</html>")




