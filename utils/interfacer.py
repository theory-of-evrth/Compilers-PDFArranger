from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import A4

# test library present and working
def hello(c):
    c.setFillColor("#FF0000") 
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("generated/hello.pdf", pagesize=A4)
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