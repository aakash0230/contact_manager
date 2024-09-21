from app.model import UserPhoneMapping
from app import db
from flask import g
from sqlalchemy import text
class UserPhoneService:
    def add_phone_number(self, data):
        print(data)
        user_id = g.user_id
        phone_number = data.get('phone_number')
        name = data.get("name")

        if user_id and phone_number and name:
            is_phone_exists = db.session.query(UserPhoneMapping).filter(UserPhoneMapping.user_id == user_id, UserPhoneMapping.phone_no == phone_number).first()
            if is_phone_exists:
                return False, "Phone number already exists", {}
            users_contact = UserPhoneMapping(
                user_id=user_id,
                phone_no=phone_number, 
                name=name
            )
            users_contact.save()
                
            return True, "Contact Added Successfully", {"user_id" : user_id, "phone_number" : phone_number, "name" : name}
        else:
            return False, "Invalid Data", {}
        
    def get_phone_number(self):
        user_id = g.user_id
        query = text('''
            SELECT 
                user_phone_mapping.phone_no,
                user_phone_mapping.name,
                COUNT(phone_spam_mapping.phone_no) AS spam_count,
                (COUNT(phone_spam_mapping.phone_no) * 100.0 / (SELECT COUNT(DISTINCT user.id) FROM user)) AS spam_percentage
            FROM 
                user_phone_mapping
            LEFT JOIN 
                phone_spam_mapping
                ON user_phone_mapping.phone_no = phone_spam_mapping.phone_no
            WHERE 
                user_phone_mapping.user_id = :user_id
            GROUP BY 
                user_phone_mapping.phone_no, user_phone_mapping.name;

        ''')

        results = db.session.execute(query, {"user_id" : user_id})
        keys = list(results.keys())
        data = results.fetchall()

        final_results = []
        for i in range(0, len(data)):
            temp_results = {}
            for j in range(0, len(keys)):
                temp_results[keys[j]] = data[i][j]
            final_results.append(temp_results)
        return True, "List Fetched Successfully", final_results
    
