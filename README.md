# Attractions Finder Microservice
Microservice that finds attractions 

## Requesting Data from the Microservice

To request data from this microservice, an HTTP GET request must be made to its endpoint at http://localhost:5000/search. The request should include a JSON object with a location field specifying the location to search for attractions near. The location can be either a city or a city and state.

Example Call:

```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"location": "New York City"}' \
  http://localhost:5000/search
```
The microservice will use the BookingCOM API to search for attractions near the specified location. The data obtained from the BookingCOM API will be sent back within the HTTP response.

## Receiving Data from the Microservice

The data returned by the microservice will be in JSON format and will include all the search results. The search results will include nearby destinations as well as attractions. Each destination and attraction will be represented as a JSON object with fields for the name and location. The data will be returned in the body of the HTTP response, and the response will include a status code indicating the success or failure of the request.

## UML sequence diagram

![Untitled](https://github.com/arcanda3/NP_project/assets/147088921/ba49064d-ac3b-4f0e-9432-542a22c7a04f)
