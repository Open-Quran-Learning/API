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
