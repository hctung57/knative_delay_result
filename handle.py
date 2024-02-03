import re

def extract_timing_info(input_text):
    pattern = r'time_namelookup:(\d+\.\d+).*time_total:(\d+\.\d+)'
    matches = re.findall(pattern, input_text)
    time_namelookup = matches[0][0]
    time_total = matches[0][1]
    return convert_to_ms(time_namelookup), convert_to_ms(convert_to_float(time_total) - convert_to_float(time_namelookup)), convert_to_ms(time_total)

def convert_to_float(input):
    return float(input)

def convert_to_ms(input):
    return float(input)*1000