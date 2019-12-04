# Django library api 

This project contains two databases that are replicated. The first database is the master, and the second is the slave database. Writing data occurs through the master, and reading through the slave. Replication reduces the reading load and increases the reliability of the system, it can be upgraded by increasing the amount of slave and this will further increase reliability and performance.

## How to start this project?


To start Django server you need run this command


```sh
$ docker-compose up
```

After the first start, a migrating occurs that starts the data generator.

### Project URLs
* Get specific reader by the reader id, readers/:id/:
    * GET http://localhost:8000/api/readers/2
    
        ```
        {
          "id": 2,
          "first_name": "Brian",
          "last_name": "Wilson",
          "books": [
            {
              "id": 3,
              "title": "Persevering non-volatile installation",
              "author": "Cristina Branch"
            },
            {
              "id": 4,
              "title": "Switchable 4thgeneration framework",
              "author": "Ricardo Nguyen"
            }
          ]
        }
        ```
* Get CSV file contaning all entities of this project:
    * GET http://localhost:8000/api/data/csv