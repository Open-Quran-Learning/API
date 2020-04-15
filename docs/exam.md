### Exam 
--- --- ---

--- --- --- 
#### Retrieve exam for a specefic lesson or course 
#### Route: api.ayat.com/v1/programs/{id}/exams
--- --- ---
##### method: get 
##### payload:
```json
{

    "jwt": "65416584846465644546"

}

```

##### success response 
##### code: 200

```json
{
  "description": "This is a description of an exam",
  
    "questions": [{
    "description": "This is a description of a set of related questions",
    
    "type": "mcq",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":[
            ["correct answer",true],
            ["incorrect answer",false],
            ["incorrect answer",false],
            ["incorrect answer",false]
          ]
        } 
      ]
    },
    
    {
    "description": "This is a description of a set of related questions",
    
    "type": "multiple_right",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":[
            ["first correct answer",true],
            ["incorrect answer",false],
            ["second correct answer",true],
            ["incorrect answer",false]
          ]
        } 
      ]
    },
    
    {
    "description": "This is a description of a set of related questions",
    
    "type": "discribtive",
    "content": [
          {
          "question":"What is the correct answer for this question?",
          "answers":"describtive answer shown to the student to make sure of his answer"
        } 
      ]
    }
    
  ]
}
```

--- --- ---
#### Create exam for a specefic lesson or course 
--- --- ---
##### Route: api.ayat.com/v1/programs/exams
##### method: POST 
##### payload:

```json
{

    "jwt": "65416584846465644546",
    
    
  "exam":{
    "description": "This is a description of an exam",

      "questions": [{
      "description": "This is a description of a set of related questions",

      "type": "mcq",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":[
              ["correct answer",true],
              ["incorrect answer",false],
              ["incorrect answer",false],
              ["incorrect answer",false]
            ]
          } 
        ]
      },

      {
      "description": "This is a description of a set of related questions",

      "type": "multiple_right",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":[
              ["first correct answer",true],
              ["incorrect answer",false],
              ["second correct answer",true],
              ["incorrect answer",false]
            ]
          } 
        ]
      },

      {
      "description": "This is a description of a set of related questions",

      "type": "discribtive",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":"describtive answer shown to the student to make sure of his answer"
          } 
        ]
      }

    ]
  }

}
```
##### success response 
##### code 200:
```json
{
    "status":  "created",
    "exam_id": "id"
}
```
##### or 
```json
{
    "status":  "already_exists"
}
```

##### no permission
##### code 403:
```json
{
    "status":  "no permission"
}
```
--- --- ---
#### update existed exam for a specefic lesson or course
#### Route: api.ayat.com/v1/programs/{id}/exams/{id}
#### the flow is as following:
- get the desired exam json file 
- modify it in the front end 
- send the modified one to the back end again 
#### the following API is the third step which sending the updated exam.
--- --- ---
##### method: PUT 
##### payload:

```json
{
    "jwt": "65416584846465644546",
    
    
    "exam":{
    "description": "This is a description of an exam",

      "questions": [{
      "description": "This is a description of a set of related questions",

      "type": "mcq",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":[
              ["correct answer",true],
              ["incorrect answer",false],
              ["incorrect answer",false],
              ["incorrect answer",false]
            ]
          } 
        ]
      },

      {
      "description": "This is a description of a set of related questions",

      "type": "multiple_right",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":[
              ["first correct answer",true],
              ["incorrect answer",false],
              ["second correct answer",true],
              ["incorrect answer",false]
            ]
          } 
        ]
      },

      {
      "description": "This is a description of a set of related questions",

      "type": "discribtive",
      "content": [
            {
            "question":"What is the correct answer for this question?",
            "answers":"describtive answer shown to the student to make sure of his answer"
          } 
        ]
      }

    ]
  }

}
```
##### success response 
##### code 200:
```json
{
    "status":  "updated"
}
```
##### or 
```json
{
    "status":  "not_existed"
}
```
##### no permission
##### code 403:
```json
{
    "status":  "no permission"
}
```

--- --- --- 
#### delete exam from a specefic lesson or course 
#### Route: api.ayat.com/v1/programs/{id}/exams/{id}
--- --- ---

##### method: DELETE 
##### payload:
```json
{

    "jwt": "65416584846465644546"

}

```
##### success response 
##### code 200:
```json
{
    "status":  "deleted"
}
```
##### no permission
##### code 403:
```json
{
    "status":  "no permission"
}
```
