# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        Un modulo muy malo""",

    'description': """
        Un modulo muy malo para hospitales con un 100% de tasa de mortalidad
    """,

    'author': "Arion Sintes",
    'website': "http://github.com/Sud0cs",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/view_pacients.xml'
    ]
}
