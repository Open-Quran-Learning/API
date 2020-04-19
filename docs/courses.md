### Courses

<hr />

> *Note: for `creating`, `updating` and `deleting` courses user must have `admin permissions.`*


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

##### code: `201`

```json
{
  "status": "created"
}
```

or

```Json
{
    "status":  "<Duplicate resource codes: 4>"
}
```

##### Error Response:

##### code: **`403`**

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

##### code: **`200`**

```json
{
  "status": "updated"
}
```

##### Error Response:

##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Retrieving program's courses

`api.ayat.com/v1/programs/{id}/courses` **`GET`**

##### Payload:

```json
{
  "jwt": "32132143432432"
}
```

##### Success Response:

##### code: **`200`**

```json
{
  "courses": [...]
}
```

##### Error Response:

##### code: **`403`**

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

##### code: **`200`**

```json
{
  //course data.
}
```

##### Error Response:

##### code: **`403`**

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

##### code: **`200`**

```Json
{
    "status":  "deleted"
}
```

##### Error Response:

##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```
