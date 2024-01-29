import sqlite3
import hashlib

# Define the database name
dbname = 'accounting.db'
connection = sqlite3.connect('./data/' + dbname)
cursor = connection.cursor()

# Function definition is a one-time process
def import_sql(dbname, sqlfile):
    try:
        # Read the SQL file
        with open('./data/' + sqlfile, 'r') as sql_file:
            # Read the entire content of the file
            sql_script = sql_file.read()

            # Execute the SQL script
            cursor.executescript(sql_script)

            cursor.execute('DELETE FROM users;')

            # Hash the password before insertion
            hashed_password = hashlib.sha256('aashishmali'.encode()).hexdigest()

            # Insert some data
            cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                           ('aashishmali', hashed_password, 'operator'))

            # Commit the changes
            connection.commit()
            print("SQL file imported successfully")

    except Exception as e:
        print(f"Error importing SQL file: {e}")

    finally:
        # Close the database connection
        connection.close()

# Function calling is a many-time process
import_sql(dbname, 'accounting.sql')  # Actual argument

def checkIfAdminRegister():
    try:
        pass
    except:
        pass
    else:
        pass
    finally:    
        pass

    return True
