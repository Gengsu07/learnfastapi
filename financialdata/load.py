import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:sgwi2341@localhost/financial_data")

dfi = pd.read_csv(
    r"/Users/sugengw07/Downloads/ANZ.csv",
    dtype={
        "status": "string",
        "card_present_flag": "string",
        "bpay_biller_code": "string",
        "account": "string",
        "currency": "string",
        "long_lat": "string",
        "txn_description": "string",
        "merchant_id": "string",
        "merchant_code": "float",
        "first_name": "string",
        "balance": "float",
        "date": "string",
        "gender": "string",
        "age": "int8",
        "merchant_suburb": "string",
        "merchant_state": "string",
        "extraction": "string",
        "amount": "float",
        "transaction_id": "string",
        "country": "string",
        "customer_id": "string",
        "merchant_long_lat": "string",
        "movement": "string",
    },
)
dfi = dfi.replace([np.inf, -np.inf], np.nan)
df2 = dfi.replace(np.nan, "", regex=True)
df2 = df2.rename(columns={"date": "transaction_date"})
df2 = df2.rename(columns={"extraction": "extraction_timestamp"})
df2 = df2.rename(columns={"amount": "transaction_amount"})
df2["merchant_code"] = df2["merchant_code"].replace("", 0.0)
# Insert the data to the database using to_sql method.
df2.to_sql(name="financial_data", con=engine, index=False, if_exists="replace")
