# snowflake_connection.py
import pandas as pd
from sqlalchemy import create_engine

def get_data_from_snowflake():
    engine = create_engine(
        'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}'.format(
            account: FFKBEAW-NFB71515
            user: DBT_USER
            password: usmail1244
            role:  DBT_ROLE
            database: DBT_1
            warehouse: DBT_WHAREHOUSE
            schema: DBT_SCHEMA
            threads: 4

    )
    )

    query = "SELECT feature1, feature2, target FROM your_table;"
    df = pd.read_sql(query, engine)
    return df
