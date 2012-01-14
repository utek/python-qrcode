# Try to import PIL in either of the two ways it can be installed.
try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image, ImageDraw
    
    
def make_image(qrcode):
    """
    Make a PIL image from the QR Code data.

    If the data has not been compiled yet, make it first.
    """
    if qrcode.data_cache is None:
        qrcode.make()
    offset = self.border   
    pixelsize = (qrcode.modules_count + offset * 2) * qrcode.box_size

    im = Image.new("1", (pixelsize, pixelsize), "white")
    d = ImageDraw.Draw(im)    
    for r in range(qrcode.modules_count):
        for c in range(qrcode.modules_count):
            if qrcode.modules[r][c]:
                x = (c + offset) * qrcode.box_size
                y = (r + offset) * qrcode.box_size
                b = [(x, y),
                    (x + qrcode.box_size - 1, y + qrcode.box_size - 1)]
                d.rectangle(b, fill="black")
    return im