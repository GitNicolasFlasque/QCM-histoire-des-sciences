# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyPdf import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import utils
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image 



def split_sujet(filename):
    
    infile=PdfFileReader(file(filename,"rb"))
    nbp=infile.getNumPages()
    for cpt in range(nbp):
        page=infile.getPage(cpt)
        output=PdfFileWriter()
        output.addPage(page)
        outfilename="page_"+str(cpt+1)+"_sur_"+str(nbp)+".pdf"
        outputFile=file(outfilename,u"wb")
        output.write(outputFile)
        outputFile.close()
        
    return
        

def surimprime(AMCsource, sid, lname, fname):
    wmname="watermark.pdf"
    inputf=PdfFileReader(file(AMCsource,"rb"))
    page=inputf.getPage(0)    
    
    output=PdfFileWriter()
    outfilename=AMCsource+"_modifie.pdf"
    outputstream=file(outfilename,u"wb")    
    
    c=canvas.Canvas(wmname)
    c.setFillColorRGB(0,0,0) # black filling for squares

# automatic student number filling

    xbase=4.05*cm
    ybase=24.45*cm
    offsetx=0.785*cm
    offsety=0.595*cm
    dimr = 0.38*cm
    
    for ln in range(0,8):
        num=ord(sid[ln])-ord('0')
        xbox=xbase+(ln*offsetx)
        ybox=ybase-(num*offsety)
        c.rect(xbox, ybox, dimr, dimr, fill=1)

# name and surname

    pdfmetrics.registerFont(TTFont('libertine','/usr/local/share/fonts/LinLibertine_Rah.ttf'))

    c.setFont("libertine",12)
    c.drawString(11.5*cm,21.35*cm, lname)
    c.drawString(11.5*cm,20.75*cm, fname)    
    c.drawString(11.5*cm,20.15*cm, sid)
#Efrei Paris logo
 
    c.drawImage("./logo efrei paris.png",0.3*cm,27.9*cm,4.5*cm,1.5*cm)
   
    c.showPage()
    c.save()
    
    wm=PdfFileReader(file(wmname,"rb"))

    page.mergePage(wm.getPage(0))
    output.addPage(page)
    output.write(outputstream)
    outputstream.close()
    
    return
    
def prepare_exam(studfilename):
    
    studfile=open(studfilename,"r")
    studcpt=0
    
    for line in studfile:
        if studcpt > 0:
            data=line.split(',')
            rawfname=data[2]
            strname=rawfname[1:len(rawfname)-2]
            fname=strname.decode('utf-8').encode('utf-8')
            pnb=str(3*studcpt)
            modfilename="page_"+pnb+"_sur_120.pdf"
            print(data[1])

            surimprime(modfilename,data[0],data[1],fname)

        studcpt=studcpt+1
    
    
    return