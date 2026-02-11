def collect_names(names):
    if len(names) != 5:
        raise ValueError("Exactly 5 names required")
    
    return [name.strip() for name in names]
