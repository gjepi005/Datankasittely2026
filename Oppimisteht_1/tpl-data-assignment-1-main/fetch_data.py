import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Protected_Data
from config import DATABASE_URL, API_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def main():
    try:
        response = requests.get(API_URL)
        users = response.json()
        
        session = SessionLocal()
        for u in users:
            user = User(
                id=u["id"],
                name=u["name"],
                username=u["username"],
                email=u["email"],
                address=u["address"],
                phone=u["phone"],
                website=u["website"],
                company=u["company"]
            )
            session.merge(user)  # merge avoids duplicate key errors
                    
        session.commit()
        session.close()
        print("Users inserted into database.")
    except Exception as e:
        print(f"Problem while fetching user data {e}")


def save_Protected_Data(protected_data):
    try:
        session = SessionLocal()
        protected_data = json.loads(protected_data)
        for u in protected_data:
            Protected = Protected_Data(
                id=u["id"],
                name=u["name"],
                username=u["username"],
                email=u["email"],
                phone=u["phone"],
                website=u["website"],
            )
            session.merge(Protected)
            
        session.commit()
        session.close()
        print("Protected_Data inserted into database.")
    except Exception as e:
        print(f"Problem while saving protected data: {e}" )

if __name__ == "__main__":
    main()