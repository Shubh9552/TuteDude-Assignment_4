with open('output.txt','w') as file1:
    string1 = str(input("Enter text to write to the file: "))
    writing_file = file1.write(f"{string1}\n")
    print("Data successfully written to output.txt.")

with open('output.txt','a') as file2:
    string2 = str(input("Enter additional text to append:"))
    append_file = file2.write(f"{string2}\n")
    print("Data successfully appended.")

with open('output.txt','r') as read1:
    line1 = read1.readline().strip()
    line2 = read1.readline().strip()
    print("Final content of output.txt:")
    print(line1)
    print(line2)