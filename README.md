# TuteDude-Assignment_4



# Task 1: Read a File and Handle Errors 
I have put code in try block which might raise exception.
try:
    with open('sample.txt','r') as file1:             #this line will open sample.txt in read mode.
        reading_file1 = file1.readline()              #this line will read first line of sample.txt
        reading_file2 = file1.readline()              #this line will read second line of sample.txt
        print("Reading file content:")                #normal print statement
        print(f"Line1:{reading_file1.strip()}")       #this will print first line of sample.txt. strip() fn will remove extra space/lines.
        print(f"Line2:{reading_file2.strip()}")       #this will print second line of sample.txt. strip() fn will remove extra space/lines.
except FileNotFoundError:                             #this will raise exception if sample.txt file is not found.
    print("Error: The file 'sample.txt' was not found")


  # Task 2 Write and Append Data to a File

  with open('output.txt','w') as file1:                          # this will open a output.txt file in write mode.
    string1 = str(input("Enter text to write to the file: "))    # this will ask for user input which we are going to write in output.txt file.
    writing_file = file1.write(f"{string1}\n")                   # this will write user input to the file and give new line 
    print("Data successfully written to output.txt.")            # print statement

with open('output.txt','a') as file2:                            # this will open a output.txt file in append mode.
    string2 = str(input("Enter additional text to append:"))     # this will ask for user input which we are going to append in output.txt file.
    append_file = file2.write(f"{string2}\n")                    # this will write user input to the file at the end of text fiel as we opened it in append mode                                                                       and give new line.
    print("Data successfully appended.")                         # print statement

with open('output.txt','r') as read1:                            # this will open a output.txt file in read mode.
    line1 = read1.readline().strip()                             # this will read first line of output.txt and strip() will remove extra spaces/lines.
    line2 = read1.readline().strip()                             # this will read second line of output.txt and strip() will remove extra spaces/lines.
    print("Final content of output.txt:")                        # print statement
    print(line1)                                                 # It will print first line.
    print(line2)                                                 # It will print second line.
