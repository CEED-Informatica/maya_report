# -*- coding: utf-8 -*-
{
    'name': "Maya | Report",
    'version': '0.1.0a',

    'summary': """
         Extensión de Maya | Core para la gestión de informes""",

    'description': """
        Permite la generación de informes de los diferentes módulos de Maya
    """,

    'author': "Alfredo Oltra",
    'website': "https://portal.edu.gva.es/ceedcv/",
    'maintainer': 'Alfredo Oltra <alfredo.ptcf@gmail.com>',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
 

    'license': 'AGPL-3',
    'price': 0,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
