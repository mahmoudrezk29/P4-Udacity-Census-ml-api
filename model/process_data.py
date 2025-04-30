import pandas as pd
import sys

def clean_census_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    # Remove whitespace in column names and string values
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    clean_census_data(input_path, output_path)
