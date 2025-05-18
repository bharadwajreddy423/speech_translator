from run_pipeline import parse_input_pairs

def test_parse_input_pairs_valid():
    inputs = ["audio/audio01.mp3:en", "audio/audio03.mp3:fr"]
    # Mocking os.path.isfile for test purposes
    import os
    os.path.isfile = lambda path: True
    result = parse_input_pairs(inputs)
    assert result["audio/audio01.mp3"] == "en"
    assert result["audio/audio03.mp3"] == "fr"

def test_parse_input_pairs_invalid():
    inputs = ["invalid", "just_file"]
    import os
    os.path.isfile = lambda path: True
    result = parse_input_pairs(inputs)
    assert result == {}
