##Install CockroachDB

First, you will need to download the latest version of the CockroachDB binary. On Node1, run the following command to download the binary:

1.wget https://binaries.cockroachdb.com/cockroach-latest.linux-amd64.tgz


Once the download is completed, extract the downloaded file using the following command:

2.tar -xvzf cockroach-latest.linux-amd64.tgz


Next, copy the binary from the extracted directory to the /usr/local/bin so it is accessible from the command line:

3.cp cockroach-latest.linux-amd64/cockroach /usr/local/bin/


Next, check the version of the CockroachDB using the following command:

4.cockroach version

##Build a Python App with CockroachDB

1.To install the Python psycopg2 driver, run the following command:
pip install psycopg2

2.Start the built-in SQL client:
cockroach sql --certs-dir=certs

3.In the SQL shell, issue the following statements to create the maxroach user and bank database:
CREATE USER IF NOT EXISTS maxroach;
CREATE DATABASE bank;

4.Give the maxroach user the necessary permissions:
GRANT ALL ON DATABASE bank TO maxroach;

5.Exit the SQL shell:
\q