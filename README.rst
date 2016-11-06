usage

pipe sensu event json to this and it will send you a nice report


output of json will be converted into tables like so in here
http://json.bloople.net/

history will be converted to small bars for 0's and 1's


configs:

sensu_handler.json
{


  "handlers": {   "mailer": { "type": "pipe", "command": "/etc/sensu/handlers/pymailer.py" }  }


}




sensu event example
[
  {
    "id": "ef6b87d2-1f89-439f-8bea-33881436ab90",
    "action": "create",
    "timestamp": 1460172826,
    "occurrences": 2,
    "check": {
      "type": "standard",
      "total_state_change": 11,
      "history": ["0", "0", "1", "1", "2", "2"],
      "status": 2,
      "output": "No keepalive sent from client for 230 seconds (>=180)",
      "executed": 1460172826,
      "issued": 1460172826,
      "name": "keepalive",
      "thresholds": {
        "critical": 180,
        "warning": 120
      }
    },
    "client": {
      "timestamp": 1460172596,
      "version": "0.26.0",
      "socket": {
        "port": 3030,
        "bind": "127.0.0.1"
      },
      "subscriptions": [
        "production"
      ],
      "environment": "development",
      "address": "127.0.0.1",
      "name": "client-01"
    }
  }
]
another one
  {
    "timestamp": 1477401995,
    "action": "create",
    "occurrences": 1,
    "check": {
      "total_state_change": 11,
      "history": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "2"
      ],
      "status": 2,
      "output": "No keepalive sent from client for 186 seconds (>=180)",
      "executed": 1477401995,
      "issued": 1477401995,
      "name": "keepalive",
      "thresholds": {
        "critical": 180,
        "warning": 120
      }
    },
    "client": {
      "timestamp": 1477401809,
      "version": "0.20.3",
      "subscriptions": [
        "nag_basic"
      ],
      "address": "mongo-bi-replica",
      "name": "mongo-bi-replica"
    },
    "id": "d54a71a1-095d-4ce0-b41e-02bbdcb3dc2c"
  }


to do:

logic in the mailer?
  - check sensu stash?
  - write log?
  - etc
main function : send email (MTA, Google, send through root)
  - send using gmail?
  - send using system?

output formatting nested html tables with mini graph
  - create html template for email
  - use jinja to populate it
  - history as a graph in css

