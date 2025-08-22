import cgi, cgitb
from datetime import datetime

dataFilePath = 'myData/myData.txt'

print("Content-Type: text/html") 
print()

print() 
print("""<html>
<head> 
<meta http-equiv="refresh" content="1; url=index.py" />
</head>
<body>""" )

form = cgi.FieldStorage()
text = form.getvalue('mytext')

if text is None:       
    print("<h1>No message </h1>")
else:
    text = text.strip()
    if text:
        with open(dataFilePath, 'a') as file:
            file.write(datetime.now().strftime('%d/%m/%Y - %H:%M:%S') + "\n")
            file.write(text + "\n")
        print(f"<h1>Message added: {text}</h1>")
    else:
        print("<h1>Message was empty!</h1>")
    
print("<a href=\"index.py\"> </a>")
print("</body></html>")
        