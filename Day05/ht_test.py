from harmeet import collect_names

def test_collect_names_success():
    names = ["Harmeet", "aman", "rohit", "neha", "simran"]
    
    result = collect_names(names)
    
    assert result == ["Harmeet", "Aman", "Rohit", "Neha", "Simran"]
