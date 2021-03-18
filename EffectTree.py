class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_amt: int, output_amt: int):
        self.function   = function   #function to be called to apply effect, should always return audio
        
        self.input_amt  = input_amt  #number of inputs function requires
        self.output_amt = output_amt #number of outputs function returns
        
        self.inputs     = [None]*input_amt  #where inputs to pass to function come from, think of lower nodes lower in the graph. Should be [(EffectNode, int)] and tie directly to outputs
        self.outputs    = [None]*output_amt #where function outputs go think of farther along in the graph. Should be [(EffectNode, int)] and tie directly to inputs

    def apply(self) -> list: #call function, should apply effect to audio
        args = []
        for (effect, n) in self.inputs:
            args.append(effect.get(n))
        return self.function(*args)

    def get(self, value_num): #value_num, what output to get. Start counting at 0
        vals = self.apply()
        if len(vals) < value_num+1:
            return None
        else:
            return vals[value_num]

    #adds input to effect node
    #argument_num is what position the argument should be in starting at 0
    #effect is the EffectNode or EffectParam to get the effect from
    #from_output_num tells us what number output we are getting, defaults to none for when it does not apply like in an EffectParam
    def add_input(self, argument_num, effect, from_output_num=None):
        self.inputs[argument_num] = (effect, from_output_num)

class EffectParam: #class to pass values into EffectNode class without other effect nodes
    def __init__(self, value):
        self.value = value

    def get(self, value_num=None): #value_num is a placeholder value to allow calling from EffectNodes
        return self.value

class EffectTree:
    def __init__(self, root):
        self.root = root