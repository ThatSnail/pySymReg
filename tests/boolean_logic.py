from test_utils import testNetwork

def testNOT():
    """ NOT Gate. 1 input, 1 output """
    testNetwork(1, [], 1, [
                            ([0], [1], [lambda x: x > 0.5], "NOT Gate, with input 0"),
                            ([1], [0], [lambda x: x < 0.5], "NOT Gate, with input 1"),
                         ])

def testNOR():
    """ NOR Gate. 2 inputs, 1 output """
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.5], "NOR Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "NOR Gate, with inputs 1 1")
                         ])
   

def testOR():
    """ OR Gate. 2 inputs, 1 output """
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "OR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "OR Gate, with inputs 1 1")
                         ])

def testAND():
    """ AND Gate. 2 inputs, 1 output """
    testNetwork(2, [], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 0"),
                            ([0, 1], [0], [lambda x: x < 0.5], "AND Gate, with inputs 0 1"),
                            ([1, 0], [0], [lambda x: x < 0.5], "AND Gate, with inputs 1 0"),
                            ([1, 1], [1], [lambda x: x > 0.5], "AND Gate, with inputs 1 1")
                         ])

def testNAND():
    """ NAND Gate. 2 inputs, 1 output """
    testNetwork(2, [], 1, [
                            ([0, 0], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "NAND Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "NAND Gate, with inputs 1 1")
                         ])

def testXOR():
    """ XOR Gate. 2 inputs, 2 hidden, 1 output """
    testNetwork(2, [2], 1, [
                            ([0, 0], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 0 0"),
                            ([0, 1], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 0 1"),
                            ([1, 0], [1], [lambda x: x > 0.5], "XOR Gate, with inputs 1 0"),
                            ([1, 1], [0], [lambda x: x < 0.5], "XOR Gate, with inputs 1 1")
                         ])

def testBooleanLogic():
    testOR()
    testAND()
    testXOR()
    testNOR()
    testNOT()
    testNAND()
