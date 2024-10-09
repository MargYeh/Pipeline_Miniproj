# Pipeline Mini Project
This is a simple pipeline that uses mySQL.connector to load data from a csv file into a prepared database on mySQL. 
Included is TableSetup.sql which generates a table with the following schema when run in mySQL: 
| Column  | Type |
| ------------- | ------------- |
| ticket_id  | INT  |
| trans_date | DATE |
| event_id | INT |
| event_name | VARCHAR(50) |
| event_date | DATE |
| event_type | VARCHAR(10) |
| event_city | VARCHAR(20) |
| customer_id | INT |
| price | DECIMAL |
| num_tickets | INT |

## Steps to run
- Create a new database in mySQL and use TableSetup.sql to create a table with the above schema.
- Connect to the database: Replace '\<user\>', '\<password\>', '\<database_name\>' with the appropriate information in get_db_connection() inside pipeline.py
- Run pipeline.py
- The pipeline should load the data from third_party_sales_1.csv into the mySQL database and return the top three most popular events, displayed in the console.
  
## Results
Output:
![image](https://github.com/user-attachments/assets/9ac00828-30c5-4e62-b363-79a5b7486dee)
