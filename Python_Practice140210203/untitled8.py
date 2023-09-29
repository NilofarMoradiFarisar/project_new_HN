import sys
from pathlib import Path
import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
path = Path(r'C:\Users\Nilofar\Desktop\Python_Practice140210203')
with open(path, "w") as f:
    json.dump(data , f)