resistor_color = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def value(colors):
    return 10 * resistor_color.index(colors[0]) + resistor_color.index(colors[1])