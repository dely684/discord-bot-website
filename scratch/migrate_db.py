import sqlite3

def migrate():
    conn = sqlite3.connect("bot_database.db")
    cursor = conn.cursor()
    
    # Add new columns to server_config if they don't exist
    columns = [
        ("automod_links", "INTEGER DEFAULT 0"),
        ("automod_spam", "INTEGER DEFAULT 0"),
        ("automod_words", "TEXT")
    ]
    
    for col_name, col_type in columns:
        try:
            cursor.execute(f"ALTER TABLE server_config ADD COLUMN {col_name} {col_type}")
            print(f"Added column: {col_name}")
        except sqlite3.OperationalError:
            print(f"Column already exists or error adding: {col_name}")
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate()
