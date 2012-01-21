#"Just doing something for the sake of doing something..."

def html(qrcode):
    """
    Make a HTML table from the QR Code data.

    If the data has not been compiled yet, make it first.

    It's just for fun
    """
    if qrcode.data_cache is None:
        qrcode.make()
    modules = qrcode.modules_count
    output = """<style type="text/css">
    table.qrcode{
        border-width: 0px;
        border-style: none;
        border-spacing: 0px;
        border-collapse: collapse;
        background-color: white;
        line-height: %spx;
    }
    td{
        border-width: 0px;
        width: %spx !important;
        height: %spx !important;
    }
    td.black {
        background-color: #000;
    }
    </style>
    """ % (qrcode.box_size, qrcode.box_size, qrcode.box_size)
    output += "<table class='qrcode'>"
    for row in xrange(modules):
        output += "<tr>"
        for col in range(modules):
            if qrcode.modules[row][col]:
                output += "<td class='black'>&nbsp;"
            else:
                output += "<td>&nbsp;"
            output += "</td>"
        output += "</tr>"
    output += "</table>"
    return output


render = html
