from flask import request,jsonify
from apps import db
from apps.database.models import (
    User,Restaurant,MenuItem,
    MenuItemCategory,ReligiousPreference
    )
import json
from apps.helpers.send_otp import send_otp
from flask_jwt_extended import (
    jwt_required,get_jwt_identity
)
from apps.helpers.utils import get_or_create

def testing():
    return {"hello" : "world"}

@jwt_required()
def create_restaurant():
    """ this function will be use for create a restaurant """
    try:
        # get current user id 
        owner_id = get_jwt_identity() 
        
        params = request.json
        
            
        restaurant = Restaurant(
            owner_id=owner_id,
            restaurant_name=params.get('restaurant_name'),
            cuisines=params.get('cuisines'),
        )
        
        db.session.add(restaurant)
        db.session.commit()
        
        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Restaurant Data Created SuccessFully ...',
                'data':''
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating Restaurant Data.'
        }), 500
    return response

@jwt_required()
def get_all_restaurant():
    """ this function will be use for Get a current restaurant User / Owner """
    
    try:
        # send_otp()
        restaurant = db.session.query(Restaurant).all()
        
        restaurant_list = [
            {
                'id':i.id,
                'owner':{
                        'id': i.owner.id,
                        'first_name': i.owner.first_name,
                        'last_name': i.owner.last_name,
                        'phone_number': i.owner.phone_number,
                        'email': i.owner.email,
                        'is_active': i.owner.is_active,
                        'device_id': i.owner.device_id,
                        'created_at': i.owner.created_at
                    },
                'restaurant_name':i.restaurant_name,
                'is_active':i.is_active,
                'created_at':i.created_at,
            }for i in restaurant
        ]
        
        print(restaurant_list)

        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Restaurant Data Created SuccessFully ...',
                'data':restaurant_list
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating Restaurant Data.'
        }), 500
    return response

@jwt_required()
def get_menu_item():
    try:
        owner_id = get_jwt_identity() 
        restaurant_id = db.session.query(Restaurant.id).filter(Restaurant.owner_id == owner_id).first()
        id = request.args.get('id')
        if id:
            menu_items = db.session.query(MenuItem).filter(
                MenuItem.restaurant_id == restaurant_id.id,
                MenuItem.id == id).first()
            
            category = db.session.query(MenuItemCategory.name).filter(
                MenuItemCategory.id == menu_items.category_id
                ).first()
            
            religious_preference = db.session.query(ReligiousPreference.name).filter(
                ReligiousPreference.id == menu_items.religious_preference
                ).first()
            data = {
                "id":menu_items.id,
                "category":category.name,
                "religious_preference":religious_preference.name,
                "name":menu_items.name,
                "price":menu_items.price,
                "is_available":menu_items.is_available,
            }
        else:
            data = []
            menu_items = db.session.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id.id).all()

            for i in menu_items:
            
                category = db.session.query(MenuItemCategory.name).filter(
                    MenuItemCategory.id == i.category_id
                    ).first()
                
                religious_preference = db.session.query(ReligiousPreference.name).filter(
                    ReligiousPreference.id == i.religious_preference
                    ).first()
            
                data.append({
                    "id":i.id,
                    "restaurant_id":i.restaurant_id,
                    "category":category.name,
                    "religious_preference":religious_preference.name,
                    "name":i.name,
                    "price":i.price,
                    "is_available":i.is_available,
                })
        
        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Get Menu Item',
                'data':data
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating Restaurant Data.'
        }), 500
    return response


@jwt_required()
def add_menu_item():
    """ this function will be use for create a menu item """
    try:
        # get current user id 
        owner_id = get_jwt_identity() 
        restaurant_id = db.session.query(Restaurant.id).filter(Restaurant.owner_id == owner_id).first()
        
        params = request.json

        religious_preference = params.get('religious_preference')

        religious_preference = db.session.query(ReligiousPreference.id).filter(ReligiousPreference.name == religious_preference).first()

        menu_item,created = get_or_create(
            db.session,
            MenuItem,
            restaurant_id=restaurant_id.id,
            category_id=params.get('category_id'),
            religious_preference=religious_preference.id,
            name=params.get('name'),
            price=params.get('price'),
            is_available=params.get('is_available'),
        ) 
        db.session.commit()
        
        
        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Menu Item Created SuccessFully ...',
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating Restaurant Data.'
        }), 500
    return response


@jwt_required()
def edit_menu_item():
    try:
        id = request.args.get('id')
        params = request.json
        
        owner_id = get_jwt_identity() 
        
        restaurant_id = db.session.query(Restaurant.id).filter(Restaurant.owner_id == owner_id).first()

        menu_items = db.session.query(MenuItem).filter(
            MenuItem.restaurant_id == restaurant_id.id,
            MenuItem.id == id).first()
        
        category = db.session.query(MenuItemCategory.name).filter(
            MenuItemCategory.id == menu_items.category_id
            ).first()
        
        religious_preference = db.session.query(ReligiousPreference.name).filter(
            ReligiousPreference.id == menu_items.religious_preference
            ).first()
        
        if request.method == 'POST':
            religious_preference = params.get('religious_preference')

            religious_preference = db.session.query(ReligiousPreference.id).filter(ReligiousPreference.name == religious_preference).first()

            menu_items.category_id = params.get('category_id')
            menu_items.religious_preference =religious_preference.id
            menu_items.name = params.get('name')
            menu_items.price = params.get('price')
            menu_items.is_available = params.get('is_available')
        
            db.session.commit()
            
            response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Menu Item Updated SuccessFully ...',
            }), 200
        else:    
            data = {
                "id":menu_items.id,
                "category":category.name,
                "religious_preference":religious_preference.name,
                "name":menu_items.name,
                "price":menu_items.price,
                "is_available":menu_items.is_available,
            }
            
            response = jsonify({
                    'status': 'SUCCESS',
                    'code': 200,
                    'message': 'Get Menu Item ...',
                    'data':data
                }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating Restaurant Data.'
        }), 500
    return response


@jwt_required()
def delete_menu_item(id):
    try:
        item = db.session.query(MenuItem).filter(MenuItem.id == id).first()

        db.session.delete(item)
        
        response = jsonify({
                    'status': 'SUCCESS',
                    'code': 200,
                    'message': 'Item Deleted SuccessFully ...',
                    
                }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': 'Menu Item Not Found.'
        }), 500
    return response
        

