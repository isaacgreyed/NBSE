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
passthrough_effect.add_input(0, basic_param) #because basic_param is an EffectParam the last argument is unneeded, as it only has one output

print_effect = EffectNode(print, 1, 0)
print_effect.add_input(0, passthrough_effect, 0) #since we are getting from another EffectNode we need to specify the output number as it could have multiple

print(print_effect.branch_length())

print_effect.apply()