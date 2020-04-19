### Programs

<hr/>

#### Create a program

`api.ayat.com/v1/programs` **`Post`**

##### Payload

```json
{
  "JWT": "fg5562ase84c4",

  "program_name": "<Name example>",

  "prerequisite": [
    {
      "name": "name example"
    },
    {
      "name": "name example"
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

##### Success response:

##### code: **`200`**

```json
{
  "status": "created"
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
  "JWT": "adfgv5erw85s3",
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
  "JWT": "adfgv5erw85s3",
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

#### Subscribe to a program

`api.ayat.com/v1/programs/{id}/enrollments` **`POST`**

##### Payload

```json
{
  "JWT": "adfgv5erw85s3",
  "public_program_id": "{id}"
}
```

#### Success responce:

##### code: **`200`**

```json
{
  "status": "subscribed"
}
```

#### Error responce:

##### code: **`409`**

```json
{
  "error": "user already subscribed"
}
```

or

##### code: **`401`**

```json
{
  "error": "user is unauthorized"
}