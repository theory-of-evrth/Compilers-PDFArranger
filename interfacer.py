from reportlab.pdfgen import canvas

# test library present and working
def hello(c):
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("hello.pdf")
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

"""