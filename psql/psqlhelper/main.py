import logging
import psycopg2
from psycopg2 import sql

class PostgresDB:
    def __init__(self, dbname, user, password, host='localhost', port='5432', log_level=logging.DEBUG):
        # Initialize a logger with a given log level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Create a console handler that logs error messages
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        # Create a file handler that logs all messages at the configured log level
        file_handler = logging.FileHandler('db_library.log')
        file_handler.setLevel(log_level)

        # Define a standard log format including time, level, and message
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add both handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        try:
            # Establish a connection to the PostgreSQL database
            self.connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.connection.cursor()  # Create a cursor object for executing queries
            self.logger.info("Database connection successful.")
        except Exception as e:
            self.logger.error(f"Error connecting to database: {e}")
            raise  # Raise exception if connection fails

    def execute_query(self, query, params=None):
        try:
            # Execute the SQL query with optional parameters
            self.cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                # Fetch all results if the query is a SELECT statement
                result = self.cursor.fetchall()
                return result
            else:
                # Commit changes to the database for non-SELECT operations
                self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error executing query: {e}")
            raise  # Raise exception if query execution fails

    def close(self):
        if self.connection:
            # Close the cursor and database connection
            self.cursor.close()
            self.connection.close()
            self.logger.info("Database connection closed.")

# Example usage by team members:
# from db_library import PostgresDB
# db = PostgresDB(dbname='mydb', user='user', password='pass', log_level=logging.INFO)
# result = db.execute_query("SELECT * FROM table_name")
# db.close()
