### Contacts

<hr />

#### Create a complaint

`api.ayat.com/v1/contacts` **`POST`**

##### Payload:

```Json
{
    "jwt": "65416584846465644546",
    "msg_content" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```

##### Success Response:

code : **`200`**

```Json
{
    "status" : "success"
}
```

##### Error Response:

code : **`403`**

```Json
{
    "status" : "unauthorized"
}
```
