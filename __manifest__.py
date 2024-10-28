{
    'name': 'ChatGPT Integration',
    'version': '1.0',
    'summary': 'Integration with ChatGPT for Odoo Discuss and Chatbot',
    'author': 'Alexandre Defendi - Mutualizo',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/chatgpt_data.xml',
        'views/chatgpt_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}
