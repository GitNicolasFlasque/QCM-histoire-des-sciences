# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:59:39 2018

@author: cgal
"""


from pyPdf import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import utils
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image

def hasLogo(page_number):
    logotable = False
    exampages = 8
    relpagenum = page_number % exampages
    isbasepage = (relpagenum == 0)
    isanswerpage = (relpagenum == exampages-2)
    logotable = isbasepage or isanswerpage
    return logotable

def extract_answer_sheets(filename):
    exampages = 8
    infile = PdfFileReader(file(filename, 'rb'))
    outfilename = 'answer_sheets_' + filename
    nbp = infile.getNumPages()

    output = PdfFileWriter()
    for cpt in range(nbp):
        relpagenum = cpt % exampages
        isanswerpage = (relpagenum == exampages-2)
        if isanswerpage :        
            page = infile.getPage(cpt)
            output.addPage(page)
            page = infile.getPage(cpt+1)
            output.addPage(page)
    
    outfile = file(outfilename, u'wb')
    output.write(outfile)
    outfile.close()   
    return

def logotage(filename):
    infile = PdfFileReader(file(filename, 'rb'))
    outfilename = 'logo_' + filename
    # preparation du watermark : logo
    wmname = './logos/watermark_logo.pdf'
    wm=PdfFileReader(file(wmname,"rb"))
    mergepage = wm.getPage(0)
    
    nbp = infile.getNumPages()
    output = PdfFileWriter()
    for cpt in range(nbp):
        page = infile.getPage(cpt)
        if hasLogo(cpt): # on ajoute le watermark sur les seules pages concernees
            page.mergePage(mergepage)         
        output.addPage(page)
    
    outfile = file(outfilename, u'wb')
    output.write(outfile)
    outfile.close()
    return
