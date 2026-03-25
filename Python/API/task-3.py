from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import psycopg2


# Function to fetch API data
def fetch_api_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("API request failed")
            return None
    except Exception as e:
        print("API error:", e)
        return None


# Function to connect to database
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_user",
        password="your_password"
    )


def scheduled_post_fetch():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = fetch_api_data(url)

    if not posts:
        print("No posts fetched")
        return

    conn = get_connection()
    cur = conn.cursor()

    new_posts = 0

    for post in posts:
        cur.execute("""
        INSERT INTO posts (id, user_id, title, body)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT (id) DO NOTHING
        """, (post["id"], post["userId"], post["title"], post["body"]))

        if cur.rowcount > 0:
            new_posts += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"{datetime.now()} - Added {new_posts} new posts")


# Create scheduler
scheduler = BlockingScheduler()

# Run every 10 minutes
scheduler.add_job(scheduled_post_fetch, "interval", seconds=10)

print("Scheduler started...")

scheduler.start()
