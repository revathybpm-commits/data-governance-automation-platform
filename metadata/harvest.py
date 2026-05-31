import pandas as pd
import sqlite3
import os

# Get project root folder safely
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Database path (always correct)
DB_PATH = os.path.join(BASE_DIR, "database", "governance.db")

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create metadata table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS metadata (
    table_name TEXT,
    column_name TEXT,
    data_type TEXT,
    null_count INTEGER
)
""")

# Load dataset
df = pd.read_csv(os.path.join(BASE_DIR, "data", "customer.csv"))

# Extract metadata
for col in df.columns:
    cursor.execute("""
    INSERT INTO metadata VALUES (?, ?, ?, ?)
    """, (
        "customer",
        col,
        str(df[col].dtype),
        int(df[col].isnull().sum())
    ))

conn.commit()
conn.close()

print("Metadata harvested successfully")
