```python
import requests

def fetch_ip_info(ip_address):
    """
    Fetches geolocation information for the given IP address using an external API.
    
    Args:
        ip_address (str): The IP address to lookup.
        
    Returns:
        dict: A dictionary containing geolocation data or an error message.
    """
    try:
        # API endpoint for IP geolocation
        api_url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch data, check the IP address or try again."}
    except Exception as e:
        return {"error": str(e)}

def main():
    """
    Main function to execute the OSINT script.
    """
    # Sample IP addresses for testing
    ip_addresses = ["8.8.8.8", "192.0.2.1", "invalid_ip"]
    
    for ip in ip_addresses:
        print(f"Fetching information for IP: {ip}")
        ip_info = fetch_ip_info(ip)
        
        # Print the output in a formatted way
        if "error" in ip_info:
            print(f"Error: {ip_info['error']}")
        else:
            print(f"IP: {ip_info.get('ip')}")
            print(f"Location: {ip_info.get('city')}, {ip_info.get('region')}, {ip_info.get('country')}")
            print(f"Coordinates: {ip_info.get('loc')}")
            print(f"Organization: {ip_info.get('org')}")
            print("-" * 40)

if __name__ == "__main__":
    main()
```