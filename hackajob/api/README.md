# API for Movie Collection Stack

## Install dependencies

`pip3 install fastapi`
`pip3 install uvicorn`

## Starting API

Go to path with `api.py` file and run command `uvicorn api:app --reload`

## Basic requests

GET on `http://localhost:8000/`
No payload, will return current movies stack

POST on `http://localhost:8000/`
With payload (JSON)
`{ "numMovies": 40, "qtyMoviesToWatch": 4, "listMoviesToWatch": [2,18,29,1] }`
Will amend current movies stack but returns positions of watched movies.
Just like requested in the task.
