```python
import requests
from bs4 import BeautifulSoup

def fetch_ip_info(ip_address):
    """
    Fetches IP address information from the 'ipinfo.io' API.
    
    Args:
        ip_address (str): The IP address to look up.
        
    Returns:
        dict: A dictionary containing the IP information.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for IP: {ip_address}")
        return None

def scrape_domain_info(domain):
    """
    Scrapes the domain information from the 'whois.domaintools.com' website.
    
    Args:
        domain (str): The domain to look up.
        
    Returns:
        str: A string containing the domain information.
    """
    url = f"https://whois.domaintools.com/{domain}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting WHOIS information from the page
        whois_info = soup.find("div", class_="whois-info")
        return whois_info.get_text(strip=True) if whois_info else "No WHOIS info found."
    else:
        print(f"Error fetching data for domain: {domain}")
        return None

def main():
    # Example IP address and domain
    ip_address = "8.8.8.8"
    domain = "example.com"
    
    # Fetch and display IP information
    ip_info = fetch_ip_info(ip_address)
    if ip_info:
        print("IP Information:")
        print(ip_info)
    
    # Scrape and display domain information
    domain_info = scrape_domain_info(domain)
    if domain_info:
        print("\nDomain Information:")
        print(domain_info)

if __name__ == "__main__":
    main()
```
