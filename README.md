This project scrapes data from https://apps.putnam-fl.com/pa/property/?type=api&parcel=06-13-28-1830-
0020-0102. I only used 2 libraries (Scrappy to send the web requests and BeautifulSoup to aid with parsing the html doc).

The code for the scrappy spider is hosted on /tutorial/tutorial/spiders/property_spider.py. 
Once the spider has queried the html doc, it is passed to a PropertyData object which handles the parsing. 

Logs for the the queried html page are stored in tutorial/tutorial/logged_pages, and the extracted values are stored in tutorial/tutorial/logged_csvs.

While working on this, I ran into a major hurdle. Loading the initial page loads it with the content of the Main tab. Clicking on any other tab (Values, Land, Improvements, etc.) loads the content asynchronously - meaning that the response from scrappy contains an HTML doc with a chunk of data in the tab section missing saying "Your content is being loaded". This can be solved by integrating Scrappy with an Asincio Reactor, headless chrome, or Selenium, which allow for processing of asynchronous requests. All are possible solutions that would take about a week to test and troubleshoot.

To run the program, clone it, activate the virtual env, and inside the tutorial dir run scrapy crawl quotes. It will parse the url and create a new csv file inside the logged_csvs dir, and a new html file containing the parsed doc inside logged_pages. 