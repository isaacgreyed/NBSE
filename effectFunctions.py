from pyo import *
import os


def add_reverb(byteArray, fre, qu, types):
    with open('tmp.wav', 'wb') as tmpfile:
        tmpfile.write(byteArray)


    tmpfile = r'tmp.wav'

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename='tmpout.wav')
    ifile = SfPlayer(tmpfile)

    filter = Biquad(ifile, freq=fre, q=qu, type=types).out()
    s.start()

    with open('tmp.wav', 'rb') as originalF:
        with open('tmpout.wav', 'rb') as newF:
            newFile= newF.read()
            backpointer = originalF.read()

            originalF.close()
            newF.close()

    s.stop()

    os.remove('tmpout.wav')
    return newFile, backpointer
