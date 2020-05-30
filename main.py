
import cx_Oracle

username = 'SYSTEM'
password = '1234'
databaseName = "DESKTOP-M87434D/xe"

connection = cx_Oracle.connect(username, password, databaseName)

cursor = connection.cursor()

query1 = '''
select max(avgprice), region
from Prices
INNER JoIN Regions on
Regions.id = Prices.id
GROUP BY regions.region
'''
cursor.execute(query1)

for row in cursor:
    print(row)

query2 = '''
SELECT region, 
 round( COUNT(*) * 100 / ( SELECT COUNT(*) FROM Regions ), 2 ) as PERC
FROM Avocado
JOIN Regions 
ON Avocado.id=Regions.id
GROUP BY region
ORDER BY PERC DESC
'''
cursor.execute(query2)

for row in cursor:
    print(row)

query3 = '''
SELECT month, avg(avgprice)
FROM DATE_t 
JOIN Prices
ON Months.id = Prices.id
GROUP BY month
'''
cursor.execute(query3)

for row in cursor:
    print(row)

cursor.close()

connection.close()
