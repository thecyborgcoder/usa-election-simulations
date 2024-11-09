from correlated_events_simulation import Event, Simulation
import random

# State+District, Probability of GOP win
states = [
    Event("Likely R", 1, 0.9),

    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),
    Event("Tossup R", 1, 0.55),

    Event("Tossup D", 1, 0.45),
    Event("Tossup D", 1, 0.45),
    Event("Tossup D", 1, 0.45),
    Event("Tossup D", 1, 0.45),
    Event("Tossup D", 1, 0.45),

    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
    Event("Likely D", 1, 0.1),
]
buckets = {
    "<200": {"min": 0, "max": 199, "count": 0},
    "200-204": {"min": 200, "max": 204, "count": 0},
    "205-209": {"min": 205, "max": 209, "count": 0},
    "210-214": {"min": 210, "max": 214, "count": 0},
    "215-219": {"min": 215, "max": 219, "count": 0},
    "220-224": {"min": 220, "max": 224, "count": 0},
    "225-229": {"min": 225, "max": 229, "count": 0},
    "230+": {"min": 230, "max": 435, "count": 0},
    "GOP Win": {"min": 218, "max": 435, "count": 0}
}
max_offset_scale = 0.1
simulation = Simulation(states, max_offset_scale, False)
initial_seats = 211

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