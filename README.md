![alt text](https://1.bp.blogspot.com/_umhSvWEgx2c/TIi1dtaEmLI/AAAAAAAAGd8/sBSY9YgRf2Y/s320/abeona.jpg)
# Abeona
The implementation in case has as scope to reveal a set of quasi-optimal routes to be followed by each driver in order to deliver the available orders successfully.
The behaviour is described as follows:
```shell
pip install -r requirements.txt
python App.py
Serving on http://0.0.0.0:8080
```
#### POST /async_obtain_routes_for
```json
INPUT:
{
    "orders": [
        {
          "id": "1",
          "order_number": "2021-1-22-1",
          "pick_up_address": "McDonald's, Strada Nicolae Bălcescu, Sibiu",
          "drop_off_address": "Strada Viitorului 2, Sibiu"
        },
        {
          "id": "3",
          "order_number": "2021-1-22-2",
          "pick_up_address": "KFC Sibiu DT, Strada Sibiului, Șelimbăr",
          "drop_off_address": "Strada Constantin Noica 23, Sibiu"
        },
        {
          "id": "4",
          "order_number": "2021-1-22-3",
          "pick_up_address": "Pardon Cafe Bar & Restaurant, Strada Cetății, Sibiu",
          "drop_off_address": "Calea Turnisorului 41, Calea Turnișorului, Sibiu"
        },
        {
          "id": "5",
          "order_number": "2021-1-22-4",
          "pick_up_address": "Pizzeria Eli's, Strada Ioan Virgil Ispas, Cisnădie",
          "drop_off_address": "Strada Teilor 90, Sibiu"
        },
        {
          "id": "6",
          "order_number": "2021-1-23-1",
          "pick_up_address": "Taco Bell, Strada Sibiului, Sibiu",
          "drop_off_address": "Calea Dumbrăvii 107, Sibiu"
        }
      ]
    ,
    "drivers": [
      {
        "id": 186,
        "first_name": "Larisa",
        "last_name": "Tartau",
        "capacity": 15,
        "current_location": "45.795418, 24.150256"
      },
      {
        "id": 459,
        "first_name": "MARIUS",
        "last_name": "___DIT",
        "capacity" : 15,
        "current_location": "45.778655, 24.144487"
      }
    ]

}
```
You'll receive as resposne the job_id:
```json
{
  "status": "started",
  "job_id": "2143b811-2043-4f3b-b5ea-4c2b9cd6988a"
}
```
This request should be fallowed by:

#### GET /async_obtain_routes_for?job_id=2143b811-2043-4f3b-b5ea-4c2b9cd6988a
```json
{
  "status": "pending",
  "job_id": "2143b811-2043-4f3b-b5ea-4c2b9cd6988a"
}
```
Initially the response will be as above, suggesting that the job is not finalized.
The same request should be reexecuted until you'll receive the intended response/result:


```json
OUTPUT:
{
  "status": "done",
  "job_id": "2143b811-2043-4f3b-b5ea-4c2b9cd6988a",
  "result": {
    "drivers_and_operations": [
      {
        "driver": {
          "capacity": 15,
          "first_name": "Larisa",
          "last_name": "Tartau",
          "current_location": "45.795418, 24.150256",
          "id": 186
        },
        "operations": [
          {
            "order": {
              "pick_up_address": "KFC Sibiu DT, Strada Sibiului, Șelimbăr",
              "drop_off_address": "Strada Constantin Noica 23, Sibiu",
              "order_number": "2021-1-22-2",
              "id": "3"
            },
            "priority": 4,
            "type": "ridicare"
          },
          {
            "order": {
              "pick_up_address": "KFC Sibiu DT, Strada Sibiului, Șelimbăr",
              "drop_off_address": "Strada Constantin Noica 23, Sibiu",
              "order_number": "2021-1-22-2",
              "id": "3"
            },
            "priority": 3,
            "type": "livrare"
          },
          {
            "order": {
              "pick_up_address": "Pardon Cafe Bar & Restaurant, Strada Cetății, Sibiu",
              "drop_off_address": "Calea Turnisorului 41, Calea Turnișorului, Sibiu",
              "order_number": "2021-1-22-3",
              "id": "4"
            },
            "priority": 2,
            "type": "ridicare"
          },
          {
            "order": {
              "pick_up_address": "Pardon Cafe Bar & Restaurant, Strada Cetății, Sibiu",
              "drop_off_address": "Calea Turnisorului 41, Calea Turnișorului, Sibiu",
              "order_number": "2021-1-22-3",
              "id": "4"
            },
            "priority": 1,
            "type": "livrare"
          }
        ]
      },
      {
        "driver": {
          "capacity": 15,
          "first_name": "MARIUS",
          "last_name": "___DIT",
          "current_location": "45.778655, 24.144487",
          "id": 459
        },
        "operations": [
          {
            "order": {
              "pick_up_address": "Taco Bell, Strada Sibiului, Sibiu",
              "drop_off_address": "Calea Dumbrăvii 107, Sibiu",
              "order_number": "2021-1-23-1",
              "id": "6"
            },
            "priority": 6,
            "type": "ridicare"
          },
          {
            "order": {
              "pick_up_address": "Pizzeria Eli's, Strada Ioan Virgil Ispas, Cisnădie",
              "drop_off_address": "Strada Teilor 90, Sibiu",
              "order_number": "2021-1-22-4",
              "id": "5"
            },
            "priority": 5,
            "type": "ridicare"
          },
          {
            "order": {
              "pick_up_address": "Taco Bell, Strada Sibiului, Sibiu",
              "drop_off_address": "Calea Dumbrăvii 107, Sibiu",
              "order_number": "2021-1-23-1",
              "id": "6"
            },
            "priority": 4,
            "type": "livrare"
          },
          {
            "order": {
              "pick_up_address": "McDonald's, Strada Nicolae Bălcescu, Sibiu",
              "drop_off_address": "Strada Viitorului 2, Sibiu",
              "order_number": "2021-1-22-1",
              "id": "1"
            },
            "priority": 3,
            "type": "ridicare"
          },
          {
            "order": {
              "pick_up_address": "McDonald's, Strada Nicolae Bălcescu, Sibiu",
              "drop_off_address": "Strada Viitorului 2, Sibiu",
              "order_number": "2021-1-22-1",
              "id": "1"
            },
            "priority": 2,
            "type": "livrare"
          },
          {
            "order": {
              "pick_up_address": "Pizzeria Eli's, Strada Ioan Virgil Ispas, Cisnădie",
              "drop_off_address": "Strada Teilor 90, Sibiu",
              "order_number": "2021-1-22-4",
              "id": "5"
            },
            "priority": 1,
            "type": "livrare"
          }
        ]
      }
    ]
  }
}
```