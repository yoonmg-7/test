{
    "name": "starlit_sale!",
    'version': '1.0',
    "category": "sales",
    "summary": "Custom module for the HR!",
    "author": "Task1 for UI Views",
    "depends": ['sale'],
    "data": [
        "security/ir.model.access.csv",

        "views/product_template_inherit_view_form.xml",
        "views/sale_order_view_form.xml",

        "views/sale_product_list_view.xml",
        "views/menu_item.xml",

        "report/sale_order_report.xml",
        "report/sale_report_pivot_view_form_inherit.xml"

    ],
    "installable": True,
    "application": False,
}