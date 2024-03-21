import random

def randomize(array):
    random.shuffle(array)
    return random.choice(array)
class RocketEngine:
    def __init__(self):
        super().__init__()
        self.engineT = None
        self.engine_Cycle = ["Gas Generator", "Staged Combustion (Oxidizer Rich)", "Staged Combustion (Fuel Rich)",
                             "Expander (Open/Bleed)", "Expander (Closed)", "Dual Expander (Open/Bleed)",
                             "Dual Expander (Closed)", "Pressure-Fed", "Full Flow Staged", "Electric Pump Fed",
                             "Combustion Tap Off", "Monopropellant (Cold Gas)", "Monopropellant (Decomposition)",
                             "Gas Core", "Droplet Core", "Liquid Core", "Solid Core", "Vapor Core", "Nuclear SaltWater",
                             "Radioisotope Engine", "MagnetoPlasmaDynamic Thruster", "Hall Effect Thruster",
                             "Gridded Ion Thruster", "Colloid Thruster", "Variable Specific Impulse Magnetoplasma Rocket (VASIMR)"]
    def EngineType(self):
        self.engineT = randomize(self.engine_Cycle)
        return self.engineT
    def PropFind