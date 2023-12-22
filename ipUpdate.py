import requests # Import requests library to send HTTP requests
import time # Import time library to use sleep function for scheduling
import sched # Import sched library to schedule the check and update task
import json # Import json library to work with JSON data
import datetime # Import datetime library to get the current time
from colorama import init, Fore, Back, Style # Import colorama library to add colors to console output

init() # Initialize colorama library

# Define global variables
godaddy_ip = None # This will store the current IP address from GoDaddy
godaddy_url = 'https://api.godaddy.com'
godaddy_key = 'YOUR_KEY'
godaddy_sec = 'YOUR_SECRET'
godaddy_dom = 'YOUR_DOMAIN_NAME'
godaddy_sdn = 'www | @ | YOUR_SUBDOMAIN_NAME' # You can specify multiple subdomains separated by pipes
godaddy_api = f'{godaddy_url}/v1/domains/{godaddy_dom}/records/A/{godaddy_sdn}' # Construct the API URL for GoDaddy

headers = {
    'Authorization': f'sso-key {godaddy_key}:{godaddy_sec}',
    'Content-Type': 'application/json' # Specify JSON as the content type for the request
}

# Define the main function
def main():
    minutes = 5 # Define how often to run the check and update task
    scheduler = sched.scheduler(time.time, time.sleep) # Create a scheduler object
    repeat_function(scheduler, 60 * minutes, checkIp) # Schedule the check and update task to run every 5 minutes
    scheduler.run() # Start the scheduler

# Define the repeat_function function
def repeat_function(scheduler, interval, action, arguments=()):
    scheduler.enter(interval, 1, repeat_function, (scheduler, interval, action, arguments)) # Schedule the next run of the action function
    action(*arguments) # Run the action function

# Define the checkIp function
def checkIp():
    global godaddy_ip # Use the global godaddy_ip variable to store the current IP address from GoDaddy
    try:
        if not godaddy_ip: godaddy_ip = getGodaddyIP() # If the godaddy_ip variable is not set, get the current IP address from GoDaddy
        pubIp = getPubIp() # Get the current public IP address
        
        if godaddy_ip != pubIp: # If the current IP address from GoDaddy does not match the public IP address, update the IP address on GoDaddy
            updateIP(pubIp)
        else: # If the IP address is unchanged, print a message to the console
            now = datetime.datetime.now()
            print(now, Fore.GREEN + ' IP is unchanged' + Style.RESET_ALL)
    except:
        print('failed to check ip')

# Define the getGodaddyIP function
def getGodaddyIP():
    global godaddy_url # Use the global godaddy_url variable to construct the API URL
    global headers # Use the global headers variable to send the authorization header
    
    response = requests.get(godaddy_api, headers=headers) # Send a GET request to the GoDaddy API to get the IP address for the given domain and subdomain
    json_content = json.loads(response.content) # Convert the response content to JSON
    ip_address = json_content[0]['data'] # Extract the IP address from the JSON data
    #print(ip_address)
    return ip_address # Return the IP address

# Define the getPubIp function
def getPubIp():
    response = requests.get('https://api.ipify.org') # Send a GET request to the ipify API to get the current public IP address
    ip_address = response.text # Extract the IP address from the response
    #print