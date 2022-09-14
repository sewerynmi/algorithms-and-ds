# API for Movie Collection Stack

One of the tasks was to create API or Single Page App for movie collection algo. Here is my solution using flat files. 

Why files ?

Collection is quite small. I guess it doesn't need a db. Everything can be done using files.
If collection need extra functionalities or grows, in-file db can be used. 

If I was rich (and that is my Final Plan), I'd use AWS, db replicas, Golden Gate, messaging queues and like 1000 EC2 instances in autoscaling group just when 2nd user access the app. 
Of course it's a joke. Let's stay with flat file and excalate it to DB if that is really requried. 

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
