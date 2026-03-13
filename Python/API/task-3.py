from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def scheduled_post_fetch():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = fetch_api_data(url)

    if not posts:
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

    scheduler = BlockingScheduler()
scheduler.add_job(scheduled_post_fetch, "interval", minutes=10)

print("Scheduler started...")
scheduler.start()

