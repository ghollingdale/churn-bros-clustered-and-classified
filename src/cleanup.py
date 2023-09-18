import pandas as pd


# Get dummies for column_name in df
def dummies(df, column_name):
    df = pd.get_dummies(df, columns = column_name)
    return df

# Delete a column from df
def drop_column(df, column):
    try:
        df = df.drop(columns=column)
    except:
        pass
    return df

# Save df
def save_csv(df, new_csv_path):
    df.to_csv(new_csv_path, index=False)
    return df

# Move a column to a posiiton in the df
def move_column(df, column_name, new_position):
    columns = df.columns.tolist()
    columns.remove(column_name)
    columns.insert(new_position, column_name)
    df = df[columns]
    return df