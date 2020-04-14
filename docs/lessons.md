### Lessons
<hr />    

#### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons`
<hr />    

#### - Retrieve all lessons in the course 
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons`
##### Method: GET        
##### Payload: 
```Json
{
    "jwt":  "32132143432432",
    "public_id":  "123123123"
}
```         
##### Success Response:
code : 200
```
Json retrive list of lessons with IDs
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```


#### - Retrieve a specific lesson in the course    
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}`    
##### Method: POST        
##### Payload: 
```Json
{
    "jwt":  "32132143432432"
}
```         
##### Success Response:
code : 200
```Json
{
    "name":   "lessonName",
    "order":  "1",
    "objective":  "123123",
    "content":   "content example"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```


#### - Create a new lesson in the course    
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons`    
##### Method: POST        
##### Payload: 
```Json
{
    "jwt":  "32132143432432",
    "order":  "1",
    "name":  "example",
    "objective":  "123123",
    "content":   "content example"
}
```         
##### Success Response:
code : 200
```Json
{
    "status":   "<Duplicate resource codes>"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```


#### - update lesson in the course    
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}`    
##### Method: PUT        
##### Payload: 
```Json
{
    "jwt":  "32132143432432",
    "order":  "1",
    "name":  "example",
    "objective":  "123123",
    "content":   "content example"
}
```         
##### Success Response:
code 200: 
```Json
{
    "status":  "updated"
}
```
or
```Json
{
    "status":  "<Duplicate resource codes>"
}
```


#### - how to delete lesson from database
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}`    
##### Method: DELETE        
##### Payload: 
```Json
{
    "jwt":   "ffff"
}
````         
##### Success Response:
code 200: 
```Json
{
    "status":  "deleted"              
}
```
<hr />    
