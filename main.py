```python
import requests

def get_ip_info(ip_address):
    """
    Fetches information about the given IP address using the ipinfo.io API.
    
    Args:
        ip_address (str): The IP address to look up.
    
    Returns:
        dict: A dictionary containing IP information or an error message.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response as a dictionary
    except requests.RequestException as e:
        return {"error": str(e)}

def display_ip_info(ip_info):
    """
    Displays the information of the IP address in a readable format.
    
    Args:
        ip_info (dict): The dictionary containing IP information.
    """
    if "error" in ip_info:
        print(f"Error fetching IP information: {ip_info['error']}")
    else:
        print("IP Information:")
        print(f"IP: {ip_info.get('ip', 'N/A')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")

def main():
    """
    Main function to execute the OSINT project for IP information.
    """
    ip_address = input("Enter an IP address (or leave blank for your public IP): ")
    if not ip_address.strip():
        # If no IP is provided, use the requester's public IP
        ip_info = get_ip_info("me")
    else:
        # Fetch information for the given IP address
        ip_info = get_ip_info(ip_address)

    # Display the fetched IP information
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```