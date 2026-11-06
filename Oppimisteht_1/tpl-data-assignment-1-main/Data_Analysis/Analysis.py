import pandas as pd


def shape(people):
    try:
        df = pd.DataFrame(people)
        print("________")
        return df.head(2)
    except Exception as e:
        print("Problem while shape analysis: " + {e})

def first_two(people):
    try:
        df = pd.DataFrame(people)
        print("________")
        return df.shape
    except Exception as e:
        print("Problem while first_two analysis: " + {e})

def last_two(people):
    try:
        df = pd.DataFrame(people)
        print("________")
        return df.tail(2)
    except Exception as e:
        print("Problem while last_two analysis: " + {e})    