types_of_people = 10
x = f"There are {types_of_people} type of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

hilarious = "true"
joke_evaluation = "Isn't that joke so funny?! {} {test}"

# Thay giá trị của hilarious (true) vào {} trong chuỗi joke_evaluation2
joke_evaluation2 = joke_evaluation.format(hilarious, test="ca")

joke_evaluation = "Isn't that joke so funny?! {test0} {test}"
joke_evaluation3 = joke_evaluation.format(test0=hilarious, test="ca")

joke_evaluation = "Isn't that joke so funny?! {} {}"
joke_evaluation4 = joke_evaluation.format(hilarious, "ca")

print(joke_evaluation2)
print(joke_evaluation3)
print(joke_evaluation4)
