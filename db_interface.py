import pyodbc

class DatabaseInterface:
    def __init__(self, db_config):
        self.connection_string = (
            f"DRIVER={{SQL Server}};"
            f"SERVER={db_config['server']};"
            f"DATABASE={db_config['database']};"
            f"UID={db_config['user']};"
            f"PWD={db_config['password']}"
        )

    def check_data_integrity(self):
        # This is a placeholder for actual integrity checks
        with pyodbc.connect(self.connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM some_table")
            count = cursor.fetchone()[0]
            if count < 0:
                return ["Data count is invalid"]
        return []

