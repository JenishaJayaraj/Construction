# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nxweb and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BasicRate(Document):
	def validate(self):
		self.update_gst_rate()

	def update_gst_rate(self):
		if self.rate != None and self.gst != None:
			gst_rate = (int(self.rate) * int(self.gst)) / 100
			self.gst_rate = int(gst_rate) + int(self.rate)


@frappe.whitelist()
def update_gst_rate(docname,rate,gst):
	gst_rate = (int(rate) * int(gst)) / 100
	gst_rate_actual = int(gst_rate) + int(rate)
	return gst_rate_actual
