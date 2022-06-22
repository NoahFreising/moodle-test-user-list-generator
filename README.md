# Moodle User List Generator

A (very) simple script for generating a csv with test users for moodle. Intended for use in performance testing etc.

Example Usage:

```
python generate-moodle-user-csv.py --username student --firstname Student --lastname Nr. --prefix student --email @example.com -n 20 -o moodle-student-list.csv
```

Documentation of the used arguments:
    --username: The username of the user
    --firstname: The firstname of the user
    --lastname: The lastname of the user
    --prefix: The prefix of the email address
    --email: The email of the user
    --number: The number of users to generate
    --output: The output file
