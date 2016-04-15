# -*- coding: utf-8 -*-
{
    'name': 'weigh',
    'version': '0.1',
    'category': 'Tools',
    'description': """
weigh
""",
    'author': 'lipeng',
    'website': 'https://www.ylnlp.com',
    'summary': 'weith',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'models/nc_order_line.xml',
        'models/dispatche_vehicle.xml',
        'models/sample.xml',
        'views/cron.xml',
        'views/views.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'depends': ['base', 'mail', 'fleet'],
    'sequence': 0,
    'installable': True,
    'application': True,
    'auto_install': False,
}
