from . import __version__ as app_version

app_name = "frappe_whatsapp"
app_title = "Frappe Whatsapp"
app_publisher = "Shridhar Patil"
app_description = "WhatsApp integration for frappe"
app_email = "shridhar.p@zerodha.com"
app_license = "MIT"
after_install = "frappe_whatsapp.setup.install.create_integrations_card"
before_uninstall = "frappe_whatsapp.setup.uninstall.remove_integrations_card"
scheduler_events = {
  "daily": [
      "frappe_whatsapp.frappe_whatsapp.doctype.whatsapp_notification.whatsapp_notification.trigger_notifications"
  ],
}
doc_events = {
    "*": {
        "before_insert": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "after_insert": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "before_validate": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "validate": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "on_update": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "before_submit": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "on_submit": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "before_cancel": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "on_cancel": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "on_trash": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "after_delete": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "before_update_after_submit": "frappe_whatsapp.utils.run_server_script_for_doc_event",
        "on_update_after_submit": "frappe_whatsapp.utils.run_server_script_for_doc_event"
    }
}
