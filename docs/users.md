### Users
<hr />    

#### Route: `api.ayat.com/v1/users`
<hr />    

#### - how to login a user        
##### Method: POST        
##### Payload: 
```Json
{
    "action":   "login",
    "email": "example@gmail.com",
    "password": "123456",
}
```         
##### Success Response:
code : 200
```Json
{
    "jwt": "65416584846465644546",
    "public_id": "123123"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```
    
#### - how to register new user
##### Method: POST        
##### Payload: 
```Json
{
    "action":   "register",
    "user_id":  "example",
    "full_name":  "example",
    "email":  "example",
    "country":  "example",
    "phone":  61111,
    "profile_pic": "https://ayatsource.com/default.png",
    "birth_date":   "date",
    "gender":   "male",
    "password":   "464468",
    "registeration_date":   "20/2/2020" 
}
````         
##### Success Response:
code : 200
```Json
{
    "status":  "created"
}
```
or
```Json
{
    "status":  "<Duplicate resource codes> "
}
```

#### - how to edit user info
##### Method: PUT        
##### Payload: 
```Json 
{
    "jwt":   "ffff",
    "email":  "example",
    "country":  "example",
    "phone":  61111,
    "profile_pic": "https://ayatsource.com/default.png",
    "birth_date":   "date",
    "password":   "464468"
}
````         
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


#### - how to delete user from database
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
