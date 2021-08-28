num={
    "1" : "one",
    "2" : "Two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7": "seven",
    "8" : "eight",
    "9" : "nine"
}
output=""
number = input("Phone: ")
for i in number:
    output += num.get(i) + " "
print(output)