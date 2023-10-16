import praw


class RedditClient():
    """Class representing a customized reddit api crawler"""
    def __init__(self, client_id, client_secret, password,user_agent,username, subreddit):
        self.reddit = praw.Reddit(  
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent=user_agent,
            username=username,
        )

        self.subreddit = self.reddit.subreddit(subreddit)

    def get_submissions(self):
        """Function returning submissions urls"""
        submissions_urls_gen = (submission.url for submission in 
             self.subreddit.search("Quarterly Salary", limit=None) 
             if submission.author == "AutoModerator")
        return submissions_urls_gen
    
    def get_comments(self,submission_url):
        """Function returning comments"""
        comments_gen = (comment.body for comment in list(self.reddit.submission(url =submission_url).comments))
        return comments_gen , len(list(self.reddit.submission(url =submission_url).comments))