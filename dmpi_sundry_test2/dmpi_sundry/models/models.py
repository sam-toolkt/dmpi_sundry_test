# -*- coding: utf-8 -*-
from openerp import models, api, fields
import csv

class SundryPoProduct(models.Model):
	_name = "sundry.po.product"
	_rec_name = "item_code"

	name = fields.Char('Description')
	item_code = fields.Char('Item Code')
	uom = fields.Integer('UOM')
	cas = fields.Float('Cas')
	pcs = fields.Float('Pcs')
	bal_cas = fields.Float('Bal Cas')
	bal_pcs = fields.Float('Bal Pcs')
	hot_qty = fields.Float('Hot Qty')
	remarks = fields.Char('Remarks')

# def name_get(self):
#     res = []
#     for sundry in self:
#         display_name = []
#         res.append((sundry.id,
#                     sundry.name + ' ' + sundry.remarks.name))
#     return res

class DmpiSundryPoAllocation(models.Model):
	_name = 'dmpi.sundry.po.allocation'

	name = fields.Char("Remarks")
	valid_from = fields.Date('Valid From')
	valid_to = fields.Date('Valid To')
	active = fields.Boolean('Active', default=True)

	allocation_line_ids = fields.One2many('dmpi.sundry.po.allocation.line','allocation_id',"Allocation Line", copy=True)

	state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')], string='Status', readonly=True, tracking=True, default='draft', copy=False)
	
	def action_confirm(self):
		print("button_cliked")
		self.state = 'in_progress'
		self.active = True

	def action_draft(self):
		self.state = 'draft'
		self.active = True

	def action_done(self):
		self.state = 'done'
		self.active = False

	def action_cancel(self):
		self.state = 'cancelled'
		self.active = False

class DmpiSundryPoAllocationLine(models.Model):
    _name = 'dmpi.sundry.po.allocation.line'
    _rec_name = 'product_code'

    allocation_id = fields.Many2one('dmpi.sundry.po.allocation','Remarks', ondelete='cascade')
    product_code = fields.Many2one('sundry.po.product','Product Code', ondelete='cascade')

    product_id = fields.Char('Description', related='product_code.name')
    product_uom = fields.Integer('UOM', related='product_code.uom')
    product_cas = fields.Float('Cas', related='product_code.cas')
    product_pcs = fields.Float('Pcs', related='product_code.pcs')
    product_bal_cas = fields.Float('Bal Cas', related='product_code.bal_cas')
    product_bal_pcs = fields.Float('Bal Pcs', related='product_code.bal_pcs')

# def execute(self):
#     # This function return list of dict like this 
#     [{'Char': 'Description','field2': 'value2'}]
#     datas = data_from_your_csv(self.file) 
#     model = "dmpi.sundry.po.allocation.line"
#     for data in datas:
#         record = self.env[model].create(data)













