# Read a jpeg image and print the image file
from PIL import Image
img = Image.open("C:\\Users\\anvitha\\Downloads\\book.jpeg")
img.show()
print(img.format)

# Merge two pdf files using python script

import PyPDF2
pdf1File = open('python_basics.pdf', 'rb')
pdf2File = open('python-practice-book.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

# Scarp a website and store the data into DB
import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="website"
)
dbse = mydb.cursor()
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.text,"html.parser")

print(soup.prettify())

#write queries  to filter thr data in db
import pandas as pd
data = pd.read_csv("employees.csv")

data.columns = [column.replace(" ", "_") for column in data.columns]
data.query('Senior_Management == True', inplace=True)
print(data)
