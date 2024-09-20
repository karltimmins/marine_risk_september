import json
import random
from datetime import datetime, timedelta

# Define the lists of possible values
routes = [
    "Shanghai (CN) to Long Beach (US)",
    "Southampton (UK) to Singapore (SG)",
    "Cape Town (ZA) to Singapore (SG)",
    "Melbourne (AU) to Shanghai (CN)"
]

cargo_types = ["Electronics", "Automobiles", "Textiles", "Chemicals", "Furniture", "Machinery", "Food Products"]
incidents = [
    "Container ship encountered heavy fog in the Pacific Ocean. Experienced reduced visibility and navigation challenges.",
    "Engine failure in the Indian Ocean. Ship had to stop for repairs.",
    "Pirate attack in the Indian Ocean. Security measures were activated.",
    "Mechanical failure in the South China Sea. Ship had to stop for repairs.",
    "Container ship encountered Typhoon in the Pacific Ocean. Experienced 10-meter waves and 150 km/h winds."
    "Geo-political risk which has caused re-routing of cargo vessel"
]
outcomes = [
    "No damage. Cargo delayed by 1 day.",
    "Minor engine damage. Cargo delayed by 5 days.",
    "No damage. Cargo delayed by 2 days.",
    "Minor mechanical damage. Cargo delayed by 4 days.",
    "Minor hull damage. Cargo delayed by 3 days."
]

# Function to generate a random date between start and end dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Define the date range
start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-12-31", "%Y-%m-%d")

# Generate the data
data = []

for _ in range(500):
    entry = {
        "Category": "Incident Report",
        "Date": random_date(start_date, end_date).strftime("%Y-%m-%d"),
        "Route": random.choice(routes),
        "Cargo": random.choice(cargo_types),
        "Incident": random.choice(incidents),
        "Outcome": random.choice(outcomes)
    }
    data.append(entry)

# Write the data to training_data.json
with open("training_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Generated 500 JSON entries and saved to training_data.json")