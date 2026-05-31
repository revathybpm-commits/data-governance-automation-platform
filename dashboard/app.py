import streamlit as st
import sqlite3
import pandas as pd
import os
import networkx as nx

# Path to DB
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "governance.db")

st.title("📊 Data Governance Platform")

# Connect DB
conn = sqlite3.connect(DB_PATH)

# -----------------------
# Refresh Button
# -----------------------
if st.button("🔄 Refresh Data"):
    st.rerun()

# Load metadata
st.header("Data Catalog (Metadata)")

df = pd.read_sql("SELECT * FROM metadata", conn)
st.dataframe(df)

# Load defects (if exists)
st.header("Data Quality Defects")

try:
    df2 = pd.read_sql("SELECT * FROM defects", conn)
    st.dataframe(df2)
except:
    st.write("No defects generated yet")

# -----------------------
# LINEAGE GRAPH
# -----------------------


st.header("🔗 Data Lineage")

lineage_df = pd.read_sql("SELECT * FROM lineage", conn)

G = nx.DiGraph()

for _, row in lineage_df.iterrows():
    G.add_edge(row["source"], row["target"])

# Convert to Graphviz format (clean visualization)
graph_str = "digraph G {\n"

for source, target in G.edges():
    graph_str += f'  "{source}" -> "{target}";\n'

graph_str += "}"

st.graphviz_chart(graph_str)

conn.close()
