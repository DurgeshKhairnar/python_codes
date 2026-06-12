import pandas as pd
import numpy as np

df = pd.DataFrame({

    "OrderID": [
        1001,1002,1003,1004,1005,
        1006,1007,1008,1009,1010,
        1011,1012,1013,1014,1015
    ],

    "CustomerName": [
        "Amit Kumar",
        "Sara_123",
        np.nan,
        "Riya Sharma",
        "John@Doe",
        "Neha99",
        "Vikas",
        "Ankit#",
        "Pooja",
        "Rahul123",
        "Priya",
        "Karan$",
        "Amit Kumar",
        "Sneha",
        "Rohit"
    ],

    "Email": [
        "amit@gmail.com",
        "sara@yahoo.com",
        "wrong_email",
        "riya@gmail.com",
        np.nan,
        "neha123@gmail.com",
        "vikas@outlook",
        "ankit#gmail.com",
        "pooja@gmail.com",
        "rahul@yahoo.in",
        "priya@gmail.com",
        "karan$gmail.com",
        "amit@gmail.com",
        "sneha@gmail",
        "rohit@gmail.com"
    ],

    "Phone": [
        "9876543210",
        "9123456780",
        "12345",
        np.nan,
        "8888888888",
        "98765abcd0",
        "9999999999",
        "777777777",
        "88888@8888",
        "9876540000",
        "9988776655",
        "11111abcde",
        "9876543210",
        "999999999",
        "9876501234"
    ],

    "Product": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Headphone",
        np.nan,
        "Laptop",
        "Mobile",
        "Tablet",
        "Laptop",
        "Headphone",
        "Mobile",
        "Laptop",
        "Tablet",
        "Headphone"
    ],

    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories",
        "Electronics",
        "Electronics",
        "Electronics",
        "Accessories"
    ],

    "Price": [
        55000,
        20000,
        np.nan,
        60000,
        2500,
        -500,
        58000,
        22000,
        15000,
        999999,
        3000,
        21000,
        55000,
        16000,
        3500
    ],

    "Quantity": [
        1,
        2,
        1,
        np.nan,
        3,
        2,
        1,
        2,
        1,
        1,
        4,
        2,
        1,
        1,
        3
    ],

    "City": [
        "Pune",
        "Mumbai123",
        "Delhi",
        "Nagpur@",
        np.nan,
        "Chennai",
        "Pune",
        "Mumbai",
        "Delhi1",
        "Hyd#",
        "Pune",
        "Bangalore@",
        "Pune",
        "Delhi",
        "Mumbai"
    ],

    "PaymentMode": [
        "UPI",
        "Card",
        "Cash",
        "UPI",
        "Card",
        "Cash",
        np.nan,
        "UPI",
        "Card",
        "UPI",
        "Cash",
        "Card",
        "UPI",
        "Cash",
        "Card"
    ],

    "OrderDate": [
        "2024-01-10",
        "2024-01-12",
        "2024-02-01",
        "2024-02-15",
        "2024-03-05",
        "2024-03-10",
        "2024-04-01",
        "2024-04-15",
        "2024-05-01",
        "2024-05-20",
        "2024-06-10",
        "2024-06-15",
        "2024-07-01",
        "2024-07-10",
        "2024-08-01"
    ]
})

print(df)

pd.set_option("display.float_format", "{:.2f}".format)

print("Count missing values.")
print(df.isnull().sum())

print("Fill missing CustomerName with Unknown")
df["CustomerName"] = df["CustomerName"].fillna("Unknown")
print(df["CustomerName"])

print("Fill missing Product with mode.")
df["Product"] = df["Product"].ffill()
print(df["Product"])

print("Fill missing Price with mean.")
df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df["Price"])

print("Fill missing Quantity with median.")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
print(df["Quantity"])

print("Fill missing PaymentMode with mode.")
df["PaymentMode"] = df["PaymentMode"].fillna(df["PaymentMode"].mode())
print(df["PaymentMode"])

print("Remove duplicate rows.")
df.drop_duplicates()


print("Find customers containing numbers.")
print(df[df["CustomerName"].str.contains(r"\d",regex=True)])

print("Find customers containing special characters")
print(df[df["CustomerName"].str.contains(r"[^a-zA-Z0-9 ]",regex=True)])

print("Find valid emails.")
print(df[df["Email"].str.contains(r"^[\w\.-]+@[\w\.-]+\.\w+$",regex=True)])

print("Find Invalid emails.")
print(df[~df["Email"].str.contains(r"^[\w\.-]+@[\w\.-]+\.\w+$",regex=True)])

print("Find valid phone numbers.")
print(df[df["Phone"].str.contains(r"\d{10}$",regex=True)])

print("Find Invalid phone numbers.")
print(df[~df["Phone"].str.contains(r"\d{10}$",regex=True)])


print("Find cities containing numbers.")
print(df[df["City"].str.contains(r"\d",regex=True)])

print("Find cities containing special characters.")
print(df[df["City"].str.contains(r"[^a-zA-Z0-9 ]",regex=True)])

print("Remove special characters from CustomerName.")
df["CustomerName"] = df["CustomerName"].str.replace(r"[^a-zA-Z0-9 ]","",regex=True)
print(df["CustomerName"])

print("Remove numbers from City.")
df["City"] = df["City"].str.replace(r"\d","",regex=True)
print(df["City"])

print("Remove special characters from City.")
df["City"] = df["City"].str.replace(r"[^a-zA-Z0-9 ]","",regex=True)
print(df["City"])

print("Remove special characters from City.")
df["CustomerName"] = df["CustomerName"].str.title()
print(df["CustomerName"])

print("Total = Price * Quantity")
df["Total"] = df["Price"] * df["Quantity"]
print(df["Total"])

print("GST = Total * 0.18")
df["GST"] = df["Total"] * 0.18
print(df["GST"])

print("FinalAmount = Total + GST")
df["FinalAmount"] = df["Total"] + df["GST"]
print(df["FinalAmount"])

print("Orders with Total > 50000.")
print(df[df["Total"] > 50000])

print("Orders from Pune.")
print(df[df["City"] == "Pune"])

print("Laptop orders.")
print(df[df["Product"] == "Laptop"])


print("Electronics products only..")
print(df[df["Category"] == "Electronics"])

print("Orders paid via UPI.")
print(df[df["PaymentMode"] == "UPI"])

print("Orders where Quantity > 2.")
print(df[df["Quantity"] > 2])

print("Sort by Price ascending.")
print(df.sort_values("Price"))

print("Sort by Price descending.")
print(df.sort_values("Price",ascending=False))

print("Sort by Category and Price.")
print(df.sort_values(["Category","Price"],ascending=False))

print("Average price category-wise.")
print(df.groupby("Category")["Price"].mean())

print("Total sales category-wise.")
print(df.groupby("Category")["Total"].sum())

print("Total quantity sold product-wise.")
print(df.groupby("Product")["Quantity"].sum())

print("Order count city-wise.")
print(df.groupby("City")["OrderID"].count())

print("Order count city-wise.")
print(df.groupby("City")["Price"].mean())

print("Maximum order value product-wise.")
print(df.groupby("City")["Price"].max())

# print(df.columns)