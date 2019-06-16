# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2016 Shawn
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Multi-selection to one2many fields",
    "version": "1.0",
    "author": "Shawn",
    "license": "AGPL-3",
    "summary": "Add multi-selection and button capability to one2many fields",
    "description": '''
Description
-----------
This module adds the capability of selecting multiple records in one2many to perform
operations. To use it, simply add widget='one2many_selectable' to your one2many field.

e.g. <field name="categ_id" widget="one2many_selectable">
        <tree>
            <field name="name" />
        </tree>
    </field>


You will get the selected ids of the lines and can pass it to your Python function
I have commented the Python function calls from Javascript so that you can fill it up
with your own model name and function name.


Acknowledgements
----------------
Icon courtesy of http://www.iconfinder.com/
    ''',
    "category": "Web Enhancements",
    "depends": [
        'web',
    ],
    "data": [
        "view/web_assets.xml",
    ],
    "qweb":[
        'static/src/xml/widget_view.xml',
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
