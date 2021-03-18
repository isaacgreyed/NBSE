class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_amt: int, output_amt: int, inputs, outputs, extra_args=[]):
        self.function   = function   #function to be called to apply effect, should always return audio
        
        self.input_amt  = input_amt  #number of inputs function requires
        self.output_amt = output_amt #number of outputs function returns
        
        self.inputs     = inputs     #where inputs to pass to function come from, think of lower nodes lower in the graph. Should be [(EffectNode, int)] and tie directly to inputs
        self.outputs    = outputs    #where function outputs go think of farther along in the graph. Should be [(EffectNode, int)] and tie directly to inputs
        
        self.extra_args = extra_args #custom arguements to pass when applying
        self.values     = []         #actually values of output function

    def apply(self) -> list: #call function, should apply effect to audio, args are optional additional arguements
        args = []
        for (effect, n) in self.inputs:
            args.append(effect.get(n))
        args.append(self.extra_args)
        self.values = self.function(*args)

    def get(self, value_num): #value_num, what output to get, if it returned two seperate vales 
        self.apply()
        if len(self.values) < value_num:
            return None
        else:
            return self.values[value_num-1]

class EffectTree:
    def __init__(self, root):
        self.root = root