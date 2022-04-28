# XPoster1000
Reddit Bot to crosspost from one sub to another

Edit the praw.ini with your bot credentials from Reddit.

Update `subreddit_to_search` and `subreddit_to_xpost` with the originating and target sub respectively.

You will need to import/install PRAW on the machine running this script. More information on PRAW here: https://praw.readthedocs.io/en/stable/getting_started/installation.html

### How to search multiple subs?
Enter the subreddit you want to search followed by `+`. For example `subreddit_to_search = 'test+bottesting'` to search r/test and r/bottesting. 
