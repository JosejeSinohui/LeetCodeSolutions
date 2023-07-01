import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.replace(" ", "")
        test = test.strip()
        test = [int(x) for x in test]

        sum = 0

        for index, number in enumerate(test):
            if index % 2 == 0:
                sum += number * 2
            else:
                sum += number

        if sum % 10 == 0:
            print("Real")

        else:
            print("Fake")
