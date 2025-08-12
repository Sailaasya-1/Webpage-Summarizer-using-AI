#Taking the URL of the website, cleaning the raw HTML and extracting the title and text.
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

MODEL = "llama3.2"


headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:

    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt =  user_prompt + "\nThe contents of this website is as follows; \
Just a markdown short summary that might include news and announcements. \n\n"
    user_prompt += website.text
    return user_prompt


