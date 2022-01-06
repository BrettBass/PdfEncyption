#encrypt a pdf file with a password
#usage: pdfencrypt.py <pdf file> <password>

import sys
import PyPDF2

#get the pdf file and password
pdfFile = sys.argv[1]
password = sys.argv[2]

#open the pdf file
pdfReader = PyPDF2.PdfFileReader(open(pdfFile, 'rb'))

#create a new pdf file
pdfWriter = PyPDF2.PdfFileWriter()

#encrypt the pdf file
pdfWriter.encrypt(password)

#loop through all pages
for pageNum in range(pdfReader.numPages):
    #add each page to the new pdf file
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

#open the new pdf file
#file name is the same as the old pdf file eith the .pdf extension replaced with _encrypted.pdf
with open(pdfFile[:-4] + '_encrypted.pdf', 'wb') as f:
    #write the new pdf file
    pdfWriter.write(f)

#print success message
print('Done.')
