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
- [Users][]
- [Lessons][]


[Users]: ./docs/users.md
[Lessons]: ./docs/lessons.md



### Duplicate resource codes
| code |      description     |
|:----:|:--------------------:|
|   1  | Email already exists |
|   2  | Phone already exists |
|   3  | Lesson order already exists |


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

--- --- ---
### Exams
--- --- ---
#### Retrieve exam for a specefic lesson or course
#### method: get

##### payload:
```
{
    "program_name": "myprogram",
    "course_name": "mycourse",
    "lesson_name ": "mylesson"

}
```

##### success response
##### code 200
```
{
  "description": "This is a description of an exam",
  
    "questions": [{
    "description": "This is a description of a set of related questions",
    
    "type": "mcq",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":[
            ["correct answer",true],
            ["incorrect answer",false],
            ["incorrect answer",false],
            ["incorrect answer",false]
          ]
        } 
      ]
    },
    
    {
    "description": "This is a description of a set of related questions",
    
    "type": "multiple_right",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":[
            ["first correct answer",true],
            ["incorrect answer",false],
            ["second correct answer",true],
            ["incorrect answer",false]
          ]
        } 
      ]
    },
    
    {
    "description": "This is a description of a set of related questions",
    
    "type": "discribtive",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":"describtive answer shown to the student to make sure of his answer"
        } 
      ]
    }
    
  ]
}
```

--- --- ---



