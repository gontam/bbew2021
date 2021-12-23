def check_palindrome(string_line):
    if string_line==string_line[::-1]:
        return True
    else:
        return False

file =open('palindrome_check.txt', 'r')
file_lines = file.readlines()
file_lines_strip = []
for line in file_lines:
    file_lines_strip.append(line.strip())
new_file= []

for line in file_lines_strip:
    checked = check_palindrome(line)
    new_file.append(line + ' ' + str(checked) + '\n')

file = open('palindrome_check.txt', 'w')
file.writelines(new_file)
file.close()