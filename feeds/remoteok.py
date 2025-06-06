import feedparser

def get_remoteok_jobs(keywords):
    url = "https://remoteok.com/remote-dev-jobs.rss"
    feed = feedparser.parse(url)
    jobs = []

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        job_id = entry.id

        # თუ ნებისმიერი საკვანძო სიტყვა ემთხვევა title-ში
        if any(keyword.lower() in title.lower() for keyword in keywords):
            jobs.append({
                "id": job_id,
                "title": title,
                "link": link
            })

    return jobs
