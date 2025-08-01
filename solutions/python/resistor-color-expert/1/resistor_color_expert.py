def resistor_label(colors):
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

    tolerance_band = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green":  "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }

    units = [
        (10 ** 9, "gigaohms"),
        (10 ** 6, "megaohms"),
        (10 ** 3, "kiloohms"),
    ]

    length = len(colors)
    result = 0
    unit = 'ohms'
    tolerance = ''

    resistor_color_map = {color: i for i, color in enumerate(resistor_color)}

    if length == 5:
        result = (100 * resistor_color_map[colors[0]] + 10 * resistor_color_map[colors[1]] + resistor_color_map[colors[2]]) * (10 ** resistor_color_map[colors[3]])
        tolerance = tolerance_band[colors[4]]
    else:
        if length >= 1:
            result = resistor_color_map[colors[0]]
        if length >= 2:
            result = 10 * result + resistor_color_map[colors[1]]
        if length >= 3:
            result = result * (10 ** resistor_color_map[colors[2]])
        if length == 4:
            tolerance = tolerance_band[colors[3]]

    for format, name in units:
        if result >= format:
            result /= format
            unit = name
            break

    result = int(result) if result == int(result) else result
    
    return f"{result} {unit} {tolerance}".strip()