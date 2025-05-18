from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering out: {unfamiliar_skill}')

def find_jobs():
    html_web = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=').text
    soup = BeautifulSoup(html_web, 'lxml')
    jobs = soup.find_all('li')

    for job in jobs:
        try:
            published_date = job.find('span', class_ = "posting-time")
    #       if published_date and ('days ago' in published_date.text.lower()):
            
            company = job.find('span', class_ = "srp-comp-name")
            skill = job.find('div', class_ = "srp-keyskills")
            more_info = job.div.a['href'] if job.find('a') else 'N/A'
            if unfamiliar_skill.lower() not in skill.text.lower():
                if all([company, skill, published_date, more_info]):
                    print(f'Company name: {company.text.strip()}')
                    print(f'Required Skill: {skill.text.strip()}')
                    print(f'Published Date: {published_date.text.strip()}')
                    print(f"More info: {more_info}")
        except AttributeError:
            continue

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} seconds...")
        time.sleep(time_wait * 60)
        