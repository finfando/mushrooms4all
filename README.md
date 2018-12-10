# mushrooms4all

## Setup

Environment is set up using [Docker]{https://www.docker.com}.
You have to install docker and docker-compose in order to run it.

## Development environment

Development environment consists of jupyter server where we can develop the models. In order to start the jupyter server change directory to the main one and run following command:

    $  docker-compose -f .\docker-compose.dev.yml up

Notebooks are available at [http://localhost:8888](http://localhost:8888)

## Flask API

Model is deployed using Flask and can be launched using command:

    $  docker-compose -f .\docker-compose.prod.yml up

If you modified the files you should rebuild the image first:

    $  docker-compose -f .\docker-compose.prod.yml up --build --force-recreate

### Example request

API is served at host: http://localhost:5000 and is called using following example POST request:

    curl -X POST \
      http://localhost:5000/predict \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: 5c70dcc7-15c9-40b3-b677-b08df049a661' \
      -d '{
    "cap-shape": "s",
    "cap-surface": "f",
    "cap-color": "g",
    "bruises": "t",
    "odor": "p",
    "gill-attachment": "f",
    "gill-spacing": "d",
    "gill-size": "n",
    "gill-color": "k",
    "stalk-shape": "e",
    "stalk-root": "e",
    "stalk-surface-above-ring": "s",
    "stalk-surface-below-ring": "s",
    "stalk-color-above-ring": "c",
    "stalk-color-below-ring": "c",
    "veil-type": "p",
    "veil-color": "w",
    "ring-number": "t",
    "ring-type": "p",
    "spore-print-color": "k",
    "population": "n",
    "habitat": "u"
    }'

API returns a JSON with one item:

    {
        "class": "p"
    }