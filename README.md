# Odoo QR Code Generator Module

## Overview
This module extends the functionality of Odoo by adding the capability to generate QR codes for products within the `product.template` model. It allows users to generate a QR code based on specific product information, enhancing product identification and integration with other systems.

## Features
- **QR Code Generation:** Generates QR codes for product templates.
- **Customizable QR Content:** Use the `qr_code` field to specify the data encoded in the QR code.
- **Easy Integration:** Seamlessly integrates with the existing Product Template views.

## Installation
1. Ensure you have Odoo installed on your server or local machine.
2. Copy or clone this module into your Odoo addons directory.
3. Restart the Odoo server.
4. Navigate to the Apps menu in the Odoo backend.
5. Remove the Apps filter and search for "QR Code Generator".
6. Install the module by clicking the Install button.

## Usage
1. Navigate to the **Inventory** or **Products** module, depending on your Odoo setup.
2. Open a product template for editing or create a new product template.
3. Locate the **QR Code** field and enter the data you wish to encode in the QR code.
4. Click the **Generate QR Code** button to generate and display the QR code.
5. The generated QR code will be stored and displayed in the **QR Image** field.

## Configuration
No additional configuration is required for this module.

## Dependencies
This module depends on the `product` module (included in Odoo) for extending the `product.template` model.

## Support
For support, feature requests, or bug reports, please contact us at support@example.com.

## Contributing
We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to submit a pull request or open an issue.

## License
This module is licensed under the [LGPL-3](http://www.gnu.org/licenses/lgpl-3.0-standalone.html) license.

---

Thank you for using our Odoo QR Code Generator Module. We hope it enhances your Odoo experience and meets your business needs.
