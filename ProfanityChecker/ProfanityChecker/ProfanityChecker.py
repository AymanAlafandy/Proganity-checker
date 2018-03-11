import urllib

def readText():
   importedText = open("C:\Users\AymanAlafandy\Desktop\ooo.txt")# put a path to your file
   content = importedText.read()
   print content
   importedText.close()
   checkProfanity(content) 


def checkProfanity(contentToTest):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+contentToTest)
    response = connection.read()
    print response
    connection.close()
 
readText()
