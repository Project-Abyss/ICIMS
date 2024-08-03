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
  		- `X509-cert-xxx.pem` -> Certificate for Database Access
		- `.env` -> Environment Variables

---
## Usage

### How to use
Follow this 3 Step first. After that, you can follow “Testing: Database” to check your database connection.

**Step 1. Open command line / terminal**

**Step 2. Activate venv**
Go to the ICIMS folder and enter venv. If you have some problem about activate venv, see "Venv activation".
```
$ python -m venv [venv name]
```
(It will create a new venv automatically, if you use a new venv name.)

**Step 3. Run Django**
If you are running this application first time, please make sure you already installed fellow requirement by execute the command `pip install -r requirements.txt`.
Run the “manage.py” file. I will suggest that your current location should be same as manage.py .
```
$ python manage.py runserver
```

### Venv activation

[For Windows]
If you having an error message about "... cannot be loaded because running scripts is disabled on this system." That means you have to modify your execution policy.

To check your execution policy, use this command:
```
$ Get-ExecutionPolicy
```
If it is not “RemoteSigned” that means your system did not allow your command line execute scripts directly.

For temporary usage, you can use this command to allow current command line execute scripts directly.
```
$ Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

For multiple time usage, you can use this command to change execution policy that allow command line execute scripts directly. Please remember that you have to restart your command line after this command.
```
$ Set-ExecutionPolicy RemoteSigned
```

---
## Testing: Database

### Check the MongoDB Atlas Connection
This command will automatically create a test database as a duplicate of the production database and keep the test database after execution.
```
$ python manage.py test accounts.tests.TestDatabase.test_db_query --keepdb
```
