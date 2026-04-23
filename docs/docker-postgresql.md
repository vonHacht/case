# Docker & Postgresql

## Start & Stop

#### Start docker containers
```
docker compose up -d
```

#### Venture into container
```
docker exec -it case-db /bin/bash
```

#### Venture into postgresql
```
psql -U postgres -d pokemon
```

#### Stop docker container
```
docker stop case-db
```
#### Rebuild container
```
docker-compose down -v
docker-compose up --build
```
## Inside postgresql

#### 📂 List all databases
```sql
\l
```

#### 🔗 Connect to a database
```sql
\c pokemon
```

#### 📋 List tables in current database
```sql
\dt
```

#### 🧱 Describe a table (schema)
```sql
\d my_table
```

#### 🔍 Query data
```sql
SELECT * FROM my_table;
```

#### 🚪 Exit psql
```sql
\q
```

#### 🧭 Bonus: Useful extras

#### List all schemas
```sql
\dn
```

#### List all users/roles
```sql
\du
```

#### Show current database
```sql
SELECT current_database();
```