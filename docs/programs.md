- [Programs](#Programs)

### Programs
<hr/>

### Route : 'api.ayat.com/v1/programs'

<hr/>

#### - How to add a program
##### - Method : Post
##### - payload
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
#### - How to Edit a program
##### - Method : Put
##### - payload
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
#### Success responce:
code : 200
```json
{
    "status": "edited"
}
```

#### Error responce:
##### code: 403
```json
{
    "status": "Don't have permission"
}
```


#### - How to Retrieve a program
##### - Method : Get
##### - payload

```json
{
    
}
```
#### Success responce:
##### code 200
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
##### code: 404
```json
{
    "status": "Content not found"
}
```

#### - How to Delete a program
##### - Method : Delete
##### - payload

```json
{
    "user_public_id": "fs5cfew3csd"
}
```
#### Success responce:
##### code 200:

```json
{
    "status": "Deleted"
}
```

#### Error responce:
##### Error 403:

```json
{
    "status": "Forbidden"
}
```


