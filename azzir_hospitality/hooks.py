app_name = "azzir_hospitality"
app_title = "Azzir Hospitality"
app_publisher = "Azzir Group"
app_description = "Comprehensive hospitality management for restaurants and hotels, inspired by Lending module."
app_icon = "octicon octicon-briefcase"
app_color = "blue"
app_email = "info@azzir.com"
app_license = "GPL-3.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/azzir_hospitality/css/azzir_hospitality.css"
# app_include_js = "/assets/azzir_hospitality/js/azzir_hospitality.js"

# include js, css files in header of web template
# web_include_css = "/assets/azzir_hospitality/css/azzir_hospitality.css"
# web_include_js = "/assets/azzir_hospitality/js/azzir_hospitality.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "azzir_hospitality.install.before_install"
# after_install = "azzir_hospitality.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config
# notification_config = "azzir_hospitality.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways
# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
# has_permission = {
#   "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes
# override_doctype_class = {
#   "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#   "all": [
#       "azzir_hospitality.tasks.all"
#   ],
#   "daily": [
#       "azzir_hospitality.tasks.daily"
#   ],
#   "hourly": [
#       "azzir_hospitality.tasks.hourly"
#   ],
#   "weekly": [
#       "azzir_hospitality.tasks.weekly"
#   ],
#   "monthly": [
#       "azzir_hospitality.tasks.monthly"
#   ],
# }

# Testing
# -------
# before_tests = "azzir_hospitality.install.before_tests"

# Overriding Methods
# ------------------------------
# override_whitelisted_methods = {
#   "frappe.desk.doctype.event.event.get_events": "azzir_hospitality.event.get_events"
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#   "Task": "azzir_hospitality.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
# auto_cancel_exempted_doctypes = ["Auto Repeat"] 