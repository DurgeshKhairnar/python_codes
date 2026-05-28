print("Convert Name column to uppercase")
df["Name"] = df['Name'].str.upper()
print(df)