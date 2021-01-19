# roadmap
    "-" no implementation
    "~" partial implementation
    "+" functional implementation

    + database
      + models 0.1
      + migrations 0.1
      + unit tests 0.1
      + database filler 0.1

    + JSON/schema
      + deserialisation 0.1
      + serialisation 0.1
      + auto-fill data 0.1
      + input validation 0.1
      + unit tests 0.1

    ~ REST API
      + routes 0.1
      ~ swagger
        + routes 0.1
          - gets
            ~ query/filter
            - sort
            - count/limit
          - puts, posts, deletes
          - subscribe
          - unsubscribe
        - docs
        - examples
      + error handlers 0.1
      - integration tests (postman/newman)

    ~ front-end
      - React
        ~ components
          ~ filterable list
            - search
            - query
            - sort
          - previews
        ~ models
        ~ router
          - links
        - contexts
          - authorisation
          - theme
      - UI tests

    ~ back-end
      - functionality
        - subscriptions/listeners
      ~ authentication 0.1
      - authorisation
      - sessions and permissions

    - deploy the application
      - SSL
      - containers
      - AWS
        - limit throughput
        - limit data per hour/day/week
        - limit requests per hour/day/week

    - logging
      - ticket/comment/account history

    - notification system
