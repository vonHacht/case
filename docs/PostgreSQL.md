# PostgreSQL

Running requires PostgreSQL

Running on 


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