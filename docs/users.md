### Users

<hr />

#### Retrieve all users

`api.ayat.com/v1/users` **`GET`**

##### Payload:

```Json
{
    "jwt": "65416584846465644546"
}
```

##### Success Response:

code : **`200`**

```Json
{
    "users": [...] 
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

#### Retrieve a user

`api.ayat.com/v1/users/{id}` **`GET`**

##### Payload:

```Json
{
    "jwt": "65416584846465644546",
    "public_id": "123123
}
```

##### Success Response:

code : **`200`**

```Json
{
    //user data.
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
    "jwt": "65416584846465644546",
    "public_id": "123123"
    //other user data.
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

#### Create a new (inactive) user

`api.ayat.com/v1/users` **`POST`**

##### Payload:

```Json
{
    "action":   "register",
    "user_id":  "example",
    "full_name":  "example",
    "email":  "example",
    "country":  "example",
    "phone":  61111,
    "profile_pic": "https://ayatsource.com/default.png",
    "birth_date":   "date",
    "gender":   "male",
    "password":   "464468",
    "registeration_date":   "20/2/2020"
}
```

##### Success Response:

code : **`200`**

```Json
{
    "status":  "created"
}
```

or

```Json
{
    "status":  "<Duplicate resource codes> "
}
```

<hr />

#### Update user data

`api.ayat.com/v1/users/{id}` **`PUT`**

##### Payload:

```Json
{
    "jwt":   "ffff",
    "email":  "example",
    "country":  "example",
    "phone":  61111,
    "profile_pic": "https://ayatsource.com/default.png",
    "birth_date":   "date",
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
    "status":  "<Duplicate resource codes>"
}
```

<hr />

#### Delete a user

`api.ayat.com/v1/users/{id}` **`DELETE`**

##### Payload:

```Json
{
    "jwt":   "ffff"
}
```

##### Success Response:

code **`200`**

```Json
{
    "status":  "deleted"
}
```
