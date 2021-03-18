###example and testing
from EffectTree import *

def useless(): #placeholder function for testing
    print("useless called")

def passthrough(array):
    return [array]

def source():
    return "source"

basic_param = EffectParam("01110")

passthrough_effect = EffectNode(passthrough, 1, 1, [(basic_param, 0)], [])
#passthrough_effect.apply()

print_effect = EffectNode(print, 1, 0, [(passthrough_effect, 0)], [])

print_effect.apply()