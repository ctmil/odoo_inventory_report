from openerp.osv import fields,osv
from openerp import tools

 
class stock_inventory_report(osv.osv):
    _name = "stock.inventory.report"
    _description = "Stock Inventory Report"
    _auto = False
    _columns = {
	'product_id': fields.many2one('product.product','Product'),
	'location_id': fields.many2one('stock.location','Location'),
	'familia': fields.many2one('product.familia','Familia'),
	'categoria': fields.many2one('product.categoria','Categoria'),
	'version': fields.many2one('product.version','Version'),
	'subcategoria': fields.many2one('product.subcategoria','Subcategoria'),
	'sba_code': fields.char('SBA Code'),
	'sba_sku_no': fields.char('SBA SKU No'),
	'cost': fields.float('Cost',readonly=True,group_operator="sum",digits=(16,2)), 
	'qty': fields.float('Quantity',readonly=True,group_operator="sum",digits=(16,2)),
	}
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'stock_inventory_report')
	cr.execute("""
		create or replace view stock_inventory_report as (
		select  a.id as id,a.product_id,a.location_id,b.familia,b.categoria,b.version,b.subcategoria,b.sba_code,b.sba_sku_no,a.cost,a.qty 
			from stock_quant a inner join product_product b on a.product_id = b.id)
	""")	
 
stock_inventory_report()
