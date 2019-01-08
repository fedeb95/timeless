from openal.audio import SoundSource,SoundSink
from openal.loaders import load_wav_file
from time import sleep
start=[
    [200,100,0],
    [0,0,50],
    [0,100,0]
]
positions=[
    [-100,-100,0],
    [0,0,-200],
    [0,-50,0]
]
files=['./A.wav','./600.wav','./2A.wav']
#sources=[SoundSource(position=p) for p in positions]
sources=[SoundSource(position=p) for p in start]
for s in sources:
    s.looping=True
[sources[i].queue(load_wav_file(files[i])) for i in range(len(sources))]
sink=SoundSink()
sink.activate()
[sink.play(s) for s in sources]
sink.update()
while True:
    [print(s.position) for s in sources]
    for i in range(len(sources)):
        p=sources[i].position
        for j in range(len(p)):
            if p[j]<positions[i][j]:
                p[j]=p[j]+1
            elif p[j]>positions[i][j]:
                p[j]=p[j]-1
        sources[i].position=p
    sink.update()
    sleep(0.1)
