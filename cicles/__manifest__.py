# -*- coding: utf-8 -*-
{
    'name': "cicles",

    'summary': """
        Gestio de cicles""",

    'description': """
        Un modul per a gestionar cicles.
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
