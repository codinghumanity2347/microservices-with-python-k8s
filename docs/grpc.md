
# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [protos/location.proto](#protos/location.proto)
    - [Location](#.Location)
    - [Status](#.Status)
  
    - [LocationService](#.LocationService)
  

<a name="protos/location.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## protos/location.proto



<a name=".Location"></a>

### Location



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| personId | [int32](#int32) |  |  |
| latitude | [int32](#int32) |  |  |
| longitude | [int32](#int32) |  |  |
| createdTime | [google.protobuf.Timestamp](#google.protobuf.Timestamp) |  |  |






<a name=".Status"></a>

### Status



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| currentState | [string](#string) |  |  |





 

 

 


<a name=".LocationService"></a>

### LocationService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| updateLocation | [.Location](#Location) | [.Status](#Status) |  |

 

GRPC End point : `localhost:30005`

How to make request 
```python
with grpc.insecure_channel('localhost:30005') as channel:
    stub = location_pb2_grpc.LocationServiceStub(channel)

    timestamp = Timestamp()
    response = stub.updateLocation(
            location_pb2.Location(personId=111, latitude=10, longitude=30, createdTime=timestamp.GetCurrentTime()))
    
```
