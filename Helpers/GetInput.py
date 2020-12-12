def get_input(day):
    with open(f'Day{day}\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        return lines
