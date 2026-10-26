from datetime import datetime
import pandas
"""
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """
    
def anonymize(people):
    print(people)
    try:
        df = pandas.DataFrame(people)
        df = df.drop("name", axis="columns")
        
        df['birth_year'] = pandas.to_datetime(df['birthdate']).dt.year
        df = df.drop("birthdate", axis="columns")

        df['city_initial'] = df['city'].str[:1]
        df = df.drop("city", axis="columns")

        print(df)
    except:
        print('ISO VIRHE: ' + df)

    return df.to_dict(orient="records")
    