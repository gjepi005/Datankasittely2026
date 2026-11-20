from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Player, Player_Stats
from config import DATABASE_URL, DATA_PATH

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def main():
    try:
        CSV_PATH = Path(__file__).resolve().parent / "goals.csv"
        df = pd.read_csv(CSV_PATH) 
        data = df.to_dict("records")
        session = SessionLocal()
        for u in data:
            player = Player(
                serial=u["serial"],
                player_name=u["player_name"],
                club=u["club"],
                position=u["position"],
                goals=u["goals"],
                right_foot=u["right_foot"],
                left_foot=u["left_foot"],
                headers=u["headers"],
                others=u["others"],
                inside_area=u["inside_area"]
            )
            session.merge(player)  # merge avoids duplicate key errors
            
        session.commit()
        session.close()
        print("Players inserted from csv into database.")
    except Exception as e:
        print(f"Problem while fetching user data {e}")


""" def save_Protected_Data(protected_data):
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
        print(f"Problem while saving protected data: {e}" ) """

if __name__ == "__main__":
    main()