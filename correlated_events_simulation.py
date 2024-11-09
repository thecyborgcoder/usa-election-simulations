import random
import numpy as np

class Event:
    """
    Represents an event with a name, value, and probability of occurrence.
    """
    def __init__(self, name, value, probability):
        self.name = name
        self.value = value
        self.probability = probability

class Simulation:
    """
    A simulation of the outcomes of a series of correlated events.
    """
    def __init__(self, events, offset_scale, ordered_cutoff = False):
        """
        Initializes the Simulation instance.

        Attributes:
            events (list): A list of event objects.
            offset_scale (float): A scaling factor for the offset. Determine global_offset on rugular run, and event_offset on ordered cutoff run.
            ordered_cutoff (bool): A flag indicating whether to use an ordered cutoff. Defaults to False.
            max_value (float): The sum of the 'value' attributes of all events.
            outcome_occurances (dict): A dictionary to track the occurrences of each outcome.
            total_runs (int): The total number of simulation runs.
            avg_offset (float): The average offset value.
        """
        self.events = events
        self.offset_scale = offset_scale
        self.ordered_cutoff = ordered_cutoff
        self.max_value = sum(event.value for event in events)
        self.outcome_occurances = {}
        self.total_runs = 0
        self.avg_offset = 0

    def run(self):
        self.total_runs += 1
        if self.ordered_cutoff:
            return self._ordered_cutoff_run()
        else:
            return self._regular_run()
    
    def _regular_run(self):
        total_value = 0
        global_offset = np.random.normal(0, self.offset_scale)
        adjustment_to_center = -self.avg_offset * random.random()
        global_offset += adjustment_to_center
        self.avg_offset += global_offset  
        for event in self.events:
            adjusted_probability = max(0, min(1, event.probability + global_offset))
            event.result = random.random() < adjusted_probability
            total_value += event.value if event.result else 0
        self.total_value = total_value
        return total_value
    
    def _ordered_cutoff_run(self):
        total_value = 0
        # cutoff = ( max(0, min(1, np.random.normal(0.5, 0.15) ) ) + random.random() ) / 2
        # cutoff = ( max(0, min(1, np.random.normal(0.5, 0.12) ) ) + max(0, min(1, np.random.normal(0.5, 0.2) ) ) + random.random() ) / 3
        # cutoff = random.random()
        cutoff = max(0, min(1, np.random.normal(0.5, 0.14) ) )
        for event in self.events:
            event_offset = np.random.normal(0, self.offset_scale)
            adjustment_to_center = -self.avg_offset * random.random()
            event_offset += adjustment_to_center
            self.avg_offset += event_offset 
            adjusted_probability = max(0, min(1, event.probability + event_offset))
            event.result = adjusted_probability > cutoff
            total_value += event.value if event.result else 0
        self.total_value = total_value
        return total_value
    
    def set_offset_scale(self, offset_scale):
        self.offset_scale = offset_scale
    
    def _record_outcome(self):
        outcome_key = tuple(event.result for event in self.events)
        if outcome_key in self.outcome_occurances:
            self.outcome_occurances[outcome_key] += 1
        else:
            self.outcome_occurances[outcome_key] = 1
    
