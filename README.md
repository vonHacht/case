# Case - Data Build Tool

## Run project

1. This project needs postgresql, it can either be started via the [docker container provided](docs/docker-postgresql.md) or install separately
    ```
    sudo apt update
    sudo apt install postgresql postgresql-contrib -y
    ```
2. Recommended to run Python via virtual environment 
    ``` 
    python3 -m venv dbt-env
    source dbt-env/bin/activate
    pip install -r requirements.txt
    ```
3. Build the database
    ``` 
    python3 -m nox -s database_setup -- --local-profile
    ```



