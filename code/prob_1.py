s = input("Please enter the number of students in feet : ")
s = int(s)
feet = []
cms = []
for n in range(s):
        k = float(input("Enter the weight of student in foot>>"))
        feet.append(k)

cms = [feet[x] * 30.48 for x in range(s)]

print("\n The weight of number of students in cms : ", cms)

