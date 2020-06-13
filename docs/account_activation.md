### Account_activation routes 

<hr/>

#### Ask for acount confirmation

`api.ayat.com/v1/users/<public_id>/confirm`  **`GET`**

##### Payload:

```Json
{}

```
##### Success Response:

code : **`200`**

```Json
{
   "status":"message sent" 
}
```
##### Error Response:

code: **`403`**

```json
{
  "status": "user not found"
}
```
<hr/>

####  Acount confirmation link

`api.ayat.com/v1/users/<public_id>/confirm/<token>` **`GET`**

##### Payload:

```Json
{}

```
##### Success Response:

code : **`200`**

```Json
{
   "status":"confirmed" 
}
```
##### Error Response:

```json
{
  "status": "token has expired"
}
```
##### Error Response:

```json
{
  "status": "token is damaged"
}
```



