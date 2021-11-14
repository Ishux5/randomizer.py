# How to use:

-   Start **_randomizer.py_**
-   Enter the amount of possible events
-   For each event enter a description
-   The events will be randomized an Output to the console

## Syntax:

-   The amount input has to be an integer
-   The desription is not allowed to be empty

# History:

## About the history:

-   The history is stored locally
-   Future results will be appended to he current history
-   The history can be reset whe running **reset.py**
    -   input _yes_ for resetting the history

## History.json syntax:

```json
{
    "history": [
        {
            "events": {
                "event 1": "1",
                "event 2": "2"
            },
            "outcome": "event 1"
        }
    ]
}
```
