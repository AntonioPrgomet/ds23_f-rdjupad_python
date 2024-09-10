from datacleaner import DataCleaner

dc = DataCleaner()

def test_dc():
    assert isinstance(dc.clean_data(True), list)