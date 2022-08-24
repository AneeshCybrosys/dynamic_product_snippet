# -*- coding: utf-8 -*-
{
    'name': "Dynamic Product Snippet",

    'summary': """
        Helps to show most viewed and most sold products""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0.0',
    'depends': ['website','website_sale'],

    'data': [
        'views/dynamic_snippet_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'dynamic_product_snippet/static/src/js/dynamic.js',
        ]
    }
}
