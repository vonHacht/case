# case - data build tool



``` 
python3 -m venv dbt-env
source dbt-env/bin/activate
```

``` 
pip install -r requirements.txt 
```

### postgresql


```
sudo -u postgres psql
```
```
CREATE USER <username> WITH PASSWORD '<password>';
CREATE DATABASE <db>;
GRANT ALL PRIVILEGES ON DATABASE <db> TO <username>;
```

```
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

```
dbt seed
```