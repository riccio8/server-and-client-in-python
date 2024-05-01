import requests
from bs4 import BeautifulSoup
import os

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    url = input("Enter the URL: ")
    
    # Send request to get the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find CSS links
    css_links = soup.find_all('link', {'rel': 'stylesheet'})
    
    # Download and save CSS files
    for link in css_links:
        css_url = link.get('href')
        if css_url.startswith('http'):
            css_response = requests.get(css_url)
            if css_response.status_code == 200:
                css_filename = os.path.basename(css_url)
                save_file(css_filename, css_response.text)
                print(f"CSS file saved: {css_filename}")
            else:
                print(f"Failed to fetch CSS file: {css_url}")

    # Save HTML file
    html_filename = "index.html"
    save_file(html_filename, response.text)
    print(f"HTML file saved: {html_filename}")

if __name__ == "__main__":
    main()
