### Quizzes

<hr />

#### Retrieve all quizzes

`api.ayat.com/v1/programs/{id}/courses/{id}/quizzes` **`GET`**

##### Payload:

```Json
{
 "jwt": "65416584846465644546"
}
```

##### Success Response:

code: **`200`**

```json
{
  "quizes": [...]
}
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Retrieving a specific quiz

`api.ayat.com/v1/programs/{id}/courses/{id}/quizzes/{id}` **`GET`**

##### Payload:

```json
{
  "jwt": "32132143432432"
}
```

##### Success Response:

- Code: **`200`**

```json
{
  // course data.
}
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Create quiz

`api/v1/programs/{id}/courses/{id}/quizzes` **`POST`**

##### Payload:

```Json
{
    "jwt":   "ffff",
    "Quiz content" : "dummy content"
}

```

##### Success Response:

code : **`200`**

```Json
{
    "status":  "created"
}
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Update the quiz

`api/v1/programs/{id}/courses/{id}/quizzes/{id}` **`PUT`**

##### Payload:

```Json
{
    "jwt":   "ffff",
    "content" : "content"
}

```

##### Success Response:

code : **`200`**

```Json
{
    "status":  "updated"
}
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Delete the quiz

`api/v1/programs/{id}/courses/{id}/quizzes/{id}` **`DELETE`**

##### Payload:

```Json
{
    "jwt":   "ffff"
}

```

##### Success Response:

code : **`200`**

```Json
{
    "status":  "deleted"
}
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```
