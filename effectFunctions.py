from pyo import *
import os

def delay():
    add_delay(1.2, 1.6, 0.8)
    remove()

def chorus():
    add_chorus(2, 4, 0.25, 0.8)
    remove()

def distortion():
    add_distortion(0.6, 0.75)
    remove()

def reverb():
    add_reverb(1000, 5, 2)
    remove()

def harmonizer():
    add_harmonizer(2)
    remove()

def convolve():
    add_convolve()
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


def add_distortion(slo, hard):
    #slo from 0 to 1
    #hard from 0 to 1
    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)
    filter = Disto(ifile, drive=hard, slope=slo, mul=0.15).out()
    
    s.start()

    s.stop()

    return None


def add_delay(delay1, delay2, feed):
    #delay1 from 0 to 1
    #delay2 from 0 to 1
    #feed from 0 to 1
    

    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)

    d = Delay(ifile, delay=[delay1, delay2], feedback=feed, mul=0.4).out()
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



def add_harmonizer(trans):

    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile)

    harm = Harmonizer(ifile, transpo=trans, winsize=0.05).out(1)
    s.start()

    s.stop()

    #os.remove(tmpfile)
    #os.rename(r"tmpfile_working.wav", tmpfile)
    return None



def add_convolve():
    tmpfile = r"tmpfile.wav"

    s = Server(audio="offline").boot()
    filedur = sndinfo(tmpfile)[1]

    s.recordOptions(dur=filedur, filename=r"tmpfile_working.wav")
    ifile = SfPlayer(tmpfile,speed=[.999,1])

    a = Convolve(ifile, SndTable(SNDS_PATH+'/accord.aif'), size=100, mul=.2).out()
    s.start()

    s.stop()

    #os.remove(tmpfile)
    #os.rename(r"tmpfile_working.wav", tmpfile)
    return None


