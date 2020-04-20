### Recitations

<hr />

> *Note: for `creating`, `updating` and `deleting` recitation user must have `admin permissions.`*


#### Creating a new recitation

`api.ayat.com/v1/recitations` **`POST`**

##### Payload:

```json
{
  "jwt": "ffff",
  "recitation_name": "Title",
  "recitation_description": "description",
  // other recitation's data.
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
    "status":  "<Duplicate resource codes: 7>"
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

#### Updating recitation's data

`api.ayat.com/v1/recitations/{id}` **`PUT`**

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


#### Retrieving recitations

`api.ayat.com/v1/recitations/` **`GET`**

##### Payload:

```json
{}
```

##### Success Response:

##### code: **`200`**

```json
{
  "recitation": [recitaion_ids]
}
```

##### Error Response:

##### code: **`404`**

```json
{
  "error": "Content not found"
}
```

<hr />

#### Retrieving a specific recitation's data

`api.ayat.com/v1/recitations/{id}` **`GET`**

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
  //recitation data.
}
```

##### Error Response:

##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

or

##### code: **`404`**

```json
{
    "error": "Content not found"
}
```

<hr />

#### Deleting a recitation

`api.ayat.com/v1/recitations/{id}` **`DELETE`**

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

<hr />

#### Subscribe to a recitation

`api.ayat.com/v1/recitations/{id}/enrollments` **`POST`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3"
}
```

#### Success responce:

##### code: **`202`**

```json
{
  "status": "enrolled"
}
```

#### Error responce:

```json
{
  "error": "<Duplicate resource codes: 5>"
}
```

or

##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Cancel subscription to a recitation

`api.ayat.com/v1/recitations/{id}/enrollments` **`DELETE`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3"
}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "success"
}
```

#### Error responce:

```json
{
  "error": "<Duplicate resource codes: 6>"
}
```

or

##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Create new assignment in a specific recitation

`api.ayat.com/v1/recitations/{id}/assignments` **`POST`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3",
  "student_ids": [student ids]
  // Data to be added

}
```

#### Success responce:

##### code: **`201`**

```json
{
  "status": "created"
}
```

#### Error responce:
##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### update an assignment in a specific recitation

`api.ayat.com/v1/recitations/{id}/assignments/{id}` **`PUT`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3",
  // assignment's data to be updated

}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "success"
}
```

#### Error responce:
##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### User gets an assignment from a specific recitation
#### TODO
`api.ayat.com/v1/recitations/{id}/assignments/filter` **`GET`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3"
}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "success"
}
```

#### Error responce:
##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />

#### Delete an assignment in a specific recitation

`api.ayat.com/v1/recitations/{id}/assignments/{id}` **`DELETE`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3"
}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "success"
}
```

#### Error responce:
##### code: **`403`**

```json
{
  "error": "user is unauthorized"
}
```

<hr />
