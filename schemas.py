from main import ma


class OrderSchema(ma.Schema):
    class Meta:
        fields=('id','products','total_price','client','address','contact','complete','created_at')

orderSchema=OrderSchema()
ordersSchema=OrderSchema(many=True)

class ProductSchema(ma.Schema):
    class meta:
        fields=('id','name','price','description','type','photo','quantity','photo_2','photo_3')

productSchema=ProductSchema()
productsSchema=ProductSchema(many=True)

class BusinessSchema(ma.Schema):
    orders=ma.Nested(OrderSchema,many=True)
    products=ma.Nested(ProductSchema, many=True)
    class Meta:
        fields=('id','name','username','address','cartegory','phone','photo','pdf_menu','site','subsription','active','products_cartegories','created_at','products','orders')

businessSchema=BusinessSchema()
businessesSchema=BusinessSchema(many=True)

class UserSchema(ma.Schema):
    class Meta:
        fileds=('id','username','name')

userSchema=UserSchema()
usersSchema=UserSchema(many=True)
