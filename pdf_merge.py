# This program merges all pdfs in the specified directory into one pdf
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time

# get all pdfs's names.
def getFileName(filedir):

    file_list = [os.path.join(root, filespath) \
                for root, dirs, files in os.walk(filedir) \
                for filespath in files \
                if str(filespath).endswith('pdf')
                ]
    return file_list if file_list else []

# merge
def MergePDF(filepath, outfile):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            print("path：%s"%pdf_file)

            input = PdfFileReader(open(pdf_file, "rb"))

            # get a pdf's page size.
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("page size：%d"%pageCount)

            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))

        print("Page size after merge: %d."%outputPages)
        
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        print("PDF merge success!")

    else:
        print("no pdf to merge!")

def main():
    time1 = time.time()
    file_dir = r'C:\Users\yuanluo\Desktop\merge'  # your pdfs directory. 
    outfile = "outPdf.pdf"         # final pdf's name.
    MergePDF(file_dir, outfile)
    time2 = time.time()
    print('time cost: %s s.' %(time2 - time1))

main()
