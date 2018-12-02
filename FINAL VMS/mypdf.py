from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import random
def user_pass(identity,purpose,visitor_name):
    dt=datetime.datetime.now().strftime('%d/%m/%y  %H:%M:%S')
    name=str(identity)+".pdf"
    print(name)

    c=canvas.Canvas(str(name))
    c.setPageSize((720,400))
    c.setLineWidth(.8)


    c.drawString(30,370,"VISITOR PASS: ")
    c.drawString(30,340,"BARCODE INDIA LIMITED: ")
    c.drawString(500,340,"DATE&TIME: ")
    c.drawString(600,340,dt)
    c.line(590,338,695,338)

    c.drawString(500,325,"PURPOSE OF VISIT: ")
    c.drawString(620,325,purpose.upper())
    c.line(610,323,700,323,)

    c.drawString(350,240,"VISITOR ID:")
    c.drawString(430,240,identity)
    c.drawString(350,215,"VISITOR NAME:")
    c.drawString(450,215,visitor_name.upper()),

    

    

    c.save()





