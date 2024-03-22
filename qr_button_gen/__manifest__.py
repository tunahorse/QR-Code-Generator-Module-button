{
    'name': "Product QR Code Gen",
    'version': "1.0",
    'depends': ['base', 'product'],
    'author': "fabiananguiano.com",
    'category': "Product",
    'description': """
    Module adds a button to generate QR code for product.
    """,
    'data': [
        'views/product_template_qr_view.xml',
       
    ],
    'images': ['static\description\cover.png'],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1'
}
