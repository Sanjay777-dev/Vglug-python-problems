#Count Days Spent Together

def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def convert(date):
        month, day = map(int, date.split("-"))
        return sum(days[:month-1]) + day
    a1 = convert(arriveAlice)
    a2 = convert(leaveAlice)
    b1 = convert(arriveBob)
    b2 = convert(leaveBob)
    start = max(a1, b1)
    end = min(a2, b2)
    return max(0, end - start + 1)
arriveAlice = input("Alice arrival date: ")
leaveAlice = input("Alice leaving date: ")
arriveBob = input("Bob arrival date: ")
leaveBob = input("Bob leaving date: ")
print("Days together:", countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
