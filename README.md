# ICIMS
> Industry Cooperation Intern Management System

---
## Github Commit Message
- `[+] <App> - <Function> -> Add <Something>`
- `[!] <App> - <Function> -> Modify <Something>`
- `[-] <App> - <Function> -> Delete <Something>`
- `[~] <App> - <Old Function Name> -> <App> - <New Function Name>`

---
## Structure
- ICIMS
	- README.md
	- requirements.txt
	- `icims` -> Django Project
		- `icims` -> Default App
		- `accounts` -> User Management
		- `journals` -> Work Record Management

---
## Testing: Database

### Check the MongoDB Atlas Connection
This command will automatically create a test database as a duplicate of the production database and keep the test database after execution.
```
$ python manage.py test accounts.tests.TestDatabase.test_db_query --keepdb
```
