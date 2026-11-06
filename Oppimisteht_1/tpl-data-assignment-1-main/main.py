import pandas as pd
from DataProtection.masking import mask
from DataProtection.anonymization import anonymize
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import User
from Data_Analysis.Analysis import shape, first_two, last_two
from fetch_data import main as fetch_data
from fetch_data import save_Protected_Data
from config import DATABASE_URL
import json



def main():
    try:   
        #haetaan API avulla data
        fetch_data()

        #otetaan yhteys tietokantaan ja luodaan sessio
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        #otetaan data tietokannasta
        data = pd.read_sql_query(
        session.query(User).statement,
        session.bind
        )

        #original data
        print(data)

        #masking data
        print("MASKING")
        MaskData = mask(data)
        print(MaskData)
        
        #Masked + anonymized data
        print("ANONYMIZE")
        MaskAnonym = anonymize(MaskData)
        print(MaskAnonym)

        #Analysis
        print(shape(MaskAnonym))
        print(first_two(MaskAnonym))
        print(last_two(MaskAnonym))

        #tallennetaan suojattu data tietokantaan
        print("SAVING DATA")
        #Muutetaan json muotoon
        protected_json = MaskAnonym.to_json(orient="records")
        save_Protected_Data(protected_json)

        #suljetaan yhteys
        session.close()
        
    except Exception as e:
        print({e})

    #jos ajetaan suoraan koodi tämän avulla def main käynnistyy
if __name__ == "__main__":
    main()