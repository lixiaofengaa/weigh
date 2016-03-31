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
        'ecurity/security.xml',
        'security/ir.model.access.csv',
        'models/bid_evaluation.xml',
        'views/cron.xml',
        'views/views.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'depends': ['base', 'mail'],
    'sequence': 0,
    'installable': True,
    'application': True,
    'auto_install': False,
}
