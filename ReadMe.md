# Dog breed detector (backend)

## Getting started

### Prerequisites
* Python 3.6
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)

### Installing
```
git clone https://gitlab.com/dog-breed-detector/dog-breed-detector-backend.git
cd dog-breed-detector-backend
pipenv install
gunicorn --bind localhost:8000 webserver
```
You can now find the server at `localhost:8000`

### Using
The server expects an image file under the key `image` in a [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) instance and will return a JSON in the format
```
{
    "breed": <breed-name>
}
```
where \<breed-name\> is a string with the name of the detected breed.