## Justification For Message Passing Strategy

- Divided the Existed code with Reader & Writer Services.
    - This will help us scale independently read request wont get blocked due to intenside write operation and vice versa.
    - Also with this approach we can introduce async behaviour into writers with help of queues.  
- For the Person, Location, & Connections related (Storage Services) endpoints I have used the Rest with JSON payload. Dont want to complicate this without any strong reason.
- For Location Writer I have used the GRPC techniques as this endpoints seems to have high number on load. Also GRPC uses Protobuf which will take less CPU cycle on Mobiles & as this messages are serialized & less of TCP header it will give us a good performance & less latency.
- Also I have used Kafka in between, so Location writer will write the user location in to Kafka queues and consumer will process those messages and it write the location data into DB.

 