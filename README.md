# Integrate-Azure-Snowflake-to-create-real-time-dash-board
![image](https://user-images.githubusercontent.com/103509243/200219287-704520bb-3863-401d-90b4-8d8661baf664.png)
## Approach
(1) Create an Azure account  
(2) Create a Twitter Developer account and copy the bearer token, Access keys  
(3) Create a Storage Account. Ex) snowpipeline2022      
(4) Create a Container within that Storage Account. Ex) twitter  
(5) Create a Queue within that Storage Account. Ex) snowpipequeue  
(6) Create EventGrid subscription  (Whenever a new blob file is created, notifing there's a file landing into queue)  
(7) Create a Snowflakes Account on Azure  
(8) Create database, integration for Azure queue storage  
(9) Create a role in IAM of Storage Account with Storage Blob Contributor permission and assign it to Snowflakes service principal(Snowflakes App Name)  
(10) Create a role in IAM of Storage Queue and Storage Queue Contributor permission and assign it to Snowflakes service principal  
(11) Run the script twitter_search.py by altering the connection string and twitter API credentials  
(12) Create a Dashboard by traversing through Snowflakes Marketplace and feed in the SQL given in “Dashboard Query” topic, 
and choose the chart options to create a bar chart  

## Twitter Dashboard  
![image](https://user-images.githubusercontent.com/103509243/200347187-ed08c18c-7e8c-4e43-a794-0b63799472db.png)







