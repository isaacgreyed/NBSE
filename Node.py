class NodeList:
    __slots__ = ['_N', '_P']

    def __init__(self, effect_names = []):

        self._N = []
        self.P = []

        for i in range(len(effect_names)):
            self._N.append(effect_names[i])
            self._P.append(initParameters(i))


    def initParameters(self, index):
        if self._N[index] == 'reverb':
            setReverb()
        elif self._N[index] == 'distortion':
            setDistortion()
        elif self._N[index] == 'chorus':
            setChorus()
        elif self._N[index] == 'delay':
            setDelay()
        elif self._N[index] == 'harmonizer':
            setHarmonizer()
        elif self._N[index] == 'convolve':
            setConvolve()


    def setReverb(self, index, a = 1000, b = 5, c = 2):
        self._P[index] = [a, b, c]

    def setDistortion(self, index, a = 0.6, b = 0.7):
        self._P[index] = [a, b]

    def setChorus(self, index, a = 2, b = 4, c = 0.25, d = 0.8):
        self._P[index] = [a, b, c, d]

    def setDelay(self, index, a = 0.15, b = 0.2, c = 0.8):
        self._P[index] = [a, b, c]

    def setHarmonizer(self, index, a = 0):
        self._P[index] = [a]

    def setConvolve(self, index):
        self._P[index] = []



    def addNode(self, name):
        self._N.append(name)
        self._P.append([])
        initParameters(len(self._P)-1)



    def removeNode(self):
        self._N.pop(len(self._N-1))
        self._P.pop(len(self._N-1))



    def removeAllNodes(self):
        for i in range(len(self._N-1)):
            self._N.pop()
            self._E.pop()