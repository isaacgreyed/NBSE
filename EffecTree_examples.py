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