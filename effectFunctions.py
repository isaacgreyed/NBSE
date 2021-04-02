from pyo import *
import os


def add_reverb(fre, qu, types):
    tmpfile = "tmp.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=tmpfile)
    ifile = SfPlayer(tmpfile)

    filter = Biquad(ifile, freq=fre, q=qu, type=types).out()
    s.start()

    s.stop()


def add_distortion(byteArray, slo, mult):
    # slo from 0 to 1 and mult from 0 to 1

    with open('tmp.wav', 'wb') as tmpfile:
        tmpfile.write(byteArray)


    tmpfile = r'tmp.wav'

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename='tmpout.wav')
    ifile = SfPlayer(tmpfile)

    lfo = Sine(freq=[.2, .25], mul=.5, add=.5)
    filter = Disto(ifile, drive=lfo, slope=slo, mul=mult).out()
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

def delay(byteArray, delay1, delay2, feed, mult):


    with open('tmp.wav', 'wb') as tmpfile:
        tmpfile.write(byteArray)


    tmpfile = r'tmp.wav'

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename='tmpout.wav')
    ifile = SfPlayer(tmpfile)


    d = Delay(ifile, delay=[.15, .2], feedback=.5, mul=.4).out()

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


def allPass(byteArray, slo, mult):
    # slo from 0 to 1 and mult from 0 to 1

    with open('tmp.wav', 'wb') as tmpfile:
        tmpfile.write(byteArray)


    tmpfile = r'tmp.wav'

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename='tmpout.wav')
    ifile = SfPlayer(tmpfile)

    gt = Gate(ifile, thresh=-24, risetime=0.005, falltime=0.01, lookahead=5, mul=.2)
    rnd = Randi(min=.5, max=1.0, freq=[.13, .22, .155, .171])
    rnd2 = Randi(min=.95, max=1.05, freq=[.145, .2002, .1055, .071])
    fx = AllpassWG(gt, freq=rnd2 * [74.87, 75, 75.07, 75.21], feed=1, detune=rnd, mul=.15).out()
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


