import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Durgesh@12345",
    database="restaurantDB"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO orders(item_name, quantity, price, total_price)
VALUES ('Burger', 2, 120, 240)
""")

conn.commit()

print("Inserted:", cursor.rowcount)

cursor.close()
conn.close()