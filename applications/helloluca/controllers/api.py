# Here go your api methods.


def get_products():
	
	if request.vars['query'] is None:
		product_list = db().select(db.r_products.ALL)
		return response.json(dict(product_list=product_list))
	else:
		product_list = db(db.r_products.f_name.like(request.vars['query'] + '%') ).select() 
		return response.json(dict(product_list=product_list))
		