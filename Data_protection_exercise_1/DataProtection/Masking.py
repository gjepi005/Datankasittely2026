import pandas
def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    
    df = pandas.DataFrame(people)
    df["email"] = df["email"].str.replace(r"[^@](?=[^@]*@)", "*", regex=True)
    df["phone"] = df["phone"].str.replace(r"\d(?=.*\d{2}$)", "*", regex=True)
    print(df)
    
    return df.to_dict(orient="records")