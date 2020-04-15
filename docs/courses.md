### Courses
<hr />

#### Note: for `creating`, `updating` and `deleting` courses user must have `admin's permissions`

#### - Retrieving program's courses   
##### Method: `GET`
##### Route: `api.ayat.com/v1/programs/{id}/courses`
##### Payload:
```json
{
    "program_id": "public_program_id"
}
```         
##### Success Response:
- Code: `200`
```json
{
    "response": ["list of courses"]
}
```


#### - Retrieving a specific course's data
##### Method: `GET`
##### Route: `api.ayat.com/v1/programs/{id}/courses/{id}`  
##### Payload: 
```json
{
    "course_id": "public_course_id"
}
````         
##### Success Response:
- Code: `200`
```json
{
    "response": [
        course.title,
        course.description,
        course.order,
        course.program_id
    ]
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
    "course_discreption": "discreption",
    "course_order": "order",
    "program_id": "public_program_id"

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
    "course_id": "public_course_id",
    "which data to be updated"
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
    "course_id": "public_course_id"
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
