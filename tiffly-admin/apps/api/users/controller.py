from flask import request,jsonify
from apps import db
from apps.database.models import User
from flask_jwt_extended import (
    create_access_token,create_refresh_token,
    jwt_required,get_jwt_identity
)
from apps.helpers.send_otp import send_otp
from sqlalchemy.sql import and_



def create_user():
    try:
        
        params = request.json
        
        try:
            user = db.session.query(User.id).filter(User.phone_number == params.get('phone_number')).first()

            auth_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            
            response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'User Logged In SuccessFully ...',
                'data':{
                    'token':auth_token,
                    'refresh_token':refresh_token,
                    'user_id':user.id,
                    'user_status':1
                    }
            }), 200
        except:
            user = User(
                phone_number=params.get('phone_number'),
                device_id=params.get('device_id'),
            )
            
            db.session.add(user)
            db.session.commit()
            auth_token = create_access_token(identity=user.id, fresh=True)
            
            refresh_token = create_refresh_token(user.id)
            
            response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'User Created SuccessFully ...',
                'data':{
                    'token':auth_token,
                    'refresh_token':refresh_token,
                    'user_id':user.id,
                    'user_status':0
                    }
            }), 200
        
        
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while creating user.'
        }), 500
    return response


@jwt_required()
def get_user():
    try:
        
        user_id = get_jwt_identity()
        
        user = db.session.query(User).filter(User.id == user_id).first()

        data = {
                'id':user.id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'phone_number':user.phone_number,
                'email':user.email,
                'dob':user.dob,
                'special_day':user.special_day,
                'gender':user.gender,
                'is_mobile_verified':user.is_mobile_verified,
                'is_email_verified':user.is_email_verified,
                'is_active':user.is_active,
                'device_id':user.device_id,
                'created_at':str(user.created_at),
            }
        
        
        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Get All Users',
                'data':data
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while Getting user.'
        }), 500
    return response


@jwt_required()
def profile_update():
    try:
        user_id = get_jwt_identity()
        
        user = db.session.query(User).filter(User.id == user_id).first()
        
        print(user.first_name)
        
        params = request.json
        
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        email = params.get('email')
        dob = params.get('dob')
        special_day = params.get('special_day')
        profile_image = params.get('profile_image')
        background_image = params.get('background_image')
        gender = params.get('gender')
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.dob = dob if not user.dob else user.dob
        user.special_day = special_day if not user.special_day else user.special_day
        user.profile_image = profile_image
        user.background_image = background_image
        user.gender = gender if not user.gender else user.gender
        
        db.session.commit()
        
        response = jsonify({
                    'status': 'SUCCESS',
                    'code': 200,
                    'message': 'Profile Update SuccessFully..',
                    
                }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while Update Profile.'
        }), 500
    return response

@jwt_required
def authenticate_user():
    try:
        user_id = get_jwt_identity()
        
        user = db.session.query(User).filter(User.id == user_id).first()

        params = request.json
        
        if params.get('phone_number'):
            user.phone_number = params.get('phone_number')
            user.is_mobile_verified = True
            db.session.commit()
            
            response = jsonify({
                            'status': 'SUCCESS',
                            'code': 200,
                            'message': 'Mobile Number Has Been Changed',
                        }), 200
        
        if params.get('email'):
            user.email = params.get('email'),
            user.is_email_verified = True
            db.session.commit()
            
            response = jsonify({
                        'status': 'SUCCESS',
                        'code': 200,
                        'message': 'Email Has Been Changed',
                        
                    }), 200
            
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e} while Update Profile.'
        }), 500
    return response
