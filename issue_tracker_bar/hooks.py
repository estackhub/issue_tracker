from . import __version__ as app_version

app_name = "issue_tracker_bar"
app_title = "Issue Tracker Bar"
app_publisher = "Jide Olayinka"
app_description = "Issues status visual progress representation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "appdev@grossin.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/issue_tracker_bar/css/issue_tracker_bar.css"
# app_include_js = "/assets/issue_tracker_bar/js/issue_tracker_bar.js"

# include js, css files in header of web template
# web_include_css = "/assets/issue_tracker_bar/css/issue_tracker_bar.css"
# web_include_js = "/assets/issue_tracker_bar/js/issue_tracker_bar.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "issue_tracker_bar/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "issue_tracker_bar.install.before_install"
# after_install = "issue_tracker_bar.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "issue_tracker_bar.uninstall.before_uninstall"
# after_uninstall = "issue_tracker_bar.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "issue_tracker_bar.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"issue_tracker_bar.tasks.all"
# 	],
# 	"daily": [
# 		"issue_tracker_bar.tasks.daily"
# 	],
# 	"hourly": [
# 		"issue_tracker_bar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"issue_tracker_bar.tasks.weekly"
# 	]
# 	"monthly": [
# 		"issue_tracker_bar.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "issue_tracker_bar.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "issue_tracker_bar.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "issue_tracker_bar.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"issue_tracker_bar.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
