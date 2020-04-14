# Ayat Quran Center API

Ayat is cross-platform software with epic features ... Providing a way to up in your life and another way to meet your death happily.   
-- Still under development.
## Download 

1- Download Ayat distribution code from     
https://github.com/Ayat-Quran-Center/API.git

2- In a terminal window, navigate into your API directory. 

3- to make sure that all of the necessary Python packages (Flask and flask_sqlalchemy, for instance) are installed,  in your terminal window run:
```cmd
pip3 install -r requirements.txt
```
## Development

1- Set the environment variable FLASK_ENV to be development.    
On a Mac or on Linux, the command to do this is:
 ```cmd
export FLASK_ENV=development
```
 On Windows, the command is instead 
 ```cmd
set FLASK_ENV=development
```
2- To start developing and adding your sweet code, just navigate to ayat directory then add your \<name>.py file.

3- On \__init__.py file, import your file at the end of init file, for example:
```python
from ayat import <name>
``` 

4- Kindly add your documentation below at documentation section.

now, I can pay you a pizza and I have to pay my respects to your mother.

## Documentation

- [Users](#Users)
- [Quiz](#Quiz)

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
<hr />    

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
#### Duplicate resource codes:
| code |      description     |
|:----:|:--------------------:|
|   1  | Email already exists |
|   2  | Phone already exists |
<hr />    
### Quiz

<hr />    

#### Route: `api.ayat.com/v1/quiz`
<hr /> 

#### - how to enter quiz route
##### Method: GET        
##### Payload: 
   ```Json
{
    "jwt": "65416584846465644546",
    
}
```   
##### Success Response:
code : 202
```Json
{
    "status":  "Accepted"
}
```
##### Error Response:
code: 401
```json
{
    "error": "user is unauthorized"
}
```
#### - how to enter your quiz
##### Method: POST        
##### Payload:
```Json 
{
    "jwt":   "ffff",
    "program[id]":  "example",
    "course[id]":  "example"
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
code: 402
```json
{
    "error": "Payment Required"
}
```
#### - enter your respone in the quiz
##### Method: PUT        
##### Payload:
```Json 
{
    "jwt":   "ffff",
    "program[id]":  "example",
    "course[id]":  "example",
    "Q1":  "example",
    "Q2":  "example",
    "Q3":  "example"
    
    
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
code: 429
```json
{
    "error": " Too Many Requests"
}
```



