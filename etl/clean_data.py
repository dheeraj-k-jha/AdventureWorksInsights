import pandas as pd


# helper function
def money_to_float(series):
    return (
        series
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )


# converting text to float for product
def clean_product(df):
    df["Standard Cost"] = money_to_float(df["Standard Cost"])
    return df


def clean_sales(df):
    df["Unit Price"] = money_to_float(df["Unit Price"])
    df["Sales"] = money_to_float(df["Sales"])
    df["Cost"] = money_to_float(df["Cost"])
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    return df


def clean_targets(df):
    df["Target"] = money_to_float(df["Target"])
    df["TargetMonth"] = pd.to_datetime(df["TargetMonth"])
    return df