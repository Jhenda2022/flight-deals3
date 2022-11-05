# flight-deals3
Third attempt at replicating Angela Yu's flight deals exercise, a capstone project that uses environment variables, API, requests library, object oriented programming,
datetime module, and smtplib. 

First, a get request was made to fetch data of lowest prices from google sheet. 

Second, a get request was sent to Tequila to fetch city codes using locations API. 

Third, a put request was performed to populate iATA codes of cities in the google sheet. 

Fourth, datetime module and time delta was used to determine date for tomorrow and for the next six months. 

Fifth, another get request was sent to Tequila using search API to fetch flight data from tomorrow up to six months from origin city to destination cities. Stopovers/layovers and booking links were determined from the data generated from Tequila. If destination price from the result is lower than what's listed in the google sheet, an alert will be sent to email using smtplib. Used cutt.ly API to shorten the generated link. 

Note that environment variables were used to hide sensitive data.
