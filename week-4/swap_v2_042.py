def swap_unique_keys_values(d):
    values = [d[k] for k in d]
    new = ({v: k for k,v in d.items() if values.count(v) == 1})
    return new
