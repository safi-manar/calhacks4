# calhacks4 
<b>Image Annotation and Translation</b>

A CalHacks 4.0 project. Uses Google Cloud APIs to store and annotate user-uploaded images and translate corresponding annotations.


## Documentation
### POST /api/v1/photo
- Request: Base64 encoded photo
  ```
  { 
    "photo" : "/9j/4AAQSkZJRgABAQEASABIAAD/4QCYRXhpZgAASUkqAAgAAAAFABoBBQABAAAASgAAABsBBQAB"
  }
  ```
- Response
  ```
  {
    "uuid" : "47a36c23-2a3a-43d6-8a7f-8f8afbec8b6b"
  }
  ```
### DELETE /api/v1/photo/\<id>
### GET /api/v1/photo/\<id>
- Optional query parameters. For full list of languages, see [here](https://cloud.google.com/translate/docs/languages).
  - `source`: Source language, e.g. en
  - `target`: Target language, e.g. fr
- Response
  ```
  {
    "dest_labels": [
        "犬",
        "哺乳類のような犬",
        "草"
    ],
    "source_labels": [
        "dog",
        "dog like mammal",
        "grass"
    ]
  }
  ```
