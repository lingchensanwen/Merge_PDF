from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
import glob
from os import path

class MergeAllPDF:
    def __init__(self):
        self.mergelist = []

    def create(self, filepath, outpath, outfilename):
        self.outfilname = outfilename
        self.filepath = filepath
        self.outpath = outpath
        self.pdfs = glob.glob(self.filepath)
        self.myrange = len(self.pdfs)

        for _ in range(self.myrange):
            if self.pdfs:
                self.mergelist.append(self.pdfs.pop(0))
        self.mergelist.sort();
        self.merge()

    def merge(self):
        if self.mergelist:
            self.merger = PdfFileMerger()
            for pdf in self.mergelist:
                self.merger.append(open(pdf, 'rb'))  
            self.merger.write(self.outpath + "%s.pdf" % (self.outfilname))
            self.merger.close()
            self.mergelist = []
        else:
            print("mergelist is empty please check your input path")

# example how to use
#update your path here:


dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
in_path = os.path.join(dir_path,"./*.pdf") #here are your single page pdfs stored
out_path = os.path.join(dir_path,"./") #here your merged pdf will be stored
if(path.exists("merged_midterm.pdf")):
    print("Merged file was Created!")
else:
    b = MergeAllPDF()
    b.create(in_path, out_path, "merged_midterm")