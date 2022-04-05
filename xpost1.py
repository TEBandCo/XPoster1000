#adapted from busterttoni11 and bboe's videos. 

#made by /u/TheEpicBlob. 
#requested by /u/Aromatic_Sugar_966

import praw

subreddit_to_search = 'test' #subreddit to search
subreddit_to_xpost = 'TheEpicBlob' #subreddit to crosspost into

def authenticate():
    print("Authenticating..."),
    reddit = praw.Reddit('BOT', #see praw.ini file
        user_agent="Crossposting from one sub to another") #provide description of bot
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    print("Getting posts...")
    for submission in reddit.subreddit(subreddit_to_search).stream.submissions(skip_existing=True):
        print('New post found, ' + submission.title)
        submission.crosspost(subreddit_to_xpost, send_replies=False)
        print('Crossposted ' + submission.title + ' into ' + subreddit_to_xpost)

if __name__ == '__main__':
    main()