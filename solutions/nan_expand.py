def nan_expand(times):
    nan = ""
    if times > 0:
        nan = "NaN"
        expand = "Not a "
        for i in range(times):
            nan = expand + nan

    return nan
