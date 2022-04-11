# - 
# Copyright 2021 Jide Olayinka
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def get_all_task(issue=None):
    """ all task linked to single issue"""
    issue = issue
    task_list = frappe.db.sql(""" 
    SELECT name,status,subject FROM `tabTask` WHERE docstatus <> 2 AND issue = '{0}'
    """.format(issue), as_dict=1 )
    return task_list
