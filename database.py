import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    import pyexasol

    dsn = os.getenv("EXASOL_DSN")
    user = os.getenv("EXASOL_USER")
    password = os.getenv("EXASOL_PASSWORD")

    if not all([dsn, user, password]):
        return None

    return pyexasol.connect(
        dsn=dsn,
        user=user,
        password=password,
        encryption=True,
    )


def load_data():
    """
    Load data from Exasol when configured.
    Otherwise use local demo data.
    """

    conn = get_connection()

    if conn is not None:
        query = """
        SELECT *
        FROM NEXORA.SALES
        """

        return conn.export_to_pandas(query)

    # Demo fallback
    return pd.DataFrame({
        "month": [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun"
        ],
        "revenue": [
            125000, 132000, 141000, 138000, 119000, 108000
        ],
        "orders": [
            1200, 1260, 1340, 1290, 1150, 1020
        ],
        "customers": [
            980, 1020, 1080, 1050, 960, 910
        ],
        "marketing_spend": [
            18000, 19000, 21000, 20500, 17000, 16000
        ]
    })
    