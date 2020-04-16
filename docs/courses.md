### Courses

<hr />

> *Note: for `creating`, `updating` and `deleting` courses user must have `admin permissions.`*

#### Retrieving program's courses

`api.ayat.com/v1/programs/{id}/courses` **`GET`**

##### Payload:

```json
{
  "jwt": "32132143432432"
}
```

##### Success Response:

code: **`200`**

```json
{
  "courses": [...]
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

#### Retrieving a specific course's data

`api.ayat.com/v1/programs/{id}/courses/{id}` **`GET`**

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
  //course data.
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

#### Creating a new course in specific program

`api.ayat.com/v1/programs/{id}/courses` **`POST`**

##### Payload:

```json
{
  "jwt": "ffff",
  "course_name": "Title",
  "course_description": "description",
  "course_order": "order"
  // other course data.
}
```

##### Success Response:

- Code: `200`

```json
{
  "status": "created"
}
```

or

```Json
{
    "status":  "<Duplicate resource codes>"
}
```

##### Error Response:

- Code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Updating course's data

`api.ayat.com/v1/programs/{id}/courses/{id}` **`PUT`**

##### Payload:

```json
{
  "jwt": "ffff"
  // which data to be updated
}
```

##### Success Response:

- Code: **`200`**

```json
{
  "status": "updated"
}
```

##### Error Response:

- Code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Deleting a course

`api.ayat.com/v1/programs/{id}/courses/{id}` **`DELETE`**

##### Payload:

```json
{
  "jwt": "ffff"
}
```

##### Success Response:

- Code: **`200`**

```Json
{
    "status":  "deleted"
}
```

##### Error Response:

- Code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```
