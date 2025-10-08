### Devops Python Project ###

### Installation of Project 
# pip libraries: fastapi, uvicorn
# to run the project: uvicorn main:app --reload --port 8080



### Sample Requests
========= GET all users ================
curl http://localhost:8080/users
========= POST add user ================
curl -X POST http://localhost:8080/users -H "Content-Type: application/json" -d '{"name": "Charlie", "email": "charlie@example.com"}'
================ PUT update user ================
curl -X PUT http://localhost:8080/users/1 -H "Content-Type: application/json" -d '{"email": "alice@newmail.com"}'
================ DELETE user ================
curl -X DELETE http://localhost:8080/users/2
 
