from pprint import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from utils import status_code_file
import requests as http_request
from Proxy import proxies
from datetime import date
from matplotlib import pyplot as plt
import lxml

class TableData(object):
    def __init__(self):
        self.main_url = 'https://www.ethiojobs.net/'
        self.daily_url = 'https://www.ethiojobs.net/search-results-jobs/?searchId=1638535666.0806&action=search&page=1&listings_per_page=100&view=list'
        self.req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        self.webpage = webpage = urlopen(self.req).read()
        self.soup = BeautifulSoup(self.webpage, 'lxml')
# WARRING DON'T MODIFY THIS FUNCTION
    def jobs_by_catagory(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        scrape_jobs = self.soup.find_all('a', class_='list-group-item')
        scarpe_jobs_number = self.soup.find_all('span', class_='badge badge-blue pull-right')
        # current on demand jobs
        all_jobs = []
        number_of_jobs = []
        links_of_jobs = []

        for jobs in scrape_jobs:
            all_jobs.append(jobs.h4.text)

        for sjn in scarpe_jobs_number:
            number_of_jobs.append(sjn.text)

        for links_of_job in scrape_jobs:
            links_of_jobs.append(links_of_job.get('href'))

        total_jobs = zip(all_jobs, number_of_jobs, links_of_jobs)
        return list(total_jobs)

    def latest_goverment_jobs(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        latest_jobs = []
        aw = self.soup.find_all('a', target="_blank")

        for i in aw:
            latest_jobs.append(i.text)
        rez = []
        for x in latest_jobs:
            rez.append(x.replace("\n", ""))

        while ("" in rez):
            rez.remove("")

        rez.pop(0)
        rez.pop(-1)
        rez.pop()
        zz = []
        for iw in rez:
            zz.append(iw)

        aw_time = self.soup.find_all('span', class_="pull-right")
        # time_stamp
        time_stamp = []
        ts = []
        for i in aw_time:
            time_stamp.append(i.text)

        for ix in time_stamp:
            if not ix.isdigit() and ix != 'Today' and ix != 'Yesterday':
                ts.append(ix)

        # more info
        aw_more = self.soup.find_all('p', class_="no-marign")
        no_margin_text = []
        no_margin_text_b = []
        rex = []
        for i in aw_more:
            no_margin_text.append(i.text)
        for y in no_margin_text:
            no_margin_text_b.append(y.replace("\t", ""))

        while ("" in no_margin_text_b):
            no_margin_text_b.remove("")

        ngrock_man = []
        for ngrok in no_margin_text_b:
            ngrock_man.append(ngrok.strip())

        # print(ngrock_man)
        return list(zip(zz, ts, ngrock_man))

    def jobs_by_location(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        catagory = []
        catagory_jobs_numbers = []
        aw = self.soup.find_all('td')
        for i in aw:
            try:
                catagory_jobs_numbers.append(i.a.span.text)
                catagory.append(i.a.h4.text)
            except AttributeError:
                pass
        return (list(zip(catagory, catagory_jobs_numbers)))

    def pyplot_job_by_location_basic(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        catagory = []
        catagory_jobs_numbers = []
        plot_loction = []
        aw = self.soup.find_all('td')
        for i in aw:
            try:
                catagory_jobs_numbers.append(i.a.span.text)
                catagory.append(i.a.h4.text)
            except AttributeError:
                pass
        for location in catagory:
            plot_loction.append(location.split('Jobs in ')[-1])
        plot_loction.reverse()
        real_numbers = [int(i) for i in catagory_jobs_numbers]
        plt.ylabel('Locations')
        plt.xlabel('Number of Jobs')
        plt.title('Jobs By Loaction')
        plt.plot(real_numbers,plot_loction)
        plt.legend(f'{date.today().year}')
        return plt.show()
    def pyplot_job_by_location_bar(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        catagory = []
        catagory_jobs_numbers = []
        plot_loction = []
        aw = self.soup.find_all('td')
        for i in aw:
            try:
                catagory_jobs_numbers.append(i.a.span.text)
                catagory.append(i.a.h4.text)
            except AttributeError:
                pass
        for location in catagory:
            plot_loction.append(location.split('Jobs in ')[-1])
        plot_loction.reverse()
        real_numbers = [int(i) for i in catagory_jobs_numbers]
        plt.ylabel('Locations')
        plt.xlabel('Number of Jobs')
        plt.title('Jobs By Loaction')
        #plt.figure(figsize=(17, 7))
        plt.bar(real_numbers, plot_loction)
        plt.legend(f'{date.today().year}')
        return plt.show()

    def pyplot_job_by_location_pie(self):
        #req = Request(self.main_url, headers={'User-Agent': 'Mozilla/5.0'})
        #webpage = urlopen(req).read()
        #soup = BeautifulSoup(webpage, 'lxml')
        catagory = []
        catagory_jobs_numbers = []
        plot_loction = []
        aw = self.soup.find_all('td')
        for i in aw:
            try:
                catagory_jobs_numbers.append(i.a.span.text)
                catagory.append(i.a.h4.text)
            except AttributeError:
                pass
        for location in catagory:
            plot_loction.append(location.split('Jobs in ')[-1])

        real_numbers = [int(i) for i in catagory_jobs_numbers]
        plt.title('Jobs By Loaction')
        plt.pie(real_numbers,labels=plot_loction,radius = 100000, frame = True,shadow = True)
        plt.legend()
        return plt.show()







