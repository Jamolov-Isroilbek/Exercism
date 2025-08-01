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

def label(colors):
    fst_clr = resistor_color.index(colors[0])
    snd_clr = resistor_color.index(colors[1])
    trd_clr = resistor_color.index(colors[2])
    color_trio = (10 * fst_clr + snd_clr) * (10 ** trd_clr)

    units = [
        (10 ** 9, "gigaohms"),
        (10 ** 6, "megaohms"),
        (10 ** 3, "kiloohms"),
    ]

    for factor, name in units:
        if color_trio >= factor:
            return f"{color_trio // factor} {name}"
    return f"{color_trio} ohms"