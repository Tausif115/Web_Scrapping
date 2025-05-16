from bs4 import BeautifulSoup
import requests

html_web = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_web, 'lxml')
jobs = soup.find_all('li')

for job in jobs:
    try:
        published_date = job.find('span', class_ = "posting-time")
        if published_date and ('18 days ago' in published_date.text.lower()):
        
            company = job.find('span', class_ = "srp-comp-name")
            skill = job.find('div', class_ = "srp-keyskills")
            
            if all([company, skill, published_date]):
                print(f'''
                Company name: {company.text.strip()}
                Skills: {skill.text.strip()}
                Published Date: {published_date.text.strip()}
                ''')
    except AttributeError:
        continue
    