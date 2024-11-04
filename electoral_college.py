from correlated_events_simulation import Event, Simulation
import random

# State, Electoral Votes, Probability of DEM win
# initial_votes = 193
# states = [
#     Event("NE2", 1, 0.891),
#     Event("NM", 5, 0.912),
#     Event("VA", 13, 0.887),
#     Event("NH", 5, 0.834),
#     Event("MN", 10, 0.88),
#     Event("WI", 10, 0.557),
#     Event("MI", 15, 0.607),
#     Event("NV", 6, 0.47),
#     Event("PA", 19, 0.491),
#     Event("NC", 16, 0.367),
#     Event("GA", 16, 0.379),
#     Event("AZ", 11, 0.33),
#     Event("FL", 30, 0.116),
#     Event("TX", 40, 0.091),
#     Event("OH", 17, 0.08),
#     Event("ME2", 1, 0.128),
#     Event("IA", 1, 0.149),
# ]

# Swing States, Electoral Votes, Probability of DEM win
initial_votes = 226
states = [
    Event("WI", 10, 0.557),
    Event("MI", 15, 0.607),
    Event("NV", 6, 0.47),
    Event("PA", 19, 0.491),
    Event("NC", 16, 0.367),
    Event("GA", 16, 0.379),
    Event("AZ", 11, 0.33),
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
    "Dem Win": {"min": 270, "max": 538, "count": 0},  
    "Dem Blowout": {"min": 319, "max": 538, "count": 0},
}

simulation_independent = Simulation(states, 0.01, False)
simulation_offset_dependent = Simulation(states, 0.01, False)
simulation_very_low_variation_cutoff = Simulation(states, 0.01, True)
simulation_low_variation_cutoff = Simulation(states, 0.05, True)
simulation_mid_variation_cutoff = Simulation(states, 0.1, True)
simulation_high_variation_cutoff = Simulation(states, 0.15, True)
simulation_very_high_variation_cutoff = Simulation(states, 0.2, True)

# Indepentent simulations. Each event is independent (mostly) of the others.
for _ in range(5000):
    simulation_independent.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_independent.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Offset simulations. Each event is dependent on a global offset.
for _ in range(20000):
    simulation_offset_dependent.set_offset_scale(0.25 * random.random())
    simulation_offset_dependent.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_offset_dependent.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Cutoff simulations with very low variation. Each event happens in order of probability, with a cutoff.
for _ in range(10000):
    simulation_very_low_variation_cutoff.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_very_low_variation_cutoff.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Cutoff simulations with low variation. Each event happens in order of probability, with a cutoff.
for _ in range(15000):
    simulation_low_variation_cutoff.set_offset_scale(0.05 * random.random())
    simulation_low_variation_cutoff.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_low_variation_cutoff.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Cutoff simulations with mid variation. Each event happens in order of probability, with a cutoff.
for _ in range(20000):
    simulation_mid_variation_cutoff.set_offset_scale(0.1 * random.random())
    simulation_mid_variation_cutoff.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_mid_variation_cutoff.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Cutoff simulations with high variation. Each event happens in order of probability, with a cutoff.
for _ in range(25000):
    simulation_high_variation_cutoff.set_offset_scale(0.15 * random.random())
    simulation_high_variation_cutoff.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_high_variation_cutoff.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1

# Cutoff simulations with very high variation. Each event happens in order of probability, with a cutoff.
for _ in range(15000):
    simulation_very_high_variation_cutoff.set_offset_scale(0.2 * random.random())
    simulation_very_high_variation_cutoff.run()
    for bucket in buckets.values():
        if bucket["min"] <= simulation_very_high_variation_cutoff.total_value + initial_votes <= bucket["max"]:
            bucket["count"] += 1


total_sim_runs = (simulation_independent.total_runs 
                 + simulation_offset_dependent.total_runs 
                 + simulation_very_low_variation_cutoff.total_runs 
                 + simulation_low_variation_cutoff.total_runs 
                 + simulation_mid_variation_cutoff.total_runs 
                 + simulation_high_variation_cutoff.total_runs 
                 + simulation_very_high_variation_cutoff.total_runs)

for bucket_name, bucket in buckets.items():
    percentage = (bucket['count'] / total_sim_runs) * 100
    print(f"{bucket_name}: {bucket['count']} ({percentage:.2f}%)")
