from openal.audio import SoundSource, SoundSink
from openal.loaders import load_wav_file
import openal.audio as audio
from time import sleep
from loader_dae import LoaderDae
import json
import sys
from writer import generate,remove
import atexit

# return a list of (filename,position) to be played
def gen_waves(sounds):
    return [(generate(sound['frequency']), sound['position']) for sound in sounds]

def exit_handler():
    remove([sound[0] for sound in res])
    audio.alc.alcCloseDevice(device)

if len(sys.argv) < 5:
    print('Usage: python3 player.py filename.dae samples lowest_frequency highest_frequency')
    sys.exit(-1)

# magic for openal to use default audio output
device_name = audio.alc.alcGetString(None,audio.alc.ALC_DEFAULT_DEVICE_SPECIFIER)
device = audio.alc.alcOpenDevice(device_name)

# cleanup device and temp files
atexit.register(exit_handler)

loader = LoaderDae(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
res = gen_waves(loader.load())

sources = [SoundSource(position=p[1]) for p in res]
for s in sources:
    s.looping = True
[sources[i].queue(load_wav_file(res[i][0])) for i in range(len(sources))]
sink = SoundSink()
sink.activate()
print(len(sources))
print(res)
[sink.play(s) for s in sources]
sink.update()
while True:
    sleep(0.1)