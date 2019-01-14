from openal.audio import SoundSource, SoundSink
from openal.loaders import load_wav_file
from time import sleep
import json
import sys
from writer import generate

# return a list of (filename,position) to be played
def gen_waves(sounds):
    return [(generate(sound['frequency']), sound['position']) for sound in sounds]

sounds = []
with open(sys.argv[1], 'r') as file:
    sounds = json.load(file)
res = gen_waves(sounds)
sources = [SoundSource(position=p[1]) for p in res]
for s in sources:
    s.looping = True
[sources[i].queue(load_wav_file(res[i][0])) for i in range(len(sources))]
sink = SoundSink()
sink.activate()
[sink.play(s) for s in sources]
sink.update()
while True:
    sleep(0.1)
