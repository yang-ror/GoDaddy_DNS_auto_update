# GoDaddy DNS Updater
This Python script checks if the current public IP address matches the DNS record on GoDaddy domain service and updates it if it does not match. It uses the requests library to send HTTP requests to the GoDaddy API and the ipify API to get the public IP address. It also uses the sched library to schedule the check and update task to run every 5 minutes. The colorama library is used to add colors to the console output.

## Prerequisites
- Python 3.x
- requests library
- colorama library

## Installation
1. Clone or download the repository
2. Install the requests and colorama libraries by running the following commands:
	- pip install requests
	- pip install colorama
3. Edit the global variables in the script to match your GoDaddy account information and domain/subdomain names
4. Run the script using the following command:
5. python godaddy_dns_updater.py

## Usage
The script will check the current public IP address every 5 minutes and update the DNS record on GoDaddy if it does not match. The console output will show whether the IP address was updated or unchanged.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.