import sqlite3
import hashlib

# Function definition is a one-time process
def import_sql(dbname, sqlfile):
    # Step 1: Open a database
    connection = sqlite3.connect('./data/' + dbname)
    cursor = connection.cursor()
    
    try:
        # Read the SQL file
        with open('./data/' + sqlfile, 'r') as sql_file:
            # Read the entire content of the file
            sql_script = sql_file.read()

            # Execute the SQL script
            cursor.executescript(sql_script)

            # Hash the password before insertion
            hashed_password = hashlib.sha256('009988'.encode()).hexdigest()

            # Insert some data
            cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                           ('rohit', hashed_password, 'operator'))

            # Commit the changes
            connection.commit()
            print("SQL file imported successfully")

    except Exception as e:
        print(f"Error importing SQL file: {e}")

    finally:
        # Close the database connection
        connection.close()

# Function calling is a many-time process
import_sql('accounting.db', 'accounting.sql')  # Actual argument
