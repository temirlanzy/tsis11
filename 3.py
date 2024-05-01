import psycopg2

# Establish connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="JusticeForSaltanat"
)

cur = conn.cursor()

# Function to call the stored procedure
def insert_users(users_data):
    cur.execute('CALL insert_users(%s)', (users_data,))

# Example usage
users_data = []
while True:
    user_input = input("Enter user's name and phone number(John Doe,123456789) ")
    if user_input.lower() == 'done':
        break
    users_data.append(user_input)
insert_users(users_data)

# Commit and close connections
conn.commit()
cur.close()
conn.close()