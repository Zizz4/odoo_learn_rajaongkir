{
    'name': 'Aziz Kota',
    'version': '1.0',
    'sequence': 10,
    'summary': 'Bismillah Belajar Payment Gateway',
    'description': 'Bismillah Belajar Payment Gateway',
    'category': 'Productivity',
    'author': 'Muhamad Syahril Aziz',
    'website': 'http://ecodigitus.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/kota.xml',
        'views/kecamatan.xml',
        'views/partner.xml',

        'reports/kota.xml',
        

    ],
    'demo': [''],

    'application': True,
    'installable': True,
    'auto_install': False,
}