# API
RESTful API using Python Flask

## Clone
```
git clone https://github.com/peter11420/api.git
```
## Usage
Start with command:
```
cd api
docker-compose up -d
```

## Users
`http://localhost:5000`
Field | Description
------|------------
name | user name
job_title | user job
email | user email
mobile | user phone number


## /user
### POST
Add user

+ Response 200 (application/json)


### GET
Get all user info

+ Response 200 (application/json)


### PUT
Update user info

+ Response 200 (application/json)


### DELETE
remove user

+ Response 200 (application/json)

