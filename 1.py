import psycopg2

# Establish connection to the database
conn = psycopg2.connect(
    host="lhost",
    database="sql",
    user="human",
    password="12345"
)

# Create a cursor object
cur = conn.cursor()

# Define the function to retrieve records by pattern
def get_records_by_pattern(pattern_text):
    cur.execute('SELECT * FROM your_table WHERE your_column ILIKE %s', (f'%{pattern_text}%',))
    records = cur.fetchall()
    return records

# Example usage
pattern = input("Name: ")
result = get_records_by_pattern(pattern)
print(result)

# Close cursor and connection
cur.close()
conn.close()
