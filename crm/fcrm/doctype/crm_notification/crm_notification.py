# Copyright (c) 2024, Westrnet Inc. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CRMNotification(Document):
    def on_update(self):
        frappe.publish_realtime("crm_notification")
