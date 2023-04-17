# Data Models

## Accounts

| Name            | Type | Not Null | Primary Key | Unique |
| --------------- | ---- | -------- | ----------- | ------ |
| id              | Int  | True     | Yes         | True   |
| full_name       | Str  | True     | No          | False  |
| username        | Str  | True     | No          | True   |
| email           | Str  | True     | No          | True   |
| hashed_password | Str  | True     | No          | False  |

## Albums

| Name       | Type | Not Null | Primary Key | Unique |
| ---------- | ---- | -------- | ----------- | ------ |
| id         | Int  | True     | Yes         | True   |
| album_name | Str  | True     | No          | False  |
| artist     | Str  | True     | No          | True   |
| year       | Int  | False    | No          | False  |
