rule30table = {"000": 0, "001": 1, "010": 1, "011": 1, "100": 1, "101": 0, "110": 0, "111": 0}
def evolve(input):
    left_empty = [0, 0]
    right_empty = [0, 0]
    output = []   
    new_input = []
    new_input.extend(left_empty)
    new_input.extend(input)
    new_input.extend(right_empty)
    for i in range(len(new_input) - 2):
        cell = str(new_input[i]) + str(new_input[i+1]) + str(new_input[i+2])
        output.append(rule30table[cell])
    return output

def rule30(list_, n):
    result = list_
    for i in range(n):
        result = evolve(list_)
        list_ = result
    return result

print(rule30([0], 1))
print(rule30([1], 1))
print(rule30([1], 2))
