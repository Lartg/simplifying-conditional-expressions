def extract_position(line):
    if not line: return None
    if 'debug' in line or 'error' in line: return None
    if 'x:' not in line: return None
    start_index = line.find('x:') + 2
    pos = line[start_index:] # from start_index to the end.
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)