import pandas as pd
df = pd.read_excel(Users/jonathanwamarema/Downloads/Test_Files.xlsx)
def generate_email(row):
    first_name = row['First_Name'].split()[0]
    last_name = row['Last_Name'].split()[0]
    return f"{first_name.lower()}{last_name.lower()}@gmail.com"
df['Email'] = df.apply(generate_email, axis=1)