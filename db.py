from business.business import db
from orders.order import db
from products.product import db
from users.user import db

db.create_all()