import pandas as pd


file_name = ""
df = pd.read_excel(file_name)
sql = ""

for _, row in df.iterrows():

    formatted_values = ["'{}'".format(str(value).strip()) if str(value).strip() != 'nan' else "''" for value in row]
    
    sql += "INSERT INTO venues (`{}`) VALUES ({});\n".format("`, `".join(df.columns), ", ".join(formatted_values))

print(sql)
