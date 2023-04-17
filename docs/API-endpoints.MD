# API Documentation

## Sign up

- Endpoint path: /users/
- Endpoint method: POST

- Request shape (form):

  ```json
  {
    "account": {
      "full_name": string,
      "username": string,
      "email": string,
      "password": string,
      "password_confirmation": string
    },

  }
  ```

- Response: Account information and a token
- Response shape (JSON):
  ```json
  {
    "account": {
      "full_name": string
    },
    "token": string
  }
  ```

## Log in

- Endpoint path: /token/
- Endpoint method: POST

- Request shape (form):

  ```json
  {
    "account": {
      "username": string,
      "password": string,
    },

  }
  ```

- Response: Account information and a token
- Response shape (JSON):
  ```json
  {
    "account": {
      "full_name": string
    },
    "token": string
  }
  ```

## Log out

- Endpoint path: /token/
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Response: Always true
- Response shape (JSON):
  ```json
  true
  ```

## Get user

- Endpoint path: /token
- Endpoint method: GET

- Headers:

  - Authorization: Bearer token

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "full_name": string,
    "email": string
  }
  ```

## Create new album

- Endpoint path: /albums/
- Endpoint method: POST

- Request body:

  ```json
  {
    "album_name": string,
    "artist": string,
    "year": integer
  }
  ```

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

## Get all albums

- Endpoint path: /albums
- Endpoint method: GET

- Headers:

  - Authorization: Bearer token

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

## Get an album

- Endpoint path: /albums/id/
- Endpoint method: GET

- Headers:

  - Authorization: Bearer token

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

## Update an album

- Endpoint path: /albums/id/
- Endpoint method: PUT

- Headers:

  - Authorization: Bearer token

- Request body:

  ```json
  {
    "album_name": string,
    "artist": string,
    "year": integer
  }
  ```

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

## Delete an album

- Endpoint path: /albums/id/
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Request body:

  ```json
  {
    "album_name": string
  }
  ```

- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```
