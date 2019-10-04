def total_score(rolls):
    values = convert_2_num(rolls)
    score = 0
    roll_index = 0
    for frame in range(10):
        # if is strike
        if rolls[roll_index] == 'x':
            score += 10 + values[roll_index+1] + values[roll_index+2]
            roll_index += 1
        # if is spare
        elif rolls[roll_index] == '/':
            score += 10 + values[roll_index+2]
            roll_index += 2
        else:
            score += values[roll_index] + values[roll_index+1]
            roll_index += 2
    return score

def convert_2_num(rolls):
    values = []
    for i in rolls:
        if i in ('x','/'):
            values.append(10)
        elif i == '-':
            values.append(0)
        else:
            values.append(int(i))
    return values