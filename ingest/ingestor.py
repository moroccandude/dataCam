from snowflake import connector as snow
from dotenv import load_dotenv
import os
load_dotenv()
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
account=os.getenv("SNOWFLAKE_ACCOUNT")
user=os.getenv("SNOWFLAKE_USER")
password=os.getenv("SNOWFLAKE_PASSWORD")
database=os.getenv("SNOWFLAKE_DATABASE")
schema=os.getenv("SNOWFLAKE_SCHEMA")
warehouse=os.getenv("SNOWFLAKE_WAREHOUSE")

try:
    connection = snow.connect(
        account=account,
        user=user,
        password=password,
        database=database,
        schema=schema,
        warehouse=warehouse
    )
    logging.info("Connected to Snowflake successfully.")
except snow.errors.ProgrammingError as e:   
    print(f"Error connecting to Snowflake: {e}")
    exit(1)
except snow.errors.DatabaseError as e:
    print(f"Database error: {e}")
    exit(1)
except snow.errors.InternalError as e:
    print(f"Internal error: {e}")
except snow.errors.OperationalError as e:
    print(f"Operational error: {e}")