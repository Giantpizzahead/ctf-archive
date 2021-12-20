import praw
import datetime
import time
import sys

reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/Giantpizzahead)",
    client_id="zWSJrO_cKYLzCdCPImAycw",
    client_secret="KX3C7xg9VMyD0HmVac09-pYYyJrC_A"
)

def get_authors(subreddit, start_post, end_post):
    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.new(limit=end_post+1)
    for i, post in enumerate(posts):
        if i < start_post: continue
        # print(post.title)
        print(datetime.datetime.fromtimestamp(post.created_utc).strftime('%b %d, %Y'), end="\t")
        sys.stdout.flush()
        # Get comments
        submission = reddit.submission(id=post.id)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if not comment.author: continue
            check_user_created(comment.author)

seen_users = set()

def check_user_created(redditor):
    if redditor.name in seen_users: return
    seen_users.add(redditor.name)
    try:
        if (datetime.datetime.now() - datetime.timedelta(days=28)) <= datetime.datetime.fromtimestamp(redditor.created_utc):
            print()
            print('USER', redditor.name)
            sys.stdout.flush()
            subs = []
            for comment in redditor.comments.new(limit=10):
                subs.append(comment.subreddit)
            print(' '.join([str(x) for x in set(subs)][:10]))
    except Exception as e:
        print(e)

# Find users who have comments on both subreddits
get_authors('ChicagoSuburbs', 0, 100)

'''
url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)

submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:]  # Seed with top-level
while comment_queue:
    comment = comment_queue.pop(0)
    print(comment.body)
    comment_queue.extend(comment.replies)
'''