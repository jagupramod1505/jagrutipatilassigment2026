from dotenv import load_dotenv
import os
import snowflake.connector

# Load .env from project root
load_dotenv()

print("USER     =", os.getenv("SNOWFLAKE_USER"))
print("ACCOUNT  =", os.getenv("SNOWFLAKE_ACCOUNT"))
print("PASSWORD SET =", bool(os.getenv("SNOWFLAKE_PASSWORD")))

try:
   
    conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account="VB30931.ap-south-1.aws"
)


    cur = conn.cursor()
    cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE()")
    print("CONNECTED:", cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("Connection failed:")
    print(e)

