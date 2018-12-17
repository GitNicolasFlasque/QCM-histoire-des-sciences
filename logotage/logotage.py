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

def logotage(filename):
    infile = PdfFileReader(file(filename, 'rb'))
    outfilename = 'logo_' + filename
    # preparation du watermark : logo
    imgfile='./logos/logo efrei paris.png'
    wmcanvas = canvas.Canvas('watermark_logo.pdf')
    wmcanvas.drawImage(imgfile, 0.3*cm, 27.9*cm, 4.5*cm, 1.5*cm)
    nbp = infile.getNumPages()
    output = PdfFileWriter()
    for cpt in range(nbp):
        page = infile.getPage(cpt)
        
        output.addPage(page)
    
    outfile = file(outfilename, u'wb')
    output.write(outfile)
    outfile.close()
    return
