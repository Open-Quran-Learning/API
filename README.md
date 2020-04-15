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
- [Quizzes][]


[Users]: ./docs/users.md
[Lessons]: ./docs/lessons.md
[Quizzes]: ./docs/quizzes.md



### Duplicate resource codes
| code |      description     |
|:----:|:--------------------:|
|   1  | Email already exists |
|   2  | Phone already exists |
|   3  | Lesson order already exists |


<hr />    




