def test_is_valid_ip_address():
    assert is_valid_ip_address('255.255.0.0') == True
    assert is_valid_ip_address('555.555.555.555') == False
    assert is_valid_ip_address('256.255.0.0') == False
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('192.168.1.1') == True