import sqlite3

# Connect to database
# conn = sqlite3.connect('estateguru_projects.db')

# Create a cursor
# c = conn.cursor()

"""Create a table"""
# if c.execute("""CREATE TABLE estateguru_est (
#     id TEXT NOT NULL PRIMARY KEY,
#     url TEXT NOT NULL
# )"""):
#     print("Table created successfully...")

"""Special table for Government backed investments"""
# c.execute("""CREATE TABLE estateguru_special (
#     id INTEGER(11) NOT NULL PRIMARY KEY AUTO INCREMENT,
#     code VARCHAR(12) NOT NULL,
#     url VARCHAR(100) NOT NULL,
#     interest DECIMAL(3,2) NOT NULL,
#     loan_period VARCHAR(20) NOT NULL
# )""")

"""Insert data to a table"""
# if c.execute("INSERT INTO estateguru_est VALUES ('', '') "):
#     print("Data inserted to table successfully...")

"""Insert multiple values to a table"""
# many_values = [
#                 ('id', 'url'),
#                 ('id', 'url'),
#                 ('id', 'url'),
#               ]
# if c.executemany("INSERT INTO estateguru_est VALUES (?, ?)", many_values):
#     print("Inserted multiple values successfully...")

"""Query the database"""
# c.execute("SELECT * FROM estateguru_est")
# c.fetchone()
# c.fetchmany(3)
# c.fetchall()

# items = c.fetchall()
# for key, value in items:
#     print(key, value)

# for item in items:
#     print(item[0])

# Commit our command/changes
# conn.commit()

# Close the connection
# conn.close()

# Functions

def show_all():
    id_codes = []
    # Connect to database
    conn = sqlite3.connect('estateguru_projects.db')
    # Create a cursor
    c = conn.cursor()
    c.execute("SELECT * FROM estateguru_est")
    items = c.fetchall()
    for item in items:
        id_codes.append(item[0])
    conn.commit()
    conn.close()
    return id_codes

def add_one(id, url):
    # Connect to database
    conn = sqlite3.connect('estateguru_projects.db')
    # Create a cursor
    c = conn.cursor()
    if c.execute("INSERT INTO estateguru_est VALUES (?, ?)", (id, url)):
        print("Data inserted to database successfully...")
    conn.commit()
    conn.close()

