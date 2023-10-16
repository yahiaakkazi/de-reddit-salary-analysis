import configparser, json
import openai
from tqdm import tqdm
import pandas as pd
from llm_open.llm import LLM
from prawutils.reddit_client import RedditClient

config = configparser.ConfigParser()
config.read('config.ini')
client_id = config['REDDIT']['CLIENT_ID']
client_secret = config['REDDIT']['CLIENT_SECRET']
password = config['REDDIT']['PW']
user_agent = config['REDDIT']['USER_AGENT']
username = config['REDDIT']['USERNAME']
subreddit = config['REDDIT']['SUBREDDIT']
api_key = config['OPENAI']['API_KEY']
llm_model = config['OPENAI']['LLM_MODEL']

with open('system_request.txt', 'r') as file:
    system_request = file.read()
openai.api_key = api_key
if __name__ == "__main__":
    rc = RedditClient(client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent=user_agent,
            username=username,
            subreddit=subreddit
            )
    submissions = rc.get_submissions()
    data = []
    for submission in submissions:
        comments = rc.get_comments(submission)
        for comment in tqdm(comments):
            llm_response = LLM(llm_model=llm_model,
                system_request=system_request,
                user_request=comment)
            message = llm_response.get_message()
            dict_data = json.loads(message)
            data.append(dict_data)
    df = pd.DataFrame(data)
    df.to_csv('data.csv')
