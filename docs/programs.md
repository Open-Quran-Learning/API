### Programs

#### Any "x-access-token" should be added to the header of the token not the body
#### Any "public_id" can be retrieved from the route, you don't have to put it inside the payload

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
        "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
      },
      {
        "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "tessxt"
      },
      {
        "type": "tesss2xt"
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

    "available": true,
    "is_open_to_public": true,
    "start_date" : "2015-05-05",
    "end_date" : "2015-05-05",
    "requirement":{
    	"min_age": 5,
    	"max_age": 20,
    	"gender" : false},
    
    "skills":[
    	{"name" : "sdf"},
    	{"name":"hello"}
    	]

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
        "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
      },
      {
        "public_program_id": "e885f927-2b95-4a27-b1c4-223d21f429d0"
      }
    ],
    "program_level": "<Difficulty>",

    "program_category": [
      {
        "type": "tessxt"
      },
      {
        "type": "tesss2xt"
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

    "available": true,
    "is_open_to_public": true,
    "start_date" : "2015-05-05",
    "end_date" : "2015-05-05",
    "requirement":{
    	"min_age": 5,
    	"max_age": 20,
    	"gender" : false},
    
    "skills":[
    	{"name" : "sdf"},
    	{"name":"hello"}
    	]

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
  "FAQ": [
    {
      "answer": "Text",
      "question": "Text"
    },
    {
      "answer": "Text",
      "question": "Text"
    }
  ],
  "Program_description": "text example",
  "available": true,
  "end_date": "Tue, 05 May 2015 00:00:00 GMT",
  "is_open_to_public": true,
  "prerequisite": [
    {"public_program_id":"public_program_id example"},
    {"public_program_id":"public_program_id example"}
    ],
  "price": "551",
  "program_category": [
    {
      "type": "tessxt"
    },
    {
      "type": "tesss2xt"
    }
  ],
  "program_cover": "<Local pic>",
  "program_level": "<Difficulty>",
  "program_name": "<Name example>",
  "program_pic": "<Pic>",
  "public_program_id": "c8a3608e-bf88-489a-ae63-4e849330d5d6",
  "requirement": {
    "requirement": {
      "gender": false,
      "max_age": 20,
      "min_age": 5
    }
  },
  "skills": [
    {
      "name": "sdf"
    },
    {
      "name": "hello"
    }
  ],
  "start_date": "Tue, 05 May 2015 00:00:00 GMT"
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

### Get all programs

`api.ayat.com/v1/programs` **`GET`**

```json

{
  "programs": [
    {
      "Program_description": "text example",
      "available": true,
      "end_date": "Tue, 05 May 2015 00:00:00 GMT",
      "is_open_to_public": true,
      "price": "551",
      "program_category": [
        {
          "type": "tessxt"
        },
        {
          "type": "tesss2xt"
        }
      ],
      "program_cover": "<Local pic>",
      "program_level": "<Difficulty>",
      "program_name": "<Name example>",
      "program_pic": "<Pic>",
      "public_program_id": "62eb63f1-e4d9-41b8-a1dd-fc6ecbee9807",
      "start_date": "Tue, 05 May 2015 00:00:00 GMT"
    },
    {
      "Program_description": "text example",
      "available": true,
      "end_date": "Tue, 05 May 2015 00:00:00 GMT",
      "is_open_to_public": true,
      "price": "551",
      "program_category": [
        {
          "type": "tessxt"
        },
        {
          "type": "tesss2xt"
        }
      ],
      "program_cover": "<Local pic>",
      "program_level": "<Difficulty>",
      "program_name": "<Name example>",
      "program_pic": "<Pic>",
      "public_program_id": "c8a3608e-bf88-489a-ae63-4e849330d5d6",
      "start_date": "Tue, 05 May 2015 00:00:00 GMT"
    }


```

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


