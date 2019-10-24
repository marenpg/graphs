
class Module:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name

modules = [
    Module("Visual"),
    Module("Attention"),
    Module("Frontoparietal control"),
    Module("Somatic motor"),
    Module("Salience"),
    Module("Default"),
    Module("Limbic")
]
