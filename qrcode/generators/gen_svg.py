# Try to import PIL in either of the two ways it can be installed.
from pysvg.filter import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *
    
   
def make_image(qrcode):
    """
    Make a PIL image from the QR Code data.

    If the data has not been compiled yet, make it first.
    """
    if qrcode.data_cache is None:
        qrcode.make()
    offset = 4   # Spec says border should be at least four boxes wide
    pixelsize = (qrcode.modules_count + offset * 2) * qrcode.box_size

    #im = Image.new("1", (pixelsize, pixelsize), "white")
    #d = ImageDraw.Draw(im)
    oh2 = ShapeBuilder()
    oh = ShapeBuilder()
    s = svg()
    #print pixelsize
    s.addElement(oh2.createRect(0,0,pixelsize, pixelsize, strokewidth=0, fill="white"))
    for r in range(qrcode.modules_count):
        for c in range(qrcode.modules_count):
            if qrcode.modules[r][c]:
                x = (c + offset) * qrcode.box_size
                y = (r + offset) * qrcode.box_size
                b = [(x, y),
                    (x + qrcode.box_size - 1, y + qrcode.box_size - 1)]
                #d.rectangle(b, fill="black")
                #print x, y, x + qrcode.box_size - 1, y + qrcode.box_size - 1
                s.addElement(oh.createRect(x,y, qrcode.box_size, qrcode.box_size,
                                          strokewidth=0, stroke="black", fill="black"))
    return s