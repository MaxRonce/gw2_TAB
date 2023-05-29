import ast
import re

def convert_file_to_list(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Initialize the list
    result = []

    # Loop through the lines
    for line in lines:
        stripped_line = line.strip()

        try:
            # Try to convert to tuple or string
            converted_line = ast.literal_eval(stripped_line)
        except (ValueError, SyntaxError):
            try:
                # Try to convert to float
                converted_line = float(stripped_line)
            except ValueError:
                # If it fails, keep the line as string
                converted_line = convert_button(stripped_line)


        # Append the converted line to the result
        result.append(converted_line)

    return result

def convert_button(s):
    # Use regex to find the button name and the float number
    button_match = re.search('Button\.[\w\d]+', s)
    number_match = re.findall('(\d*\.\d+|\d+)', s)

    # If both matches are found, return the results as a tuple
    if button_match and number_match:
        # Select the last decimal number in the string
        return (button_match.group(0), float(number_match[-1]))
    else:
        return None


if __name__ == '__main__':
    file_path = 'input_records.txt'  # replace with the actual path to your file
    data = convert_file_to_list(file_path)
    print(data)
