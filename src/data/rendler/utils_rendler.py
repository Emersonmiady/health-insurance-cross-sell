import pandas as pd
from sqlalchemy import create_engine

def upload_data(creds, df, table_name):
    """
    Uploads a DataFrame to a PostgreSQL database table using the given credentials.

    Args:
        creds (dict): A dictionary containing the following keys:
            - PG_DB (str): The name of the database.
            - PG_USER (str): The username for the database.
            - PG_HOST (str): The hostname of the database.
            - PG_PSWD (str): The password for the database.
        df (pandas.DataFrame): The DataFrame to be uploaded.
        table_name (str): The name of the table in the database.

    Returns:
        None

    Raises:
        None

    Notes:
        This function uses the `sqlalchemy` library to connect to the database and execute the query.
        The connection is closed after the query is executed.
    """
    string_con = f"postgresql://{creds['PG_USER']}:{creds['PG_PSWD']}@{creds['PG_HOST']}/{creds['PG_DB']}"
    engine = create_engine(string_con)
    con = engine.connect()

    # Uppercase column names
    df.columns = [k.upper() for k in df.columns]

    df.to_sql(table_name, con=con, if_exists='replace', index=False)

    con.close()
    engine.dispose()

def get_data(creds, query):
    """
    Connects to a PostgreSQL database using the given credentials and executes the given SQL query.

    Args:
        creds (dict): A dictionary containing the following keys:
            - PG_DB (str): The name of the database.
            - PG_USER (str): The username for the database.
            - PG_HOST (str): The hostname of the database.
            - PG_PSWD (str): The password for the database.
        query (str): The SQL query to be executed.

    Returns:
        pandas.DataFrame: A DataFrame containing the results of the query.

    Raises:
        None

    Notes:
        This function uses the `sqlalchemy` library to connect to the database and execute the query.
        The connection is closed after the query is executed.
    """
    
    # Connect to the database
    string_con = f"postgresql://{creds['PG_USER']}:{creds['PG_PSWD']}@{creds['PG_HOST']}/{creds['PG_DB']}"
    engine = create_engine(string_con)
    conn = engine.connect()

    # Get data
    df = pd.read_sql(query, conn)

    # Close connection
    conn.close()
    engine.dispose()

    return df