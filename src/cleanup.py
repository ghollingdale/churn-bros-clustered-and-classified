import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Get dummies for a non-ordinal column_name in df
def dummies(df, column_name):
    column_name = [column_name]
    df = pd.get_dummies(df, columns=column_name)
    return df

# Encode an ordinal column_name in df
# hierarchy variable takes the list of unique column values of column_name in ascending order
def encode_ordinal(df, column_name, hierarchy):
    hierarchy = [hierarchy]
    encoder = OrdinalEncoder(categories=hierarchy)
    df[column_name] = encoder.fit_transform(df[[column_name]])
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

# Rename a column
def column_rename(df, old_column_name, new_column_name):
    df = df.rename(columns = {old_column_name:new_column_name})
    return df

# Replace boolean
def replace_boolean(df):
    df = df.replace({True: 1, False: 0})
    return df
