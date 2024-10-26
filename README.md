# Blue Bite Assessment

## Project Summary
This assessment involved implementing specific API routes in Django. Although I had basic familiarity with Django from a few years ago, revisiting the framework and implementing the requirements posed challenges, particularly in setting up Docker and resolving initial connectivity issues. Notably, in settings.py, a typo in the database connection settings (using post instead of port) required troubleshooting, which added to the initial setup time. This assignment provided a valuable opportunity to deepen my understanding, but it required more time than I initially anticipated.

## Time Taken
Although the suggested time allotment was two hours, given the re-learning curve with Django and resolving setup issues, the overall time required was approximately four hours. Due to this extended timeframe, I prioritized completing the essential features and deferred any additional work.

## Design Choices
**Models:** I structured the models to clearly represent the batch, objects, and key-value data relationships, using ForeignKey constraints and setting appropriate unique constraints to ensure data integrity.

**Serializers:** Nested serializers were chosen to simplify data handling for nested JSON input, facilitating validation and efficient data processing.

**API Response:** For a clear response structure, the successful API returns a message rather than the full payload, keeping the response concise and user-friendly.

## Additional Information
While I aimed to incorporate unit tests for API endpoints, time constraints limited this implementation. Given more time, I would add comprehensive test cases for each route to ensure robust validation and response accuracy.

**Code Clarity:** I've added comments throughout the code to explain the logic behind various sections, ensuring that the reasoning behind design choices is clear.

**Docstrings:** Each function includes a docstring outlining its purpose, parameters, and return values, which is critical for maintaining clarity in collaborative environments.

## Conclusion
This assessment was an enriching experience that enhanced my familiarity with Django. I appreciate the opportunity to showcase my problem-solving skills and my approach to developing APIs. Please feel free to reach out if you have any questions regarding my implementation.

## Introduction

This repo includes a stub Django project. We would like you to extend this project by adding three
routes and related validation logic. Included are example files and schema for the expected JSON
request structure.

We use this test to gain insight into your approach when solving a general problem, and to
gauge your familiarity with Django and its related dependencies. So if you are unable to complete
all the requirements due to time constraints or other issues with the local environment, please
submit your partial work.

While we are a test-driven engineering team, we understand take-home assessments can be
time-consuming and do not expect unit tests for this project, though if you'd like to write some
by all means feel free!

## Data Constraints

There is a JSON Schema that describes the format of incoming API request bodies.
[It can be found  here](files/schema.json). You may use it to validate the requests.
**Alternative validation methods, such as serialization, are allowed**.

Each object record will be part of an array and will look something like this:
```json
{
  "batch_id": "71a8a97591894dda9ea1a372c89b7987",
  "objects": [
    {
      "object_id": "d6f983a8905e48f29ad480d3f5969b52",
      "data": [
        {
          "key": "type",
          "value": "shoe"
        },
        {
          "key": "color",
          "value": "purple"
        }
      ]
    },
    {
      "object_id": "1125528d300d4538a33069a9456df4e8",
      "data": [
        {
          "key": "fizz",
          "value": "buzz"
        }
      ]
    }
  ]
}
```

Object records will contain a `data` array consisting of a random assortment of `key` and `value`
pairs. The values in both `key` and `value` are not normalized, but will always be strings.

`object_id` fields should be treated as unique.

The `batch_id` value for a submitted Object should be associated to the created Object in some way.

Example request bodies can be found in [files directory](files)

## Requirements

You are welcome to use whatever amount of time you see fit on this assessment, but we do not expect
developers to spend more than two hours implementing both parts. **If you used more or less than the
two-hour allotment, please indicate how much time you used in your repo's README.**

### Part 1

* The application should accept JSON requests via a route.
    * When the application receives a new request it must be validated, parsed and (if the data is correct) stored in the database.
    * The application must be able to handle validation errors. The format of the errors is your choice so long as it is consistent and adheres to HTTP protocol standards.

### Part 2
* Add two routes for Object retrieval
  * One retrieval endpoint that returns an object for a given `object_id`.
  * One list endpoint that can be filtered based on `data` keys and/or values.

## Submission

After finishing the requirements, or reaching your time constraints, **please document any unfinished
work you would have completed if given more time**.

Feel free to add any additional information you'd like us to know about your assessment as well
(code documentation, decision process for a specific design choice etc).

Once completed, please zip your assignment and email it to your point of contact at Blue Bite. You
may alternatively send us a link to your published GitHub Repo.

**If you choose to publish your solution, please do not fork the assessment repository.**


## Local Setup

This repo includes support for spinning up Django and a local Postgres server using Docker and
Pipenv.

**You are welcome to utilize other package managers, or a simple `requirements.txt` file if
preferred.**

If you choose to utilize the included Docker+Pipenv implementation, use the following steps to
set up the local environment.

Your system needs to be able to:
 - Run `docker-compose` (you will need an up-to-date version of `docker` installed).
 - Run a `bash` script.

Everything is dockerized so as long as you are running an up-to-date version of docker
then everything will work. The automated spin up maps the app port to `8000` for
convenience.

### Basic Spin-up

Run `./scripts/run-local`

This will spin up a `postgres` container and an `app` container that is running a bare
Django app on a hot-loaded debug server. After spin-up, the command will run the database
migrations. This does **not** seed any users or super users.

### Adding Additional Dependencies

When adding a dependency to the `pipfile`, make sure to rerun `./scripts/run-local`, or run
`docker-compose build`, or Docker will not properly pull in the new dep.
