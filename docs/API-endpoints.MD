## API Documentation

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
