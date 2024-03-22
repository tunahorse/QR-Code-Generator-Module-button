{
    'name': "Product QR Code Generator",
    'version': "1.0",
    'depends': ['base', 'product'],
    'author': "fabiananguiano.com",
    'category': "Product",
    'description': """
    Module adds a button to generate QR code for product.
    
    This module does one thing, and one thing well it creates a QR code for a product.
    """,
    'data': [
        'views/product_template_qr_view.xml',
       
    ],
    'images':['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1'
}
