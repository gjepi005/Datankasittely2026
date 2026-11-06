import pandas
def mask(people):
    try:
        df = pandas.DataFrame(people)
        df["name"] = df["name"].str.replace(r"(?<=.).", "*", regex=True)
        df["email"] = df["email"].str.replace(r"[^@](?=[^@]*@)", "*", regex=True)
        df["phone"] = df["phone"].str.replace(r"\d(?=.*\d{2}$)", "*", regex=True)
        print(df)
        
        return df
    except Exception as e:
        print(f"Masking error: {e}")