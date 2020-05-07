### Programs

<hr/>

#### Create a program

`api.ayat.com/v1/programs` **`Post`**

##### Payload

```json
{

   "x-access-token": "fg5562ase84c4",
   "program_name": "<Name example>",

    "prerequisite": [
      {
        "name": "name of already exist program"
      },
      {
        "name": "name of already exist program"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "text"
      },
      {
        "type": "text"
      }
    ],

    "price": "551",

    "program_pic": "<Pic>",

    "FAQ": [
      {
        "question": "Text",
        "answer": "Text"
      },
      {
        "question": "Text",
        "answer": "Text"
      }
    ],

    "program_cover": "<Local pic>",

    "Program_description": "text example",

    "available": true

}


```

##### Success response:

##### code: **`200`**

```json
{
  "status": "created",
  "program_public_id": "e903928c-9a4c-43ca-aa56-12de83fde5a9",
}
```

#### Error responce :

##### code: **`403`**

```json
{
  "status": "Forbidden"
}
```

<hr/>

#### Edit a program

`api.ayat.com/v1/programs/{id}` **`PUT`**

##### Payload

```json

{

   "x-access-token": "fg5562ase84c4",
   "program_name": "<Name example>",

    "prerequisite": [
      {
        "name": "name of already exist program"
      },
      {
        "name": "name of already exist program"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "text"
      },
      {
        "type": "text"
      }
    ],

    "price": "551",

    "program_pic": "<Pic>",

    "FAQ": [
      {
        "question": "Text",
        "answer": "Text"
      },
      {
        "question": "Text",
        "answer": "Text"
      }
    ],

    "program_cover": "<Local pic>",

    "Program_description": "text example",

    "available": true

}


```

#### Success responce:

code: **`200`**

```json
{
  "status": "edited"
}
```

#### Error responce:

##### code: **`403`**

```json
{
  "status": "Forbidden"
}
```

<hr/>

#### How to Retrieve a program

`api.ayat.com/v1/programs/{id}` **`GET`**

##### Payload

```json
{}
```

#### Success responce:

##### code: **`200`**

```json
{
  "program_name": "name example",

  "prerequisite": [
    {
      "type": "example"
    },
    {
      "type": "example"
    }
  ],
  "program_level": "<Difficulty>",

  "program_category": [
    {
      "type": "example"
    },
    {
      "type": "example"
    }
  ],

  "price": "$$$",

  "program_pic": "<Local Pic>",

  "FAQ": [
    {
      "question": "Text",
      "answer": "Text"
    },
    {
      "question": "Text",
      "answer": "Text"
    }
  ],

  "program_cover": "<Local pic>",

  "Program_description": "text example",

  "available": "<true as a default boolean value>"
}
```

#### Error responce:

##### code: **`404`**

```json
{
  "status": "Content not found"
}
```

<hr/>

#### Delete a program

`api.ayat.com/v1/programs/{id}` **`DELETE`**

##### Payload

```json
{
  "x-access-token": "adfgv5erw85s3",
}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "Deleted"
}
```

#### Error responce:

##### code: **`403`**

```json
{
  "status": "Forbidden"
}
```
or

```json
{
  "status": "program not found"
}

```

<hr />

#### Subscribe to a program

`api.ayat.com/v1/programs/{id}/enrollments` **`POST`**

##### Payload

```json
{
  "x-access-token": "adfgv5erw85s3",
  "public_program_id": "{id}"
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
  "error": "'User is already subscribed"
}
```

or

##### code: **`403`**

```json
{
  "error": "you are a staff member"
}
```

<hr />

#### Cancel subscription to a program

`api.ayat.com/v1/programs/{id}/enrollments` **`DELETE`**

##### Payload

```json
{
  "x-access-token": "adfgv5erw85s3",
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
  "error": "User not enrolled "
}
```


