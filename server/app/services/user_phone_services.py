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


    def get_phone_number(self, data):
        user_id = g.user_id
        search_query = data.get('search')


        # Modified query to include 'marked_as_spam' for the current user
        query = '''
            SELECT 
                user_phone_mapping.phone_no,
                user_phone_mapping.name,
                COUNT(phone_spam_mapping.phone_no) AS spam_count,
                (COUNT(phone_spam_mapping.phone_no) * 100.0 / (SELECT COUNT(DISTINCT user.id) FROM user)) AS spam_percentage,
                CASE
                    WHEN EXISTS (
                        SELECT 1 
                        FROM phone_spam_mapping 
                        WHERE phone_spam_mapping.phone_no = user_phone_mapping.phone_no
                        AND phone_spam_mapping.user_id = :user_id
                    )
                    THEN 1
                    ELSE 0
                END AS marked_as_spam
            FROM 
                user_phone_mapping
            LEFT JOIN 
                phone_spam_mapping
            ON 
                user_phone_mapping.phone_no = phone_spam_mapping.phone_no
            WHERE 
                user_phone_mapping.user_id = :user_id
        '''

        # If a search query is provided, add search condition
        if search_query:
            query += ''' AND (user_phone_mapping.phone_no LIKE :search_query OR user_phone_mapping.name LIKE :search_query)'''

        query += '''
            GROUP BY 
                user_phone_mapping.phone_no, user_phone_mapping.name;
        '''

        # Execute the query with parameters
        results = db.session.execute(
            text(query), 
            {"user_id": user_id, "search_query": f'%{search_query}%' if search_query else None}
        )
        
        keys = list(results.keys())
        data = results.fetchall()

        final_results = []
        for i in range(len(data)):
            temp_results = {}
            for j in range(len(keys)):
                temp_results[keys[j]] = data[i][j]
            final_results.append(temp_results)

        return True, "List Fetched Successfully", final_results

    
