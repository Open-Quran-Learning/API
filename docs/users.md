### Users

#### Any "x-access-token" should be added to the header of the token not the body
#### Any "public_id" can be retrieved from the route, you don't have to put it inside the payload


<hr />

#### Retrieve all users

`api.ayat.com/v1/users` **`GET`**

##### Header:

```Json
{
    "x-access-token": "65416584846465644546"
}
```

##### Success Response:

code : **`200`**

```Json
{
    
  "users": [
    {
      "birth_date": "Sat, 16 May 2015 00:00:00 GMT",
      "country_name": "example",
      "email": "ex1pleamssdasd",
      "gender": false,
      "is_activated": false,
      "phone_number": "612s1211",
      "profile_picture": "2d",
      "public_id": "40dd1b7a-96c2-4f73-9e1c-dc22bdbb3e56",
      "registeration_date": "Sat, 16 May 2015 00:00:00 GMT",
      "type": "staff"
    },
    {
      "birth_date": "Sat, 16 May 2015 00:00:00 GMT",
      "country_name": "example",
      "email": "examplsdfeasdasd",
      "gender": false,
      "is_activated": false,
      "phone_number": "611211",
      "profile_picture": "2d",
      "public_id": "0758ef45-bde5-41f6-b80e-6188b8022183",
      "registeration_date": "Sat, 16 May 2015 00:00:00 GMT",
      "type": "staff"
    },
      
  ]

}
```

##### Error Response:

code: **`403`**

```json
{
  "message": "user is unauthorized"
}
```

<hr />

#### Retrieve a user

`api.ayat.com/v1/users/{id}` **`GET`**

##### Header:

```Json
{
    "x-access-token": "65416584846465644546"
}
```



##### Success Response:

code : **`200`**

```Json
{
   "user": {
    "birth_date": "Sat, 16 May 2015 00:00:00 GMT",
    "country_name": "example",
    "email": "examplsdfeasdasd",
    "gender": false,
    "is_activated": false,
    "phone_number": "611211",
    "profile_picture": "2d",
    "public_id": "0758ef45-bde5-41f6-b80e-6188b8022183",
    "registeration_date": "Sat, 16 May 2015 00:00:00 GMT",
    "type": "staff"
  }
}
```

##### Error Response:

code: **`403`**

```json
{
  "message": "user is unauthorized"
}
```

<hr />

#### Login

`api.ayat.com/v1/users` **`POST`**

##### Payload:

```Json
{
    "action":   "login",
    "email": "example@gmail.com",
    "password": "123456",
}
```

##### Success Response:

code : **`200`**

```Json
{
  "birth_date": "Sat, 16 May 2015 00:00:00 GMT",
  "country_name": "example",
  "email": "explsaddfeasdasd",
  "gender": false,
  "name": "example",
  "phone_number": "123",
  "profile_picture": "2d",
  "public_id": "735b3f64-afcf-4b42-b255-14bf8b3a5bc0",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```

##### Error Response:

code: **`403`**

```json
{
  "message": "user is unauthorized"
}
```
or
code: **`404`**

```json
{
  "message": "user not found"
}
```
or
code: **`404`**

```json
{
  "message": "invalid password"
}
```


<hr />

#### Create a new (inactive) user

`api.ayat.com/v1/users` **`POST`**

##### Payload:

```Json
{
    "action":   "register_student",
    "full_name":  "example",
    "email":  "explsaddfeasdasd",
    "country":  "example",
    "phone":  "123",
    "profile_pic": "2d",
    "birth_date":   "2015-05-16",
	  "gender": false,
    "password":   "464468",
    "registeration_date":   "2015-05-16",
    "guardian_email" : "111d19",
    "guardian_phone" : "11d119"
}
```
or

```Json
{
    "action":   "register_staff",
    "full_name":  "example",
    "email":  "explsaddfeasdasd",
    "country":  "example",
    "phone":  "123",
    "profile_pic": "2d",
    "birth_date":   "2015-05-16",
  	"gender": false,
    "password":   "464468",
    "registeration_date":   "2015-05-16",
    "permission_name": "example <teacher>"
}
```

##### Success Response:

code : **`200`**

```Json
{
    "status":  "created",
    "public_id": "example"
}
```

or

```Json
{
    "status":  "1"
}
```
or

```Json
{
    "status":  "2"
}
```

<hr />

#### Update user data

`api.ayat.com/v1/users/{id}` **`PUT`**

##### Payload:

```Json

{
    "x-access-token": "65416584846465644546",
    "full_name":  "exaaklsfmple",
    "email":  "edlsdfdkfdfeasdasd",
    "country":  "exsdkf123ample",
    "phone":  "3211kd23",
    "profile_pic": "https://ayatsource.com/default.png",
    "birth_date":   "2015-05-16",
    "password":   "464468"
}
```

##### Success Response:

code **`200`**

```Json
{
    "status":  "updated"
}
```

or
```Json
{
    "status":  "1"
}
```
or

```Json
{
    "status":  "2"
}
```
<hr />

#### Delete a user

`api.ayat.com/v1/users/{id}` **`DELETE`**

##### Payload:

```Json
{
    "x-access-token":   "ffff"
}
```

##### Success Response:

code **`200`**

```Json
{
    "status":  "deleted"
}
```
or

```Json
    {"status": "user is unauthorized"}
```
or 
```Json
    {"status": "no user found"}
```

