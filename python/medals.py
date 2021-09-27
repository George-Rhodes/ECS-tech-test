medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point

    res_table = {   # on a further itoration i would make it so that if this table creation is done automatically
    # such as that if there is a team that isnt already in the table a new value would be created
        "Italy": 0,
        "France": 0,
        "ROC": 0,
        "USA": 0,
        "Qatar": 0,
        "China": 0,
        "Germany": 0,
        "Brazil": 0,
        "Belarus": 0,
    }


    for x in results:
        podium = x.get('podium')
        first1 = podium[0]
        second1 = podium[1]
        third1 = podium[2]
        first = first1[2:]
        second = second1[2:]
        third = third1[2:]
        val1 = res_table.get(first) + 3
        val2 = res_table.get(second) + 2
        val3 = res_table.get(third) + 1
        res_table[first] = val1
        res_table[second] = val2
        res_table[third] = val3


    return res_table


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3, # this is wrong this wouldnt pass the test as the actual outcome is 2
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

# test harness
if __name__ == "__main__":
    R_T = createMedalTable(medalResults)
    print(R_T)
    #for x in medalResults:
    #    podium = x.get('podium')
    #    first = podium[0]
    #    print(first[2:])