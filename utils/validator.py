import pandas as pd

def load_data(filePath):
    
    df=pd.read_csv(filePath)
    if len(df.columns) == 1:

        column_name = df.columns[0]

        rows = [column_name] + df[column_name].tolist()

        split_rows = [row.split(",") for row in rows]

        header = split_rows[0]
        data = split_rows[1:]

        df = pd.DataFrame(data, columns=header)

    return df
  
def validate_data(df):
    if df.empty:
        raise ValueError("Dataset is empty!")
    
    if 'close'  not in df.columns:
        raise ValueError("close column not present in dataset!")
    df["close"] = pd.to_numeric(df["close"])
    return df