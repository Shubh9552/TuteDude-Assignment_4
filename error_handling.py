try:
    with open('sample.txt','r') as file1:
        reading_file1 = file1.readline()
        reading_file2 = file1.readline()
        print("Reading file content:")
        print(f"Line1:{reading_file1.strip()}")
        print(f"Line2:{reading_file2.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")


