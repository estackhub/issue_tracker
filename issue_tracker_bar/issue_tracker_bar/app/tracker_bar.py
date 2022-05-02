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
    task_list = []
    task_list = frappe.db.sql(""" 
    SELECT name,status,subject FROM `tabTask` WHERE docstatus <> 2 AND issue = '%s'
    """%issue, as_dict=1 )

    """get all  available status of task"""
    tmeta = frappe.get_meta('Task')
    tstatus = tmeta.get_field('status').options.split("\n")

    """ get all color tagging for task"""
    color_tast_tagr = frappe.db.get_single_value('Issue Task Bar', 'task_status_style').split("\n")
    
    for tl in task_list:
        indexitm = tstatus.index(tl.status)
        tl['tcolor'] = color_tast_tagr[indexitm]

    #print(f"\n\n\n\n\n {task_list} \n\n\n")
    return task_list
    
