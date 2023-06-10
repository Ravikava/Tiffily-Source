from flask import request,jsonify
from apps import db
from apps.database.models import MenuItem,ReligiousPreference,TodoNotes
import json
from apps.helpers.send_otp import send_otp
from flask_jwt_extended import (
    jwt_required,get_jwt_identity
)
from sqlalchemy.sql import and_

def get_market_place():
    try:
        
        items = db.session.query(MenuItem).all()

        veg_items = []
        dal_items = []
        for item in items:
            if item.category.name == "Veg":  
                veg_items.append({
                    'id':item.id,
                    'veg': item.name,
                    'religious': ReligiousPreference.query.get(item.religious_preference).name if item.religious_preference else 'Regular'
                })

            if item.category.name == "Dal":  
                dal_items.append({
                    'id':item.id,
                    'dal': item.name,
                    'religious': ReligiousPreference.query.get(item.religious_preference).name if item.religious_preference else 'Regular'
                })
        
        todays_menu = {
                

                'veg': veg_items,
                'dal':dal_items,
                'roti':'butter roti',
                'rice': 'Basmati Rice',
                'salad': 'cucumber',
                'papad':'rosted_papad',
                'aachar':'mango'
            }
        
        response = jsonify({
                'status': 'SUCCESS',
                'code': 200,
                'message': 'Todays Menu',
                'data':todays_menu
            }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e}'
        }), 500
    return response


def todo_user_notes():
    try:
        todo_list = db.session.query(TodoNotes).filter(TodoNotes.user_id == 1).all()
        
        data = [
            {
                'id':i.id,
                'user_name':i.writer.name,
                'title':i.note_title,
                'description':i.note_description,
                'status':i.status,
                'priority':i.priority,
                'location':i.location,
                'created_at':i.created_at
            }for i in todo_list
        ]
        response = jsonify({
                    'status': 'SUCCESS',
                    'code': 200,
                    'message': 'TO-DO Notes',
                    'data':data
                }), 200
    except Exception as e:
        print(f"\n\n\n Error {e} \n\n\n")
        response = jsonify({
            'status': 'ERROR',
            'code': 910,
            'message': f'Error {e}'
        }), 500
    return response