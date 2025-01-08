import requests
from bs4 import BeautifulSoup
print("Script started")
print("Script started")

# Base URL of the website you want to scrape
base_url = 'https://example.com/leads?page='

# Function to get leads from a single page
def get_leads_from_page(page_number):
    url = base_url + str(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    leads = soup.find_all('div', class_='lead')  # Modify this based on the website's structure
    return leads

# Function to filter leads by location
def filter_leads(leads, location):
    filtered_leads = []
    for lead in leads:
        # Extract location from lead (modify this based on the website's structure)
        lead_location = lead.find('span', class_='location').text.strip()
        if location.lower() in lead_location.lower():
            filtered_leads.append(lead)
    return filtered_leads

# Example usage
location = 'California'
all_leads = []
page_number = 1

# Loop through multiple pages
while True:
    leads = get_leads_from_page(page_number)
    if not leads:
        break
    all_leads.extend(leads)
    page_number += 1

# Filter leads by location
filtered_leads = filter_leads(all_leads, location)

# Print filtered leads
for lead in filtered_leads:
    print(lead.text.strip())
