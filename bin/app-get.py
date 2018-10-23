#!/usr/bin/env python

import uuid
import psycopg2

print("Content-type: text/html\n\n")


new_uuid = uuid.uuid4()
print("{id: %s}" % str(new_uuid))

conn = psycopg2.connect(database="riazantsev", user="riazantsev", password="xk41vu2", host="127.0.0.1", port="5432")
conn.close()
