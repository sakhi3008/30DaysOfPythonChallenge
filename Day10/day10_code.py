# Challenge - Read numbers from a file and handle errors gracefully

file_path = r"C:\30DaysPythonChallenge\numbers.txt"

try:
    with open(file_path, 'r') as file:
        total = 0
        for line in file:
            try:
                number = float(line.strip()) 
                total += number
            except:
                print(f"Skipping invalid line: {line.strip()}")
        print(f"Total sum of valid numbers: {total}")   
except FileNotFoundError:
    print("Error: The file {file_path} was not found.")
finally:
    print("Execution completed — file processing handled properly.")
