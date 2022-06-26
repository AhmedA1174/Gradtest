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
    medalTable = {
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
    for game in medalResults:
        winnerslist = game['podium']
        for index in range(len(winnerslist)):
            position = int(winnerslist[index][0])
            country = winnerslist [index][2:]
            if position==1:
                medalTable[country] = medalTable[country] +3
            elif position==2:
                medalTable[country] = medalTable[country] +2
            elif position==3:
                medalTable[country] = medalTable[country] +1


    return medalTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
