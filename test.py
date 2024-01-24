import sqlite3

#1 function defination is one time process
def import_sql(dbname,sqlfile): #formal argument
    #step 1 open a database
    connection = sqlite3.connect('./data/'+dbname)
    cursor = connection.cursor()
    try:
        # Read the SQL file
        with open('./data/'+sqlfile, 'r') as sqlfile:
            # Read the entire content of the file
            sql_script = sqlfile.read()
            
            # Execute the SQL script
            connection.executescript(sql_script)
            
           #commit the changes
            connection.commit()
            print("SQL file imported succesfully")

    except Exception as e:
        print(f"Error importing SQL file: {e}")

    finally:
        # Close the database connection
        connection.close()


    #step last close a database
    pass

# function calling is many time process
import_sql('accounting.db','accounting.sql') #actual argument