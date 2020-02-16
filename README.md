Adnymics Developer Task

# Table of Contents
##### 1.  Brief Description
##### 2.  Requirements
##### 3.  How to Run
##### 4.  Request Msg Format
##### 5.  Response Msg Format


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



##### 4. Request Message format
The request message is of the following format:

GET /fib/first_idx/end_idx, where
- first_idx represents the start index and end_idx represents the end index. Both the indexes are non-negative numbers

The output can be obtained by typing the following command in the terminal:
- $ curl -i localhost:8080/fib/3/5

On typing the above command, the output would be a JSON array [2,3,5] in the body of the output with a status code of 200 in 
the header

##### 5. Response Message Format
Response is a status code reported in a HTTP header and a JSON array
