def test_sort_array():
    # Test case 1
    arr = [5, 2, 8, 1, 9]
    expected_output = [1, 2, 5, 8, 9]
    assert sort_array(arr) == expected_output

    # Test case 2
    arr = [100, 180, 260, 310, 40, 535, 695]
    expected_output = [40, 100, 180, 260, 310, 535, 695]
    assert sort_array(arr) == expected_output

    # Test case 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_array(arr) == expected_output

    # Test case 4
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_array(arr) == expected_output

    # Test case 5
    arr = []
    expected_output = []
    assert sort_array(arr) == expected_output

    # Test case 6
    arr = [1]
    expected_output = [1]
    assert sort_array(arr) == expected_output

    # Test case 7
    arr = [1, 1, 1, 1, 1]
    expected_output = [1, 1, 1, 1, 1]
    assert sort_array(arr) == expected_output

    # Test case 8
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    expected_output = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    assert sort_array(arr) == expected_output

    # Test case 9
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_array(arr) == expected_output

    # Test case 10
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
    expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sort_array(arr) == expected_output