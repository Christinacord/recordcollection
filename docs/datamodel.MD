# Data Models

## Albums

| Name       | Type | Not Null | Primary Key | Unique |
| ---------- | ---- | -------- | ----------- | ------ |
| id         | Int  | True     | Yes         | True   |
| album_name | Str  | True     | No          | False  |
| artist     | Str  | True     | No          | True   |
| year       | Int  | False    | No          | False  |
