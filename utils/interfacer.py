from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os.path

# test library present and working
def hello(c):
    c.setFillColor("#0000FF") 
    c.drawString(100,100,"Hello World")    
c = canvas.Canvas("compil/Compilers-PDFArranger/generated/hello.pdf", pagesize=A4)
hello(c)
c.showPage()
c.save()

"""
TODO : create functions for interfacing with the library
needed functions:
- create canvas
- draw line (position, color, size) 
- draw circle (position, color, size)
- draw triangle (position, color, size)
- draw text (position, color, size, content) opt.: font (set default value)
- set background color (?)
- save file as (filename)

!! spumoni for overlap. Test with overlapping of different elements
"""

def createCanvas(filename, pagesize: tuple[float, float]):
    c = canvas.Canvas(filename, pagesize=pagesize)
    return c

# TODO drawing line based on 2 point would vbe better, no ?
def drawLine(c: canvas.Canvas, position: tuple[float, float], color: str, size: float):
    """draw a line based on a point and a length.
    
    param:  
        position : a tuple containing the coordinate of the starting point of the line
        color    : string representing the hexadecimal value of a color (format: #hex_value)
        size     : length of the line
    """
    c.setStrokeColor(aColor=color)
    c.line(x1=position[0], y1=position[1], x2=position[0] + size, y2=position[1] + size)

def drawCircle(position, color, size):
    pass

def drawTriangle(position, color, size):
    pass

def drawText(c: canvas.Canvas, position: tuple[float, float], color: str, content, font="Helvetica", size=20):
    c.setFillColor(aColor=color)
    c.setFont(psfontname=font, size=size)
    c.drawString(x=position[0], y=position[1], text=content)

def setBackgroundColor(color):
    pass

def saveFileAs(fileName):
    pass