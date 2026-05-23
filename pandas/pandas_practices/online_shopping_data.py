import pandas as pd
import numpy as np

ord = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer": ["Amit", "Sara", np.nan, "Riya", "Karan", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", np.nan, "Laptop", "Mobile"],
    "Price": [55000, 20000, np.nan, 15000, 60000, 22000],
    "Quantity": [1, 2, 1, np.nan, 1, 3],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", np.nan, "Mumbai"]
})

pay = pd.DataFrame({
    "OrderID": [1001, 1002, 1003, 1007],
    "PaymentMode": ["UPI", "Card", "Cash", "UPI"],
    "Status": ["Success", "Success", "Pending", "Success"]
})

print("ORDERS DATAFRAME")
print(ord)

# print("\nPAYMENTS DATAFRAME")
# print(payments)

print("Show first 4 rows")
print(ord.head(4))

print("Show only Customer, Product, Price")
print(ord[["Customer","Product","Price"]])

print("Find orders where Price > 20000")
print(ord[ord["Price"] > 20000])

print("Find orders from Mumbai")
print(ord[ord["City"] == "Mumbai"])

print("Find Laptop orders")
print(ord[ord["Product"] == "Laptop"])

print("Count missing values")
print(ord.isnull().sum())

print("Fill missing Price with average price")
ord['Price'] = ord['Price'].fillna(ord['Price'].mean())
print(ord)

print("Fill missing Quantity with average quantity")
ord['Quantity'] = ord['Quantity'].fillna(ord['Quantity'].mean())
print(ord)

print("Fill missing Customer with Unknown")
ord['Customer'] = ord['Customer'].fillna("Unknown")
print(ord)

print("Fill missing City with Unknown")
ord['City'] = ord['City'].fillna("Unknown")
print(ord)

print("Fill missing Product with Unknown")
ord['Product'] = ord['Product'].fillna("Unknown")
print(ord)

# print("Add new column Total")
# ord.insert(len(ord),"Total",[1000,1000,1000,1000,1000,1000])
# print(ord)

print("Calculate: Total = Price * Quantity")
ord["Total"] = ord["Quantity"] * ord["Price"]
print(ord)

print("Add one new order row")
ord.loc[len(ord)] = [1007,"vishal","Fidge","30000","2.0","Malegoan","60000.0"]
print(ord)

print("Update Amit price to 58000")
ord.loc[ord["Customer"] == 'Amit',"Price"] = 58000 
print(ord)

print("Replace Mumbai with Nagpur")
ord["City"] = ord["City"].replace("Mumbai","Nagpur",inplace=True)
print(ord)

# print("Remove City column")
# ord = ord.drop("City",axis=1)
# print(ord)

print("Remove row index 2")
ord = ord.drop(2)
print(ord)

ord['Price'] = pd.to_numeric(ord['Price'],errors="coerce")

print("Sort by Price ascending")
ord = ord.sort_values("Price")
print(ord)

print("Sort by Product and Price")
ord = ord.sort_values(["Product","Price"])
print(ord)

print("Find average price")
print(ord["Price"].mean())

print("Find average max")
print(ord["Price"].max())

print("Find product-wise average price")
print(ord.groupby("Product")["Price"].mean())

# print("Find product-wise total quantity")
# print(ord.groupby("Product")["Total"].sum())

# print("Find city-wise order count")
# print(ord.groupby("Product")["Total"].sum())

# print("Find city-wise order count")
# print(ord.groupby("City")["Product"].count())

print("Merge orders and payments")
df = pd.merge(ord,pay,on="OrderID",how="left")
print(df)

print("Find orders without payment details")
print(df.groupby("Product")["PaymentMode"].count())

print("Find customers whose names start with A")
print(df[df["Customer"].str.startswith("A")])

print("Find total sales amount")
print(df["Price"].sum())

df["Quantity"] = pd.to_numeric(df["Quantity"],errors="coerce")

print("Find highest quantity order")
print(df["Quantity"].max())

print("Find orders where quantity > 1 and price > 20000")
print(df[(df["Quantity"] > 1) & (df["Price"] > 20000)])

print("Find duplicate products ?")
print("Reset index after deleting rows ?")
print("Rename column Price to ProductPrice ?")
print("Check data types of all columns ?")
print("Convert Quantity column to integer type ?")
