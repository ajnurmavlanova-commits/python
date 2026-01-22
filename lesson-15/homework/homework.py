import sqlite3


conn = sqlite3.connect("roster.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert data into the table
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Benjamin Sisko", "Human", 40))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Jadzia Dax", "Trill", 300))
cursor.execute("INSERT INTO Roster VALUES (?, ?, ?)", ("Kira Nerys", "Bajoran", 29))

conn.commit()

# 3. Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = ?
WHERE Name = ?
""", ("Ezri Dax", "Jadzia Dax"))

conn.commit()

# 4. Display Name and Age of Bajoran species
cursor.execute("""
SELECT Name, Age
FROM Roster
WHERE Species = ?
""", ("Bajoran",))

results = cursor.fetchall()

print("Bajoran members:")
for name, age in results:
    print(f"Name: {name}, Age: {age}")


conn.close()
