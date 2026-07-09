import os

files = [
    "01_import_data.py",
    "02_data_exploration.py",
    "03_data_cleaning.py",
    "04_category_analysis.py",
    "05_rating_analysis.py",
    "06_installs_analysis.py",
    "07_price_analysis.py",
    "08_sentiment_analysis.py"
]

for file in files:
    print(f"\nRunning {file}")
    os.system(f"python {file}")