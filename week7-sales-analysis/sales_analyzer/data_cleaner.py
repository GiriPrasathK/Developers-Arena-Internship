import pandas as pd
import warnings

def clean_data(df):
    df = df.drop_duplicates()

    # ---- Date ----
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # ---- Numeric columns ----
    df["Quantity"] = df["Quantity"].fillna(0).astype(int)
    df["Price"] = df["Price"].fillna(0)
    df["Total Sales"] = df["Total Sales"].fillna(0)

    # ---- Month feature ----
    df["Month"] = df["Date"].dt.to_period("M")

    return df
