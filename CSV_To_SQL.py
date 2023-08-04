import pandas as pd

file_name = "/Users/josephdobos/Desktop/CV's/venue_data.xlsx"
df = pd.read_excel(file_name)
sql = ""

for _, row in df.iterrows():
    formatted_values = []
    for value in row:
        if isinstance(value, int):  # Check if the value is an integer
            formatted_values.append(str(value).strip())
        else:
            formatted_values.append("'{}'".format(str(value).strip()) if str(value).strip() != 'nan' else "''")

    sql += "INSERT INTO venues (`{}`) VALUES ({});\n".format("`, `".join(df.columns), ", ".join(formatted_values))

print(sql)
