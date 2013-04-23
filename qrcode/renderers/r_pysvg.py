from pysvg.builders import *


def render(qrcode):
    """
    Make a pySVG image from the QR Code data.

    If the data has not been compiled yet, make it first.
    """
    if qrcode.data_cache is None:
        qrcode.make()
    offset = qrcode.border   # Spec says border should be at least four boxes wide
    pixelsize = (qrcode.modules_count + offset * 2) * qrcode.box_size
    oh = ShapeBuilder()
    # pysvg backward compatibility fix
    try:
        img = svg()
    except NameError:
        img = Svg()
    img.addElement(oh.createRect(0,0,pixelsize, pixelsize, strokewidth=0, fill="white"))
    for r in range(qrcode.modules_count):
        for c in range(qrcode.modules_count):
            if qrcode.modules[r][c]:
                x = (c + offset) * qrcode.box_size
                y = (r + offset) * qrcode.box_size
                #SVG Rectangle is x, y, size_x, size_y
                img.addElement(oh.createRect(x,y, qrcode.box_size, qrcode.box_size,
                                          strokewidth=0, fill="black"))
    return img