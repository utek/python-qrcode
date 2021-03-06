=============================
Pure python QR Code generator
=============================

This module uses the Python Imaging Library (PIL) or pySVG (http://codeboje.de/pysvg/)
to allow for the generation of QR Codes.

What is a QR Code?
==================

A Quick Response code is a two-dimensional pictographic code used for its fast
readability and comparatively large storage capacity. The code consists of
black modules arranged in a square pattern on a white background. The
information encoded can be made up of any kind of data (e.g., binary,
alphanumeric, or Kanji symbols)

Usage
=====

Use the ``make`` shortcut function::

    import qrcode
    img = qrcode.make('Some data here')

    #using renderes
    from qrcode.renderes import r_cairo
    img = qrcode.make('Some data here', renderer=r_cairo.render_pdf)

Advanced Usage
--------------

For more control, use the ``QRCode`` class. For example::

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image()


Using renderes::

    import qrcode
    from qrcode.renderers import r_pil, r_pysvg, r_cairo

    #pysvg
    qr = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        renderer=qrcode.renderers.r_pysvg
    )
    qr.add_data('Some data')
    qr.make(fit=True)
    img = qr.make_image()

    #cairo - PDF
    qr = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        renderer=r_cairo.render_pdf
    )
    qr.add_data('Some data')
    qr.make(fit=True)
    img = qr.make_image() #img is io.ByteIO stream


The ``version`` parameter is an integer from 1 to 40 that controls the size of
the QR Code (the smallest, version 1, is a 21x21 matrix).
Set to ``None`` and use the ``fit`` parameter when making the code to determine
this automatically.

The ``error_correction`` parameter controls the error correction used for the
QR Code. The following four constants are made available on the ``qrcode``
package:

``ERROR_CORRECT_L``
    About 7% or less errors can be corrected.
``ERROR_CORRECT_M`` (default)
    About 15% or less errors can be corrected.
``ERROR_CORRECT_Q``
    About 25% or less errors can be corrected.
``ERROR_CORRECT_H``
    About 30% or less errors can be corrected.

The ``box_size`` parameter controls how many pixels each "box" of the QR code
is.

The ``border`` parameter controls how many boxes thick the border should be
(the default is 4, which is the minimum according to the specs).

The ``renderer`` parameter controls which how qrcode is drawn.
Available renderers:

- ``qrcode.renderers.r_pil`` (default)
    PIL renderer.
- ``qrcode.renderers.r_pysvg``
    pySVG renderer.
- ``qrcode.renderers.r_cairo``
    Cairo renderer. Available formats:
        - ``render_svg`` (default)
        - ``render_pdf``
        - ``render_image``
