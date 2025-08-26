from sys import argv
input_filename = "GMT20250726-234400_Recording.transcript.txt"
output_filename = "session 8.txt"

def read_filtered_file(file_path):
    with open(file_path, 'r') as file:
        cleaned_lines = []
        for line in file.readlines():
            # Strip whitespace from the line to check if it's blank
            stripped_line = line.strip()
            if len(stripped_line) >0 and not stripped_line[0].isdigit():
                cleaned_lines.append(stripped_line)
    return cleaned_lines

# Example usage:
# read_filtered_file('your_file.txt')


with open(output_filename,'w+') as file:
    for line in read_filtered_file(input_filename):
        file.write(line+'\n')
