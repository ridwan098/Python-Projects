import random
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Hello</title>
</head>
<body>
loop = 1 == 1
while 1 == True:

    print("My mood ranges from 1 to 3, \n Enter a number between these to show my mood")
    mood = float(random.randint(0,3))




    if mood == 1:
        print ("my mood is :)")
    if mood == 2:
        print ("my mood is :(")
    if mood == 3:
        print ("my mood is :|")</body>
</html>
'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()
loop = 1 == 1
while 1 == True:

    print("My mood ranges from 1 to 3, \n Enter a number between these to show my mood")
    mood = float(random.randint(0,3))




    if mood == 1:
        print ("my mood is :)")
    if mood == 2:
        print ("my mood is :(")
    if mood == 3:
        print ("my mood is :|")
