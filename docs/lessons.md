### Lessons

<hr />

#### Retrieve all lessons in the course

`api.ayat.com/v1/programs/{id}/courses/{id}/lessons` **`GET`**

##### Payload:

```Json
{
    "jwt":  "32132143432432"
}
```

##### Success Response:

code : **`200`**

```
Json retrive list of lessons with IDs
```

##### Error Response:

code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Retrieve a specific lesson in the course

`api.ayat.com/v1/programs/{id}/courses/{id}/lessons` **`GET`**

##### Payload:

```Json
{
    "jwt":  "32132143432432"
}
```

##### Success Response:

code : **`200`**

```Json
{
    "name":   "lessonName",
    "order":  "1",
    "objective":  "123123",
    "content":   "content example"
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

#### Create a new lesson in the course

`api.ayat.com/v1/programs/{id}/courses/{id}/lessons` **`POST`**

##### Payload:

```Json
{
    "jwt":  "32132143432432",
    "order":  "1",
    "name":  "example",
    "objective":  "123123",
    "content":   "content example"
}
```

##### Success Response:

code : **`200`**

```Json
{
    "status":   "<Duplicate resource codes>"
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

#### Update lesson in the course

`api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}` **`PUT`**

##### Payload:

```Json
{
    "jwt":  "32132143432432",
    "order":  "1",
    "name":  "example",
    "objective":  "123123",
    "content":   "content example"
}
```

##### Success Response:

code **`200`**:

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

#### How to delete lesson from database

`api.ayat.com/v1/programs/{id}/courses/{id}/lessons/{id}` **`DELETE`**


##### Payload:

```Json
{
    "jwt":   "ffff"
}
```

##### Success Response:

code **`200`**:

```Json
{
    "status":  "deleted"
}
```
