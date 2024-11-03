from correlated_events_simulation import Event, Simulation
import random

# State, Probability of GOP win
states = [
    Event("NE", 1, 0.845),
    Event("MT", 1, 0.77475),
    Event("TX", 1, 0.769),
    Event("FL", 1, 0.7935),
    Event("OH", 1, 0.474),
    Event("WI", 1, 0.32975),
    Event("PA", 1, 0.26875),
    Event("MI", 1, 0.25875),
    Event("AZ", 1, 0.18825),
    Event("NV", 1, 0.1755),
    Event("ME", 1, 0.0175),
    Event("NJ", 1, 0.0125),
    Event("VA", 1, 0.0475),
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
max_offset_scale = 0.15
simulation = Simulation(states, max_offset_scale, False)
initial_seats = 47

for _ in range(100000):
    simulation.set_offset_scale(max_offset_scale * random.random())
    simulation.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation.total_value + initial_seats <= bucket["max"]:
            bucket["count"] += 1

for bucket_name, bucket in buckets.items():
    percentage = (bucket['count'] / 100000) * 100
    print(f"{bucket_name}: {bucket['count']} ({percentage:.2f}%)")

print(simulation.avg_offset)