class Audio:
    def __init__(self, data):
        self.data = data

class EffectNode:
    def __init__(self, function, input_amt: int, output_amt: int):
        self.function   = function   #function to be called to apply effect, should always return audio
        
        self.input_amt  = input_amt  #number of inputs function requires
        self.output_amt = output_amt #number of outputs function returns
        
        self.x_pos = None

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

    def recalculate_x(self):
        max_previous = -1
        for (effect, n) in self.inputs:
            if effect.x_pos == None:
                effect.recalculate_x()
        for (effect, n) in self.inputs:
            if effect.x_pos > max_previous:
                max_previous = effect.x
        self.x_pos = max_previous+1

    def get_as_list(self):
        ls = [self]
        for o in self.outputs:
            ls.extend(o.get_as_list())
        return ls

    #adds input to effect node
    #argument_num is what position the argument should be in starting at 0
    #effect is the EffectNode or EffectParam to get the effect from
    #from_output_num tells us what number output we are getting, defaults to none for when it does not apply like in an EffectParam
    def add_input(self, argument_num, effect, from_output_num):
        self.inputs[argument_num] = (effect, from_output_num)
        self.recalculate_x()

    def add_output(self, return_num, effect, to_input_num):
        self.outputs[return_num] = (effect, to_input_num)

def connect(a, b, return_num, input_num):
    a.add_output(return_num, b, input_num)
    b.add_input(input_num, a, return_num)

class EffectParam: #class to pass values into EffectNode class without other effect nodes
    def __init__(self, value):
        self.value = value
        self.output = []

    def get(self, value_num=None): #value_num is a placeholder value to allow calling from EffectNodes
        return self.value

    def add_output(self, return_num, effect, to_input_num):
        self.outputs[return_num] = (effect, to_input_num)

    def recalculate_x(self):
        return 0

class EffectTree:
    def __init__(self, root):
        self.root = root

    def get_height(self):
        ls = self.get_as_list()
        height_list = [0]*len(ls)
        for effect in ls:
            height_list[effect.x_pos] += 1
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
        self.get_height()
        array = [[]]*self.get_length()
        for l in ls:
            array[l.x_pos].append(l)


def render(effect_tree, canvas_x, canvas_y):
    array = effect_tree.get_as_2d
    i = 0
    for x in array:
        j = 0
        for y in x:
            draw(y, i, j, canvas_x, canvas_y)
            j += 1
        i += 1


def draw(effect, x, y, canvas_x, canvas_y):
    return