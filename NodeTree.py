class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_num: int, output_num: int, inputs: list<EffectNode>, outputs: list<EffectNode>):
        self.function   = function   #function to be called to apply effect, should always return audio
        self.input_num  = input_num  #number of inputs function requires
        self.output_num = output_num #number of outputs function returns
        self.inputs     = inputs     #what inputs to pass to function, think of lower in the tree
        self.outputs    = outputs    #what outputs that function returns

class EffectTree:
    def __init__(self, root):
        self.root = root