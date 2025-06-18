# Web Scraping Program

import requests
from bs4 import BeautifulSoup # type: ignore

def scrape_website(url):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all headings (h1-h6)
        for level in range(1, 7):
            for heading in soup.find_all(f'h{level}'):
                print(f'H{level}: {heading.text.strip()}')

        print("\nAll Links Found:")
        # Extract all links
        for link in soup.find_all('a', href=True):
            print(link['href'])

    except requests.exceptions.RequestException as e:
        print("Error during request:", e)

if __name__ == '__main__':
    url = input("Enter a website URL (e.g., https://example.com): ")
    scrape_website(url)
