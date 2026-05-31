import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "governance.db")

df = pd.read_csv(os.path.join(BASE_DIR, "data", "customer.csv"))

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS defects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset TEXT,
    rule_name TEXT,
    failure_count INTEGER,
    status TEXT
)
""")

# RULE 1: missing email
missing_email = df["email"].isnull().sum()

if missing_email > 0:
    cursor.execute("""
    INSERT INTO defects (dataset, rule_name, failure_count, status)
    VALUES (?, ?, ?, ?)
    """, ("customer", "email_not_null", missing_email, "OPEN"))

conn.commit()
conn.close()

print("Quality check completed")
