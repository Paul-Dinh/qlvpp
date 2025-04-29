# -*- coding: utf-8 -*-
{
    'name': "qlvpp",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'purchase',
        'stock',
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/hr_department.xml',
        'views/hr_employee.xml',

        'views/purchase_view.xml',
        'views/purchase_report.xml',
        'views/purchase_paper.xml',
        'views/purchase_product.xml',
        'views/inventory.xml',
        'views/qlvpp_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}

