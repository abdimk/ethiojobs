from pprint import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from utils import status_code_file
import requests as http_request
from Proxy import proxies
from matplotlib import pyplot
import lxml

class EthioJobs(object):
    def __init__(self,query):
        self.query = query
        self.words = self.query.split()
        self.sent_str = ""
        for i in self.words:
            self.sent_str += str(i) + "+"
        self.sent_str = self.sent_str[:-1]
        self.url = f'https://www.ethiojobs.net/search-results-jobs/?action=search&listing_type%5Bequal%5D=Job&keywords%5Ball_words%5D={self.sent_str}'
        self.status_code = urlopen(self.url).getcode()
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})

    def __str__(self):
       return str(self.sent_str)

    def show_status(self):
        #my_proxy = proxies.get_proxy()
        #status_code = http_request.get(self.url,proxies=urllib.request.getproxies())
        #status_code = urlopen(self.url).getcode()
        http_request_response = status_code_file.http_status(int(self.status_code))
        return http_request_response

    def numberofjobs(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        number_of_jobs = soup.find_all('span', class_='pull-left sp-right')
        for number_of_job in number_of_jobs:
            try:
                if (int(number_of_job.text) == None or int(number_of_job.text) == 0):
                    print('\n')
            except ValueError:
                print('No jobs found!')
            else:
                return(f'{int(number_of_job.text)} {self.query} jobs has been found!')
    def scraped_jobs_title(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        job_titles_list = []
        job_titles = soup.find_all('h2')
        for job in job_titles:
            job_titles_list.append(job.text)
        return job_titles_list
    def scraped_campany_names(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        campany_names = []
        refine_search = soup.find_all('a', class_="company-name")
        for campany_names_title in refine_search:
            campany_names.append(campany_names_title.text)
        return campany_names
    def job_over_all(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        job_over_all = soup.find_all('span', class_='captions-field')
        job_over_all_list = []
        for over_all in job_over_all:
            job_over_all_list.append(over_all.text.strip())
        return job_over_all_list

    def scraped_campany_jobs_dead_line(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        dead_line_list = []
        dates = soup.find_all('span', class_='text-danger captions-field')
        for date in dates:
            dead_line_list.append(date.text)
        return dead_line_list
    def scraped_campany_jobs_info(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        show_brief_list = []
        show_brief = soup.find_all('div', class_='show-brief')
        for i in show_brief:
            show_brief_list.append(i.text)

        show_brief_list.pop(0)
        return show_brief_list
    def scraped_campany_jobs_links(self):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        links = []
        view_job_list = soup.find_all('div', class_='listing-links')
        for i in view_job_list:
            links.append(i.a.get('href'))

        return links

