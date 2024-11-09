from correlated_events_simulation import Event, Simulation
import random

# State, Probability of GOP win
states = [
    # Event("NE", 1, 0.838),
    # Event("MT", 1, 0.95),
    # Event("TX", 1, 1),
    # Event("FL", 1, 1),
    # Event("OH", 1, 1),
    Event("WI", 1, 0.48),
    Event("PA", 1, 0.6),
    Event("MI", 1, 0.51),
    Event("AZ", 1, 0.45),
    Event("NV", 1, 0.45),
    # Event("ME", 1, 0),
    # Event("NJ", 1, 0),
    # Event("VA", 1,0),
]
buckets = {
    "<49": {"min": 0, "max": 49, "count": 0},
    "50": {"min": 50, "max": 50, "count": 0},
    "51": {"min": 51, "max": 51, "count": 0},
    "52": {"min": 52, "max": 52, "count": 0},
    "53": {"min": 53, "max": 53, "count": 0},
    "54": {"min": 54, "max": 54, "count": 0},
    "55": {"min": 55, "max": 55, "count": 0},
    "56+": {"min": 56, "max": 100, "count": 0},
    "GOP Win": {"min": 50, "max": 100, "count": 0}
}
simulation = Simulation(states, 0.15, False)
initial_seats = 52

for _ in range(100000):
    simulation.set_offset_scale(0.01 * random.random())
    simulation.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation.total_value + initial_seats <= bucket["max"]:
            bucket["count"] += 1

for _ in range(100000):
    simulation.set_offset_scale(0.05 * random.random())
    simulation.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation.total_value + initial_seats <= bucket["max"]:
            bucket["count"] += 1

for bucket_name, bucket in buckets.items():
    percentage = (bucket['count'] / simulation.total_runs) * 100
    print(f"{bucket_name}: {bucket['count']} ({percentage:.2f}%)")

print(simulation.avg_offset)