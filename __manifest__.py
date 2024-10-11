{
    'name': "To Do App ",
    'author': "Muhamed Magdy",
    'category': '',
    'version': '17.0.1.0',
    'depends': ['base', 'sale', 'account', 'mail', 'contacts'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/res_partner_view.xml',
        'views/todo_task_view.xml',
    ],
    'application': True,


}