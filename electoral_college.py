from correlated_events_simulation import Event, Simulation
import random

# State, Electoral Votes, Probability of DEM win
states = [
    Event("ME2", 1, 0.8912),
    Event("NM", 5, 0.9098),
    Event("VA", 13, 0.8835),
    Event("NH", 5, 0.8261),
    Event("MN", 10, 0.8723),
    Event("WI", 10, 0.5348),
    Event("MI", 15, 0.6061),
    Event("NV", 6, 0.4961),
    Event("PA", 19, 0.4838),
    Event("NC", 16, 0.3658),
    Event("GA", 16, 0.3396),
    Event("AZ", 11, 0.329),
    Event("FL", 30, 0.1148),
    Event("TX", 40, 0.0938),
    Event("OH", 17, 0.0783),
    Event("NE2", 1, 0.1178),
]
buckets = {
    "GOP by 215+": {"min": 0, "max": 161, "count": 0},
    "GOP by 155-214": {"min": 162, "max": 191, "count": 0},
    "GOP by 105-154": {"min": 192, "max": 216, "count": 0},
    "GOP by 65-104": {"min": 217, "max": 236, "count": 0},
    "GOP by 35-64": {"min": 237, "max": 251, "count": 0},
    "GOP by 15-34": {"min": 252, "max": 261, "count": 0},
    "GOP by 5-14": {"min": 262, "max": 266, "count": 0},
    "GOP by 1-4": {"min": 267, "max": 268, "count": 0},
    "Dems by 0-4": {"min": 269, "max": 271, "count": 0},
    "Dems by 5-14": {"min": 272, "max": 276, "count": 0},
    "Dems by 15-34": {"min": 277, "max": 286, "count": 0},
    "Dems by 35-64": {"min": 287, "max": 301, "count": 0},
    "Dems by 65-104": {"min": 302, "max": 321, "count": 0},
    "Dems by 105-154": {"min": 322, "max": 346, "count": 0},
    "Dems by 155-214": {"min": 347, "max": 376, "count": 0},
    "Dems by 215+": {"min": 377, "max": 538, "count": 0},
    "GOP Blowout": {"min": 0, "max": 219, "count": 0},
    "GOP Win": {"min": 0, "max": 268, "count": 0},
    "Tie": {"min": 269, "max": 269, "count": 0},
    "Dem Win": {"min": 269, "max": 538, "count": 0},  
    "Dem Blowout": {"min": 319, "max": 538, "count": 0},
}
max_offset_scale = 0.1
simulation = Simulation(states, max_offset_scale, True)
initial_votes = 192

for _ in range(100000):
    simulation.set_offset_scale(max_offset_scale * random.random())
    simulation.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

for bucket_name, bucket in buckets.items():
    percentage = (bucket['count'] / 100000) * 100
    print(f"{bucket_name}: {bucket['count']} ({percentage:.2f}%)")

print(simulation.avg_offset)