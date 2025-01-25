from reportlab.pdfgen import canvas
from reportlab.pdfgen import textobject
from reportlab.pdfgen import pathobject
from reportlab.lib.pagesizes import A4
from reportlab.graphics import shapes
import array as arr


"""
Interfacer for the PDF Compiler, to interact with the reportlab

Authoring: Brandt Mael
"""


class Interfacer:
    def __init__(self, file: str, pagesize: tuple[float, float] = A4):
        try:
            self.c = canvas.Canvas(filename=file, pagesize=pagesize)
        except:
            open(file=file, mode="x").close()  # create a new file, and imediately close it
            self.c = canvas.Canvas(filename=file, pagesize=pagesize)

        self.color = "#FFFFFF"  # background are white by default
        self.borderColor = "#000000"  # borders are black by default
        self.textColor = "#000000"  # text is black by default

    def setCanvas(self, filename: str, pagesize: tuple[float, float] = A4):
        self.c = canvas.Canvas(filename=filename, pagesize=pagesize)

    def getCanvas(self):
        return self.c

    def setColor(self, color: str = None, borderColor: str = None, textColor: str = None):
        # make color, borderColor and textColor argument optional
        if color != None:
            self.color = color
        if borderColor != None:
            self.borderColor = borderColor
        if textColor != None:
            self.textColor = textColor

        # set canvas colors
        self.c.setFillColor(aColor=self.color)
        self.c.setStrokeColor(aColor=self.borderColor)

    def drawLine(self, positions: arr.array[float]):
        """draw a line based on two points.

        Args:
            position : an array containing the coordinates of the starting and ending points of the line
            color    : string representing the hexadecimal value of a color (format: #hex_value)
        """
        self.c.line(x1=positions[0], y1=positions[1], x2=positions[2], y2=positions[3])

    def drawCircle(self, centre: arr.array[float], radius: float, border: int = 1, fill: int = 1):
        self.c.circle(x_cen=centre[0], y_cen=centre[1], r=radius, stroke=border, fill=fill)

    def drawRectangle(self, position: arr.array[float], width: float, height: float, border: int = 1, fill: int = 1):
        """Args:
        position : coordinate of the bottom left corner
        size : array containg with an height
        """
        self.c.rect(x=position[0], y=position[1], width=width, height=height, stroke=border, fill=fill)

    def drawTriangle(self, p1, p2, p3):
        p = self.c.beginPath()
        p.moveTo(p1[0], p1[1])
        p.lineTo(p2[0], p2[1])
        p.lineTo(p3[0], p3[1])
        p.close()
        self.c.drawPath(p)

        self.c.drawPath(aPath=p)

    def drawShape(self, pointList, pointNumber):
        """draw any shape

        Args:
            pointList (_type_): list of point representing the corner of the shape
            pointNumber (_type_): number of element in pointList
        """
        p = self.c.beginPath()
        p.moveTo(pointList[0][0], pointList[0][0])
        for point in pointList:
            p.lineTo(point[0], point[1])
        p.close()
        self.c.drawPath(p)

        self.c.drawPath(aPath=p)

    def drawText(self, position: arr.array[float], content: list[str], font="Helvetica", size=20):
        """Draw text in the PDF.

        Args:
            position (arr.array[float]): Starting position of the text.
            content (list[str]): Text to be written on the pdf. Each element is written on a new line
            font (str, optional): font of the text. Defaults to "Helvetica".
            size (int, optional): size of the text's font. Defaults to 20.
        """

        self.c.setStrokeColor(self.textColor)
        self.c.setFillColor(self.textColor)

        self.c.setFont(psfontname=font, size=size)  # TODO attribut self.font, self.fontsize
        self.c.drawString(x=position[0], y=position[1], text=content)

        self.c.setStrokeColor(self.borderColor)  # keep text color separate from shape color
        self.c.setFillColor(self.color)

    def setBackgroundColor(self, color="#FFFFFF"):
        """Draw a rectangle the size of the page

        Args:
            color (str, optional): color of the background, the format of the str is #hex_value (exemple: #FF0000 for red). Defaults to white.
        """
        self.c.setFillColor(color)
        self.drawRectangle(position=[0, 0], width=A4[0], height=A4[1], border=0)
        self.c.setFillColor(self.color)  # this method doesn't modify the drawing color of the others methods


if __name__ == "__main__":
    # test if library is working
    interfacer = Interfacer("./generated/hello.pdf")
    interfacer.setBackgroundColor("#00DD00")
    interfacer.drawLine([10, 700, 10, 750])
    interfacer.setColor("#FF0000", "#0000FF", "0x662366")
    interfacer.drawText((20, 710), "Hello, world!", size=40)
    interfacer.drawCircle([100, 100], 20)
    interfacer.drawRectangle(position=[200, 100], width=30, height=35, fill=0)
    interfacer.drawCircle(centre=[300, 100], radius=20, border=0)
    interfacer.drawTriangle((30, 600), (30, 500), (50, 650))

    c = interfacer.getCanvas()
    c.showPage()
    c.save()
