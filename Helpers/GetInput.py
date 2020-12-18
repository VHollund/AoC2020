def get_input_split_lines(day):
    with open(f'Day{day}\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        return lines


def get_file_split_lines(file):
    with open(file, 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        return lines



def get_input_tuple(day):
    with open(f'Day{day}\input.txt', 'r') as input:
        lines = "".join(input.readlines()).split("\n")
        lines=(lines[0],[x for x in lines[1].split(",") if x != "x"])
    return lines