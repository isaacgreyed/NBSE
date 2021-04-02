class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_amt: int, output_amt: int):
        self.function   = function   #function to be called to apply effect, should always return audio
        
        self.input_amt  = input_amt  #number of inputs function requires
        self.output_amt = output_amt #number of outputs function returns
        
        self.x_pos = None

        self.inputs     = []  #where inputs to pass to function come from, think of lower nodes lower in the graph. Should be [(EffectNode, int)] and tie directly to outputs
        self.outputs    = [] #where function outputs go think of farther along in the graph. Should be [(EffectNode, int)] and tie directly to inputs

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

    def recalculate_x(self):
        max_previous = -1
        for (effect, n) in self.inputs:
            if effect.x_pos == None:
                effect.recalculate_x()
        for (effect, n) in self.inputs:
            if effect.x_pos > max_previous:
                max_previous = effect.x_pos
        self.x_pos = max_previous+1

    def get_as_list(self):
        ls = [self]
        for (out, n) in self.outputs:
            ls.extend(out.get_as_list())
        return ls

    #adds input to effect node
    #argument_num is what position the argument should be in starting at 0
    #effect is the EffectNode or EffectParam to get the effect from
    #from_output_num tells us what number output we are getting, defaults to none for when it does not apply like in an EffectParam
    def add_input(self, argument_num, effect, from_output_num):
        self.inputs.insert(argument_num, (effect, from_output_num))
        self.recalculate_x()

    def add_output(self, return_num, effect, to_input_num):
        self.outputs.insert(return_num, (effect, to_input_num))

def connect(a, b, return_num, input_num):
    a.add_output(return_num, b, input_num)
    b.add_input(input_num, a, return_num)

class EffectParam: #class to pass values into EffectNode class without other effect nodes
    def __init__(self, value):
        self.value = value
        self.outputs = []
        self.x_pos = 0

    def get(self, value_num=None): #value_num is a placeholder value to allow calling from EffectNodes
        return self.value

    def add_output(self, return_num, effect, to_input_num):
        self.outputs.insert(return_num, (effect, to_input_num))

    def recalculate_x(self):
        return 0

class EffectTree:
    def __init__(self, root):
        self.root = root

    def get_height(self):
        ls = self.get_as_list()
        height_list = []
        for effect in ls:
            if len(height_list) >= effect.x_pos:
                height_list[effect.x_pos-1] += 1
            else:
                height_list.insert(effect.x_pos, 1)
        return max(height_list)

    def get_length(self):
        ls = self.get_as_list()
        length_list = []
        for effect in ls:
            length_list.append(effect.x_pos)
        return max(length_list)

    def get_as_list(self):        
        return list(set(self.root.get_as_list()))

    def get_as_2d(self):
        ls = self.root.get_as_list()
        array = []
        for i in range(0, self.get_length()):
            array.append([])
        for l in ls:
            array[l.x_pos-1].append(l)
        return array