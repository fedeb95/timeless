from collada import *
import random


class LoaderDae:
    def __init__(self, filename, max_sounds, lowest, higher):
        self.filename = filename
        self.max_sounds = max_sounds
        self.lowest = lowest
        self.higher = higher

    def load(self):
        sounds = []
        mesh = Collada(self.filename)
        for geom in mesh.geometries:
            for primitive in geom.primitives:
                for vertex in primitive.vertex:
                    sounds.append({'position': list(vertex), 'frequency': self.get_random_freq()})
        if len(sounds) > self.max_sounds:
            return random.sample(sounds, self.max_sounds)
        else:
            return sounds

    def get_random_freq(self):
        return random.uniform(self.lowest, self.higher)
