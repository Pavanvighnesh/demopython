phone=input("phonenumber: ")
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for digit in phone:
   output+=digit_mapping.get(digit, "!!")+" "
print(output)