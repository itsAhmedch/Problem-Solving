def make_readable(seconds):
    if seconds < 360000:
        hh = seconds // 3600
        mm = (seconds % 3600) // 60
        ss = seconds % 60
        return f"{hh:02}:{mm:02}:{ss:02}"

