from math import gcd

def LCM(inputQuestionValue):
    lcm = inputQuestionValue[0]
    for value in inputQuestionValue[1:]:
        lcm = (lcm*value) // gcd(lcm, value)
    return(lcm)


try :
    n = int(input())
    dictionary = {"Darrell" : 0, "Sally" : 0}

    for case in range(n//2):
        question = input().split()
        questioner = question[0]

        inputQuestionValue = list(map(int, question[1].split(',')))

        # print(questioner, inputQuestionValue)

        assert(2 <= len(inputQuestionValue) <= 7)
        for num in inputQuestionValue:
            assert(1 <= num <= 100)

        correctAnswer = LCM(inputQuestionValue)

        answer = input().split()
        answerer = answer[1]

        if(case == 0):
            first = questioner
            second = answerer

        print(questioner + "'s question is : ", end='')
        print(*inputQuestionValue, sep=',')

        if(answer[2] != 'PASS'):
            inputAnswerValue = int(answer[2])
            if(inputAnswerValue == correctAnswer):
                print("Correct Answer")
                print(answerer + ": 10points")
                dictionary[answerer] += 10
            else:
                print("Incorrect Answer")
                print(answerer + ": 0points")

        else:
            print("Question is PASSed")
            print("Answer is:", correctAnswer)
            print(answerer + ": 0points")
        # print(answerer, inputAnswerValue)

    print("Total Points:")
    print(first + ": " + str(dictionary[first]) + "points")
    print(second + str(dictionary[second]) + "points")

    if(dictionary["Darrell"] == dictionary["Sally"]):
        print("Game Result: Draw")
    elif(dictionary["Darrell"] > dictionary["Sally"]):
        print("Game Result: Darrell is winner")
    else:
        print("Game Result: Sally is winner")

except:
    print("Invalid Input")
