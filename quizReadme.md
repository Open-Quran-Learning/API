

## Documentation



### Quiz

<hr />    

#### Route: `api/v1/programs/{id}/courses/{id}/quizzes`
<hr /> 

#### - how to enter quiz route
##### Method: GET        
##### Payload: 
   ```Json
{
    "jwt": "65416584846465644546"
    
}
```   
##### Success Response:
code : 200
```
List of quizzes
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```
#### - Create quiz
##### - Route = `api/v1/programs/{id}/courses/{id}/quizzes`
##### Method: POST        
##### Payload:
```Json 
{
    "jwt":   "ffff",
    "Quiz content" : "dummy content"
}

```   
##### Success Response:
code : 200
```Json
{
    "status":  "created"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```
#### - Update the quiz
#### - Route = `api/v1/programs/{id}/courses/{id}/quizzes`
##### Method: PUT        
##### Payload:
```Json 
{
    "jwt":   "ffff",
    "Content" : "content"
    
    
}

```   
##### Success Response:
code : 200
```Json
{
    "status":  "updated"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```
#### - Delete the quiz
#### - Route = `api/v1/programs/{id}/courses/{id}/quizzes/{id}`
##### Method: DELETE        
##### Payload:
```Json 
{
    "jwt":   "ffff"
    
    
    
}

```   
##### Success Response:
code : 200
```Json
{
    "status":  "deleted"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```

