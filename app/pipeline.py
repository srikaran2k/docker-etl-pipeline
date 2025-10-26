import pandas as pd
import sqlite3
import os

data_path = os.path.join('/data', 'raw_data.csv')
db_path = os.path.join('/data', 'cleaned_data.db')

def extract_data(path):
    df = pd.read_csv(path)
    print('✅ Extraction complete')
    return df

def transform_data(df):
    df = df.dropna()  # remove rows with missing values
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    print('✅ Transformation complete')
    return df

def load_data(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('people', conn, if_exists='replace', index=False)
    conn.close()
    print('✅ Load complete — data saved to SQLite')

def run_pipeline():
    df_raw = extract_data(data_path)
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned, db_path)
    print('🎉 ETL Pipeline executed successfully!')

if __name__ == '__main__':
    run_pipeline()
