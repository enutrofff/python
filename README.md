# Python different code examples

## Postgresql Installation

To install psql 

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

configure db, user, etc:

```bash
sudo -i -u postgres
psql

CREATE DATABASE mydb;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO "myuser";

CREATE TABLE cars3 (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT

insert into cars3 (brand, model, year) VALUES ('bmw', 'super-model', 2014);
```


python requirements

```bash
pip install -r requirements.txt
```

