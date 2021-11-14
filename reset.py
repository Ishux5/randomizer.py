from pathlib import Path
import json
import os
import pathlib

path = pathlib.Path().absolute()
historyJson = str(path) + "/history/history.json"

historyJsonTemplate = {"history": []}

reset = input("Do you want to reset the history? ")

if reset.upper() == "YES":
    with open(historyJson, "w") as writeFile:
        json.dump(historyJsonTemplate, writeFile, indent=4,
                  separators=(", ", ": "), sort_keys=False)
    print("History was Reset!")
else:
    print("Reset was canceled!")

os.system("pause")
