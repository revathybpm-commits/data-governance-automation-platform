pip install -r requirements.txt

# Run metadata extraction
python3 metadata/harvest.py

# Run quality checks
python3 quality/quality_engine.py

# Launch dashboard
streamlit run dashboard/app.py
📸 Screenshots
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/8f49c286-8029-4947-92d4-a9003ea5bdeb" />
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5e2fc3c2-319c-481e-893a-8e8758931138" />


🎯 Use Case
This project simulates enterprise tools like:
Collibra (data governance)
Alation (catalog)
DataHub (lineage)
Great Expectations (data quality)
👨‍💻 Author
Revathy
