import pandas

def anonymize(people):
    try:
        print(people)
        df = pandas.DataFrame(people)
        df = df.drop("address", axis="columns")
        df = df.drop("company", axis="columns")
    except Exception as e:
        print("Anonymize error: " + {e})

    return df