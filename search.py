import re

def grep(pattern, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            if re.search(pattern, line):
                print(line.strip())
    return 

def sed(old_pattern, new_patten, file_name):
    # ... 
    return 

def awk(n, file_name):
    # ...
    return 

def main():
    file_name = input("Enter the file name")
    command  = input("Enter the command: grep, sed, awk")

    if command == 'grep':
        pattern = input("Enter the pattern")
        grep(pattern, file_name);
    elif command == 'sed':
        old_pattern = input("Enter old pattern")
        new_pattern = input("Enter new pattern")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number")
        num = int(n)
        awk(n, file_name)
    else:
        print("Comamnd is invalid")

if __name__ == "__main__":
    main()
