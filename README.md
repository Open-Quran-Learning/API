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

now, I can pay you a pizza.

## Documentation

- [Users](#Users)
- [Lessons](#Lessons)
- [Duplicate resource codes](#Duplicate-resource-codes)
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
```Json
{
    "name":   "lessonName",
    "objective":  "123123",
    "reading_time":   "12",
}
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
    "jwt":  "32132143432432",
    "public_id":  "123123123",
    "lesson_number":  "1"
}
```         
##### Success Response:
code : 200
```Json
{
    "name":   "lessonName",
    "objective":  "123123",
    "reading_time":   "12",
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
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}`    
##### Method: POST        
##### Payload: 
```Json
{
    "jwt":  "32132143432432",
    "public_id":  "123123123",
    "lesson_number":  "1",
    "name":  "example",
    "objective":  "123123",
    "reading_time":   "12",
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


#### - Create a new lesson in the course    
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}`    
##### Method: PUT        
##### Payload: 
```Json
{
    "jwt":  "32132143432432",
    "public_id":  "123123123",
    "lesson_number":  "1",
    "name":  "example",
    "objective":  "123123",
    "reading_time":   "12",
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
##### Method: DELETE        
##### Payload: 
```Json
{
    "jwt":   "ffff",
    "public_id":  "123123123",
    "lesson_number": 2
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

### Duplicate resource codes
| code |      description     |
|:----:|:--------------------:|
|   1  | Email already exists |
|   2  | Phone already exists |
|   3  | Lesson already exists |
|   4  | Lesson number already exists |


<hr />    



