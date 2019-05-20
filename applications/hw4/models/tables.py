# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.


db.define_table('r_products', Field('f_name', label='name'), 
						      Field('f_description', label='description'), 
							  Field('f_price', label='price', type='double'))

db.r_products.id.readable = False

"""db.define_table('r_reviews', Field('f_productid', type='reference r_products'), 
						     Field('f_rating', type='integer'), 
							 Field('f_text', type='text'))
"""
# after defining tables, uncomment below to enable auditing
 auth.enable_record_versioning(db)
