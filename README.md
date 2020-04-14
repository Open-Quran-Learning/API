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
- [Courses](#Courses)

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



### Courses
<hr />


#### - Retrieving program's courses   
##### Method: `GET`
##### Route: `api.ayat.com/v1/programs/{id}/courses`
##### Payload:
```json
{
    "program_id": "int"
}
```         
##### Success Response:
- Code: `200`
```json
{
    "status": "HTTP_200_OK"
}
```
##### Error Response:
- Code: `404`
```json
{
    "error": "Program not found"
}
```  


#### - Retrieving a specific course's data
##### Method: `GET`
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}`  
##### Payload: 
```json
{
    "course": "int"
}
````         
##### Success Response:
- Code: `200`
```json
{
    "status":  "HTTP_200_OK"
}
```
##### Error Response:
- Code: `404`
```json
{
    "error": "Course not found"
}
```


#### - Creating a new course in specific program
##### Method: `POST`
##### Route: `api.ayat.com/v1/programs/{id}/courses`
##### Payload: 
```json 
{
    "jwt":   "ffff",
    "course_name": "Title",
    "course_discreption": "discreption"

}
````         
##### Success Response:
- Code: `201`
```json
{
    "status":  "created"
}
```
or
```Json
{
    "status":  "<Duplicate resource codes>"
}
```
##### Error Response:
- Code: `403`
```json
{
    "error": "forbidden"
}
```  


#### - Updating course's data
##### Method: `PUT`
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}`
##### Payload: 
```json
{
    "jwt":   "ffff",
    // which data to be updated
}
````         
##### Success Response:
- Code: `200` 
```json
{
    "status":  "updated"              
}
```
##### Error Response:
- Code: `403`
```json
{
    "error": "forbiddend"
}
```
or
- Code: `204`
```json
{
    "error": "No content found"
}
```


#### - Deleting a course
##### Method: `DELETE`
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}`
##### Payload: 
```json
{
    "jwt":   "ffff",
    "course_id": "course's pk"
}
````         
##### Success Response:
- Code: `200` 
```Json
{
    "status":  "deleted"              
}
```
##### Error Response:
- Code: `403`
```json
{
    "error": "forbidden"
}
```


#### Duplicate resource codes:
| code  |      description      |
|:-----:|:---------------------:|
|   60  | Course already exists |

<hr />
