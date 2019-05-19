# Here go your api methods.


def get_products():
	product_list = db().select(db.r_products.ALL)
	if request.args.query is None:
		return response.json(dict(product_list=product_list))
	else:
		return response.json(dict(product_list=product_list))
		