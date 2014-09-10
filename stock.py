from openerp.osv import fields,osv
from openerp import tools

 
class stock_inventory_report(osv.osv):
    _name = "stock.inventory.vat_report"
    _description = "Stock Inventory Report"
    _auto = False
    _columns = {
	'product_id': fields.many2one('product.product','Product'),
	'partner_id': fields.many2one('res.partner','Partner Name'),
	'qty': fields.float('Tax Amount',readonly=True,group_operator="sum",digits=(16,2)),
	'cost': fields.float('Cost',readonly=True,group_operator="avg",digits=(16,2)), 
	}
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'stock_inventory_report')
	cr.execute("""
		create or replace view stock_inventory_report as (
		select  a.id as id,a.product_id,a.location_id,avg(a.cost) as cost,sum(a.qty) as qty from stock_quant group by 1,2
	""")	
 
stock_inventory_report()
