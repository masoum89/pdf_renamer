__author__ = 'mehdi'

# import os


path = '/media/mehdi/New Volume1/Learning/Uni/Master/Thesis/ICN (copy)'

from os import listdir, system
from os.path import isfile, join, isdir
from pyPdf import PdfFileReader, PdfFileWriter

# import pdfquery
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument

def get_all_files_recursively(root):
    files = [join(root, f) for f in listdir(root) if isfile(join(root, f)) and f.split('.')[-1] == 'pdf']
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        files_in_d = get_all_files_recursively(join(root, d))
        if files_in_d:
            for f in files_in_d:
                if f.split('.')[-1] == 'pdf':
                    files.append(join(root, f))
    return files


def pdf_name_extract(file):
    if file.split('.')[-1] == 'pdf':
        # pdfquery.PDFQuery()
        pdf = PdfFileReader(open(file, 'rb'))
        info = pdf.getDocumentInfo()
        try:
            name = info['/Title']
        except:
            name = ''
        return name


def rename_recursively(files):
    for file in files:
        name = pdf_name_extract(file)
        file2 = file.replace(path, path+'/new')
        file2 = file2.replace(' ', '\ ')
        # print file2
        dir = ''
        for s in file2.split('/')[:-1]:
            dir += s+'/'
        # print dir

        try:
            system('mkdir '+dir)
        except:
            pass
        system('cp '+file+' '+file2)
        # print file, ' ...\n'


# print(get_all_files_recursively(path))

# files = os.listdir(path)

if __name__ == '__main__':
    path = '/media/mehdi/New Volume1/Learning/Uni/Master/Thesis/ICN2'
    files = get_all_files_recursively(path)
    rename_recursively(files)