text = input("Enter a string: ")
count = 0
for character in text: 
     if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u': 
          count += 1
print("Number of vowels:", count) 
