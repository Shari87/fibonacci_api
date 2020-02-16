Adnymics Developer Task

# Table of Contents
##### 1.  Brief Description
##### 2.  Requirements
##### 3.  How to Run
##### 4.  Request Type
##### 5.  Response Type

##### 1. Brief Description
Fibonacci Server is a RESTful web service used to serve numbers from index 0 upto a predefined number 10000

##### 2. Requirements
This service requires 
1.  Flask
2. Python 2.7+, 3.5+ (Verified on these 2 version)

##### 3. How to run
Download the repository, enter the directory and run:
- /fibonacci_server.py

This will run the service on port 8080. At this moment, the service is up and running and is also ready to serve logs into runtime.log. Also, a --help option is provided in the script
- ./fibonacci_server.py --help
Usage: fibonacci_server.py [options]

Options:

-h, --help      shows this help message and exits

-b BIND, --bind=BIND Binds, the address

-p PORT, --port=PORT Listens on this port
