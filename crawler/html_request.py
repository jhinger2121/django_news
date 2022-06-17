import requests
from requests.exceptions import ConnectionError
import random
timeout = 30

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
]

class MakeRequest:
    def __init__(self):
        self.inst = self
        self.session = requests.Session()
        self.tries = 1
        self.headers = {
            "Host": "",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def _get(self, url):
        # update the headers "Host" for the url
        self._update_headers(url)
        print(f"Headers: {self.headers['User-Agent']} \n Host: {self.headers['Host']}")

        request = self.session.get(url=url, headers=self.headers, timeout=timeout)
        if request.status_code != 200:
            if url == 'https://number1.co.za/category/django-2/':
                return request
            if not (self.tries > 1):
                self.tries += 1
                self.inst._get(url)
            else:
                print('You MAX out tries ', self.tries)
                raise ConnectionError(
                    'Status code {status} for url {url}\n'.format(
                        status=request.status_code, url=url, content=request.text))
        return request
        
    
    def _update_headers(self, url):
        # change user-agent 'Hosts' to current site
        # (line): amazon.ca to amazon.com OR amazon to newegg
        if 'number1' in url:
            self.headers['Host'] = "number1.co.za"
        elif 'djangostars' in url:
            self.headers['Host'] = 'djangostars.com'
        elif 'djangotricks' in url:
            self.headers['Host'] = 'djangotricks.blogspot.com'
        elif 'djangoproject' in url:
            self.headers['Host'] = 'www.djangoproject.com'
        elif 'justdjango' in url:
            self.headers['Host'] = 'justdjango.com'
        elif 'djangocentral.com' in url:
            self.headers['Host'] = 'djangocentral.com'

        user_agent = random.choice(user_agent_list)
        self.headers['User-Agent'] = user_agent
