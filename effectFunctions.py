from pyo import *
import os

def delay(arg1, arg2, arg3, arg4):
    add_delay(arg1, arg2, arg3, arg4)
    remove()

def chorus(arg1, arg2, arg3, arg4):
    add_chorus(arg1, arg2, arg3, arg4)
    remove()

def distortion(arg1, arg2):
    add_distortion(arg1, arg2)
    remove()

def reverb(arg1, arg2, arg3):
    add_reverb(arg1, arg2, arg3)
    remove()

def add_reverb(fre, qu, types):
    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)

    filter = Biquad(ifile, freq=fre, q=qu, type=types).out()
    s.start()

    s.stop()

    #os.remove(tmpfile)
    #os.rename(r"tmpfile_working.wav", tmpfile)
    return None

def remove():
    os.remove('tmpfile.wav')
    os.rename(r"tmpfile_working.wav", 'tmpfile.wav')


def add_distortion(slo, mult):
    #slo from 0 to 1
    #mult from 0 to 1
    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)
    lfo = Sine(freq=[.2, .25], mul=.5, add=.5)
    filter = Disto(ifile, drive=lfo, slope=slo, mul=mult).out()
    
    s.start()

    s.stop()

    return None


def add_delay(delay1, delay2, feed, mult):
    #delay1 from 0 to 1
    #delay2 from 0 to 1
    #feed from 0 to 1
    # mult form 0 to 1

    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)

    d = Delay(ifile, delay=[delay1, delay2], feedback=feed, mul=mult).out()
    s.start()

    s.stop()

    return None



def add_chorus(d1, d2, feed, balance):

    # d1 between 0 and 5
    # d2 between 0 and 5
    # feedback doesnt matter but defaults to 0.25
    # bal from 0 to 1

    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)

    chor = Chorus(ifile, depth=[d1,d2], feedback=feed, bal=balance).out()
    s.start()

    s.stop()

    #os.remove(tmpfile)
    #os.rename(r"tmpfile_working.wav", tmpfile)
    return None
