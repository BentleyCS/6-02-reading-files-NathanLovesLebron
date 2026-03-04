import CSP_6_02_reading_files as HW

def test_to_string():
    assert HW.toString("example.txt") == "stuff\n" "things\n" "Bananas!!"


def test_longest_line():
    assert HW.longestLine("example.txt") == "Bananas!!"


def test_to_binary():
    assert HW.toBinary("Binary.txt") == ['10010011', '1100']
