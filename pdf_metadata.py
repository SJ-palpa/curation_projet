import os
from PyPDF2 import PdfFileReader
import csv

directoryPath = "***path***"


def get_info(path):
    with open(path, 'rb') as f:
        try:

            pdf = PdfFileReader(f)
            info = pdf.getDocumentInfo()
            author = info.author
            creator = info.creator
            producer = info.producer
            subject = info.subject
            title = info.title
            listPfmeta = ["Author:"+ ""+str(author), "creator:"+str(creator),"producer:"+ str(producer),"subject:"+ str(subject),"title:"+ str(title)]
            outfile = open('/Users/stephane/Desktop/webScraping/meta_cc.csv', 'a')
            out = csv.writer(outfile)
            out.writerow(listPfmeta)
            outfile.close()
        except:
            print("An exception occurred")
            print(path)




for filename in os.listdir(directoryPath):
    if filename.endswith(".pdf"):
        get_info(os.path.abspath(directoryPath+filename))
        continue
    else:
        continue


