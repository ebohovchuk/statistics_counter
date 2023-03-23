run docker-compose up (the project is available at the link http://127.0.0.1:8000)
 
We have 3 entry points:

1. Create statistic. Method - POST, url - http://127.0.0.1:8000/statistics/

   example request body:
   ```
   {
    "date": "2023-03-23", # string required. Format YYYY-MM-DD
    "views": 44, # int optional
    "clicks": 55, # int optional
    "cost": 12.22, # decimal optional
   }
   ```
   
   example curl request:
   ```
   curl --location --request POST 'http://127.0.0.1:8000/statistics/' \
   --header 'Content-Type: application/json' \
   --data-raw '{
       "date": "2023-03-23",
       "views": 44,
       "clicks": 55,
       "cost": 12.22
   }'
   ```
   
   example response:
   ```
   {
    "date": "2023-03-23", # string. Format YYYY-MM-DD
    "views": 44, # int nullable
    "clicks": 55, # int nullable
    "cost": 12.22, # decimal nullable
   }
   ```
   
2. Delete statistic. Method - DELETE, url - http://127.0.0.1:8000/statistics/{STATISTIC_ID}/

   example curl request:
   ```
   curl --location --request DELETE 'http://127.0.0.1:8000/statistics/3/'
   ```
   
   example response:
   ```
   {
    "message": "delete statistic item with id 3"
   }
   ```
   
   
3.Get all statistics filtered by from_date, to_date and sorted by order_by value. Method - GET, url - http://127.0.0.1:8000/statistics/
 
   from_date - string. Start date of the period (inclusive). Not required

   to_date - string. End date of the period (inclusive). Not required
   
   order_by - string. Field to sort by. Allow values - views, clicks, cost, cpc, cpm
   
   example curls request:
   ```
   curl --location --request GET 'http://127.0.0.1:8000/statistics/?from_date=2023-03-10&to_date=2023-03-22&order_by=views'
   ```

   example response:
   ```
   [
       {
           "date": "2023-03-11",
           "views": 10,
           "clicks": 2,
           "cost": 24.44,
           "cpc": 12.22,
           "cpm": 2444.0
       },
       {
           "date": "2023-03-10",
           "views": 12,
           "clicks": 6,
           "cost": 24.44,
           "cpc": 4.073333333333333,
           "cpm": 2036.6666666666667
       }
   ]
   ```


You can also view the docs at http://127.0.0.1:8000/docs