from correlated_events_simulation import Event, Simulation
import random

# State+District, Probability of GOP win
states = [
    Event("AZ2", 1, 0.91),
    Event("CA40", 1, 0.91),
    Event("CO3", 1, 0.9),
    Event("CA3", 1, 0.9),
    Event("WI1", 1, 0.88),
    Event("PA1", 1, 0.87),
    Event("TX15", 1, 0.86),
    Event("NY1", 1, 0.85),
    Event("FL27", 1, 0.85),
    Event("MT1", 1, 0.83),
    Event("FL13", 1, 0.81),
    Event("WI3", 1, 0.78),
    Event("PA10", 1, 0.76),
    Event("VA2", 1, 0.74),
    Event("NJ7", 1, 0.72),
    Event("MI10", 1, 0.7),
    Event("IA1", 1, 0.69),
    Event("CA41", 1, 0.68),
    Event("AZ6", 1, 0.67),
    Event("AZ1", 1, 0.64),
    Event("NY17", 1, 0.62),
    Event("IA3", 1, 0.61),
    Event("MI7", 1, 0.6),
    Event("CA22", 1, 0.58),
    Event("AK", 1, 0.57),
    Event("WA3", 1, 0.55),
    Event("CA45", 1, 0.51),
    Event("NY19", 1, 0.5),
    Event("MI8", 1, 0.46),
    Event("OR5", 1, 0.43),
    Event("CA27", 1, 0.4),
    Event("ME2", 1, 0.39),
    Event("CO8", 1, 0.36),
    Event("PA8", 1, 0.36),
    Event("NE2", 1, 0.34),
    Event("PA7", 1, 0.29),
    Event("NY4", 1, 0.28),
    Event("CA13", 1, 0.28),
    Event("VA7", 1, 0.27),
    Event("NY22", 1, 0.23),
    Event("CA47", 1, 0.22),
    Event("OH13", 1, 0.2),
    Event("OH9", 1, 0.18),
    Event("NC1", 1, 0.18),
    Event("NM2", 1, 0.18),
    Event("MD6", 1, 0.18),
    Event("PA17", 1, 0.17),
    Event("CT5", 1, 0.16),
    Event("MN2", 1, 0.13),
    Event("NY18", 1, 0.12),
    Event("IL17", 1, 0.1),
    Event("AL2", 1, 0.09),
    Event("IN1", 1, 0.08),
    Event("NV3", 1, 0.08),
    Event("MI3", 1, 0.06),
    Event("CA9", 1, 0.06),
    Event("NH1", 1, 0.06),
    Event("TX28", 1, 0.06),
    Event("CA49", 1, 0.05),
    Event("OR4", 1, 0.05),
    Event("TX34", 1, 0.05),
    Event("KS3", 1, 0.04),
    Event("NH2", 1, 0.03),
    Event("OR6", 1, 0.03),
    Event("OH1", 1, 0.03),
    Event("WA8", 1, 0.03),
    Event("NV4", 1, 0.03),
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
max_offset_scale = 0.15
simulation = Simulation(states, max_offset_scale, False)
initial_seats = 191

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