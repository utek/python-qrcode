#import cairo
import cairo


def prepare(qrcode):
    if qrcode.data_cache is None:
        qrcode.make()
    offset = qrcode.border   # Spec says border should be at least four boxes wide
    pixelsize = (qrcode.modules_count + offset * 2) * qrcode.box_size
    return (offset, pixelsize)

def make(qrcode, surface, pixelsize, offset):
    ctx = cairo.Context(surface)
    pat_w = cairo.SolidPattern(1, 1, 1, 1)
    pat_b = cairo.SolidPattern(0, 0, 0, 1)
    ctx.rectangle(0, 0, pixelsize, pixelsize)
    ctx.set_source(pat_w)#fill it white
    ctx.fill()
    ctx.set_source(pat_b)#paint it black
    for r in range(qrcode.modules_count):
        for c in range(qrcode.modules_count):
            if qrcode.modules[r][c]:
                x = (c + offset) * qrcode.box_size
                y = (r + offset) * qrcode.box_size
                #cairo Rectangle is x0, y0, x1, y1
                x1, y1 = (qrcode.box_size, qrcode.box_size)
                ctx.rectangle(x, y, x1, y1)
                ctx.fill()
    return surface

def render_image(qrcode):
    """
    Make a cairo ImageSurface version of QRCode

    return cairo ImageSurface
    """
    offset, pixelsize = prepare(qrcode)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, pixelsize, pixelsize)
    return make(qrcode, surface, pixelsize, offset)

def render_svg(qrcode):
    """
    Make a cairo SVGSurface version of QRCode
    return stream (io.BytesIO)

    """
    import io
    stream = io.BytesIO()
    offset, pixelsize = prepare(qrcode)
    surface = cairo.SVGSurface(stream, pixelsize, pixelsize)
    surface = make(qrcode, surface, pixelsize, offset)
    surface.finish()
    stream.seek(0)
    return stream

def render_pdf(qrcode):
    """
    Make a cairo SVGSurface version of QRCode
    return stream (io.BytesIO)

    """
    import io
    stream = io.BytesIO()
    offset, pixelsize = prepare(qrcode)
    surface = cairo.SVGSurface(stream, pixelsize, pixelsize)
    surface = make(qrcode, surface, pixelsize, offset)
    surface.finish()
    stream.seek(0)
    return stream

#default renderer
render = render_svg