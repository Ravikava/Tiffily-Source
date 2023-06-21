from apps.helpers.base_model import BaseModel, db
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime
from sqlalchemy.sql import func


class User(BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    dob = db.Column(db.String(12))
    special_day = db.Column(db.String(12))
    profile_image = db.Column(db.String(256))
    background_image = db.Column(db.String(256))
    gender = db.Column(db.Enum('male', 'female', 'other',name="gender_type"))
    food_preference = db.Column(db.Enum('Regular', 'Swaminarayan', 'Jain',name="food_type"))
    is_mobile_verified =db.Column(db.Boolean, default=False)
    is_email_verified =db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    device_id = db.Column(pg.ARRAY(db.String(256), as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    restaurants = db.relationship('Restaurant', backref='owner', lazy=True)
    addresses = db.relationship('UserAddress', backref='user', lazy=True)


class Restaurant(BaseModel):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cuisines = db.Column(pg.ARRAY(db.String(25), as_tuple=False, dimensions=None, zero_indexes=False), nullable=True)
    restaurant_name = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    menu_items = db.relationship('MenuItem', backref='restaurant', lazy=True)


class MenuItemCategory(BaseModel):
    __tablename__ = 'menu_item_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    menu_items = db.relationship('MenuItem', backref='category', lazy=True)
    
    def __repr__(self):
        return self.name


class ReligiousPreference(BaseModel):
    __tablename__ = 'religious_preference'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    menu_items = db.relationship('MenuItem', backref='religious', lazy=True)
    
    def __repr__(self):
        return self.name

class Cuisine(BaseModel):
    __tablename__ = 'cuisine'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    def __repr__(self):
        return self.name

class MenuItem(BaseModel):
    __tablename__ = 'menu_item'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('menu_item_category.id'))
    religious_preference = db.Column(db.Integer, db.ForeignKey('religious_preference.id'),nullable=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    order_items = db.relationship('OrderItem', backref='menu_item', lazy=True)
    
    def __repr__(self):
        return self.name


class Customer(BaseModel):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    billing_address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    orders = db.relationship('Order', backref='customer', lazy=True)
    
    def __repr__(self):
        return self.name


class Order(BaseModel):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    status = db.Column(db.Enum('placed', 'accepted', 'ready', 'out_for_delivery', 'delivered', 'cancelled', 'rejected',name="status_type"))
    total_price = db.Column(db.Integer)
    delivery_time_slot = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(BaseModel):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
    
class UserAddress(BaseModel):
    __tablename__ = 'user_address'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location_type = db.Column(db.Enum('Home', 'Work', 'Hotel', 'Others',name="location_type"))
    address = db.Column(db.Text)
    floor = db.Column(db.String(50),nullable=True)
    landmark = db.Column(db.String(150),nullable=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    
class TodoUser(BaseModel):
    __tablename__ = 'todo_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255), unique=True, nullable=True)
    phone_number = db.Column(db.String(10), unique=True)
    is_mobile_verified =db.Column(db.Boolean, default=False)
    is_email_verified =db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    restaurants = db.relationship('TodoNotes', backref='writer', lazy=True)
    
class TodoNotes(BaseModel):
    __tablename__ = 'todo_notes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('todo_user.id'))
    note_title = db.Column(db.String(50),nullable=False)
    note_description = db.Column(db.String(250),nullable=True)
    status = db.Column(db.Enum('upcoming', 'completed', 'due',name="todo_status"))
    priority = db.Column(db.Enum('extreme', 'high', 'medium','low',name="todo_priority"))
    location = db.Column(pg.JSONB())
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    
class TodoCategories(BaseModel):
    __tablename__ = 'todo_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    image_url = db.Column(db.String(255),nullable=True)
    description = db.Column(db.String(356), nullable=True)
    