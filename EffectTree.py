class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_amt: int, output_amt: int, inputs, extra_args=[]):
        self.function   = function   #function to be called to apply effect, should always return audio
        self.input_amt  = input_amt  #number of inputs function requires
        self.output_amt = output_amt #number of outputs function returns
        self.inputs     = inputs     #where inputs to pass to function come from, think of lower nodes lower in the graph. Should be [(EffectNode, int)]
        self.extra_args = extra_args #custom arguements to pass when applying
        #self.outputs   = outputs    #where function outputs go think of farther along in the tree
        self.values     = []         #actually values of output function

    def apply(self) -> list: #call function, should apply effect to audio, args are optional additional arguements
        args = self.extra_args
        for (effect, n) in self.inputs:
            args.append(effect.get(n))
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


###example and testing


def useless(): #placeholder function for testing
    print("useless called")

def passthrough(array):
    return [array]

def source():
    return "source"

passthrough_effect = EffectNode(passthrough, 1, 1, [], extra_args=["3213"])
passthrough_effect.apply()

print_effect = EffectNode(print, 1, 0, [(passthrough_effect, 1)])

print_effect.apply()

root = EffectNode(useless, 0, 0, [], [])
root.apply()