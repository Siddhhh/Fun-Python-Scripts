import PyPDF2
import pyttsx3
filename=input("Enter pdf you want to read")
book=open(filename,'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
speaker=pyttsx3.init()
num=input("Enter page number you want to start reading")
page=pdfReader.getPage(num)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()
