import mysql.connector
import csv

def get_db_connection(): 
    connection = None 
    try: connection = mysql.connector.connect(
        user='<user>', 
        password='<password>', 
        host='localhost', 
        port='3306', 
        database='<database name>'
        ) 
   
    except Exception as error: 
        print("Error while connecting to database for job tracker", error) 
    
    return connection

def load_third_party(connection,file_path_csv): 
    cursor = connection.cursor() 
    #[IteratethroughtheCSVfileandexecuteinsertstatement] 
    with open (file_path_csv, 'r') as file:
        csv_file = csv.reader(file)
    
        for row in csv_file:
            cursor.execute('INSERT INTO sales (ticket_id,trans_date,event_id,event_name,event_date, event_type, event_city, customer_id, price, num_tickets)'
                       'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    connection.commit() 
    cursor.close() 
    return

def query_popular_tickets(connection): 
    #Get the most popular ticket in the past month 
    sql_statement="SELECT event_name, SUM(num_tickets) as total FROM sales GROUP BY event_name ORDER BY total DESC LIMIT 3" 
    cursor=connection.cursor() 
    cursor.execute(sql_statement) 
    records=cursor.fetchall() 
    cursor.close() 
    return records

connection = get_db_connection()
load_third_party(connection, 'third_party_sales_1.csv')
records = query_popular_tickets(connection)

print('Here are top three events that sold the most number of tickets:')
for line in records:
    (event_name, total_tickets) = line
    print(f'- {event_name}: {total_tickets} tickets sold')
