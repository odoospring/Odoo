{
    'name': 'EDI Tools',
    'version': '18.0.1.0.0',
    'category': 'EDI',
    'summary': 'Simple EDI Management Tools',
    'description': 'Manage EDI trading partners and settings.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',

    'depends': [
        'base'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/edi_partner_views.xml',
        'views/menus.xml',
    ],

    'images': [
        'static/description/icon.png'
    ],

    'installable': True,
    'application': True,
}
