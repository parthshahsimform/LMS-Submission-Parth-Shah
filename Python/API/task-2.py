import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("")
    )


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY,
        name TEXT,
        email TEXT,
        address TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS posts(
        id INT PRIMARY KEY,
        user_id INT,
        title TEXT,
        body TEXT
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

# store user 
def save_users(users):
    conn = get_connection()
    cur = conn.cursor()

    for user in users:
        address = f"{user['address']['street']}, {user['address']['city']}"

        cur.execute("""
        INSERT INTO users (id, name, email, address)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT (id) DO NOTHING
        """, (user["id"], user["name"], user["email"], address))

    conn.commit()
    cur.close()
    conn.close()

# store posts

def save_posts(posts):
    conn = get_connection()
    cur = conn.cursor()

    for post in posts:
        cur.execute("""
        INSERT INTO posts (id, user_id, title, body)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT (id) DO NOTHING
        """, (post["id"], post["userId"], post["title"], post["body"]))

    conn.commit()
    cur.close()
    conn.close()
