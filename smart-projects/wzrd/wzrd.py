def get_color_for_temp(temp_current):
    # i can't think in degrees celsius to save my life
    temp_cold = 5
    temp_comfort = 27
    temp_hot = 46
    temp_range = temp_hot - temp_cold

    if temp_current >= temp_hot:
        return (50, 0, 0)
    elif temp_current <= temp_cold:
        return (0, 0, 50)
    else:
        return get_color_in_range(temp_cold, temp_hot, temp_current)

def get_color_in_range (minimum, maximum, value):
    max_color_val = 30

    minimum, maximum = float(minimum), float(maximum)
    ratio = 2 * (value - minimum) / (maximum - minimum)
    b = int(max(0, max_color_val * (1 - ratio)))
    r = int(max(0, max_color_val * (ratio - 1)))
    g = max_color_val - b - r
    return (r, g, b)
