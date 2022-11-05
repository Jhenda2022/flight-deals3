# flight-deals3
Initial commit:
Third attempt at replicating Angela Yu's flight deals exercise, a capstone project that uses environment variables, API, requests library, object oriented programming,
datetime module, and telegram bot. 

First, a get request was made to fetch data of lowest prices from google sheet. 

Second, a get request was sent to Tequila to fetch city codes using locations API. 

Third, a put request was performed to populate iATA codes of cities in the google sheet. 

Fourth, datetime module and time delta was used to determine date for for tomorrow and for the next six months. Fifth, another get request was sent to Tequila using search API to fetch flight data from tomorrow up to six months from origin city to destination cities. If destination price from the result is lower than what's listed 
in the google sheet, an alert will be sent to telegram using telegram bot. Note that environment variables were used to hide sensitive data.

2nd Commit:
Stopovers/layovers and booking links were determined from the data generated from Tequila. Used cutt.ly API to shorten the generated link. 
Used smtplib instead of telegram bot to send alert via email. 

3rd commit:
Removed print function in flight_details.py for a cleaner project.
