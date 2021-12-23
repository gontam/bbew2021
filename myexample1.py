def check_palindrome(string_line):
    return string_line == string_line[::-1]


FILE_NAME = 'palindrome_check.txt'

with open(FILE_NAME) as file:
    file_lines = file.read().splitlines()

new_file = []

for line in file_lines:
    checked = check_palindrome(line)
    new_file.append(line + ' ' + str(checked) + '\n')

file = open(FILE_NAME, 'w')
file.writelines(new_file)
file.close()
