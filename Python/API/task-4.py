def summary_report(new_posts):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    total_users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM posts")
    total_posts = cur.fetchone()[0]

    print("\n Summary Report ")
    print(f"Total Users: {total_users}")
    print(f"Total Posts: {total_posts}")
    print(f"New Posts Added: {new_posts}")
    print("=======Ended============\n")

    cur.close()
    conn.close()
