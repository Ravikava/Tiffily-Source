from flask import request,jsonify
from apps import db
from apps.database.models import User,Restaurant
import json
from apps.helpers.send_otp import send_otp
from flask_jwt_extended import (
    jwt_required,get_jwt_identity
)

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
                'phone_number':i.phone_number,
                'address':i.address,
                'location':json.loads(i.location),
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