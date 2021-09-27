All required libraries are added in requirements.txt
All APIs endpoints are added to tutorial_postman.json file.
ORM queries are added in orm_data.txt

NOTE:
For the Excel bulk upload- 
  I have used django-import-export library, I have modified the excel file based on requirements. 
  We can upload excel data from django/admin site.
  
  I have also written bulk upload logic in courses/utils.py using pandas as well as model-objects-bulk_create(commented).
  Getting some issue with both the approaches, haven't got the time to resolve it.
  
Please let me know for any modifications.
