import math        #import needed modules
import wave


def generate(frequency):
    bitrate = 44100  # number of frames per second/frameset.
    numberofframes = int(bitrate / frequency)
    phase = ( bitrate / frequency ) - numberofframes
    wavedata = ''

    #generating wawes
    for x in range(numberofframes):
        wavedata += chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + phase))

    f = wave.open(str(frequency)+'.wav', 'w')
    f.setframerate(44100)
    f.setnchannels(1)
    f.setsampwidth(1)
    f.writeframes(wavedata.encode())
    f.close()
    return str(frequency)+'.wav'
