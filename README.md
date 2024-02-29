# UK Lawyers Scraping Project

In this project we are scraping https://solicitors.lawsociety.org.uk/ to extract all registered uk lawyers
data from this site. There are around more than 200k lawyers.

So far i have written a functioning scrapy project with one spider name lawyer which scrapes all lawyers page indvidually.

## Installation & Running
* First clone this repo into your project dir
* Install Python version 3.10.9
* Create a virtual env and install the dependencies listed in requirements.txt
* Activate the virtual env.
* Update the following line of code in uk_lawyers/spiders/lawyers.py "for i in range(1, 1001):  # Adjust range as needed"
* Run the script by using the command in cmd "scrapy crawl lawyers -O data.csv"
* Data would be saved in the project dir


## TODO
* Write a spider to extract organization data.
* Run the lawyer spider with start_request url changed to 600,000.
* Save logs in logs dir.