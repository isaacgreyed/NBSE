###example and testing
from EffectTree import *

def useless(): #placeholder function for testing
    print("useless called")

def passthrough(array):
    return [array] #always return a list

def source():
    return "source"

basic_param = EffectParam("01110")

passthrough_effect = EffectNode(passthrough, 1, 1)

print_effect = EffectNode(print, 1, 0)
print_effect2 = EffectNode(print, 1, 0)

connect(basic_param, passthrough_effect, 1, 1)
connect(passthrough_effect, print_effect, 0, 0)
connect(passthrough_effect, print_effect2, 0, 0)

eff = EffectTree(passthrough_effect)
print_effect.apply()

