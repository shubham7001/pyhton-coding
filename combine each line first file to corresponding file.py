#Write a Python program to combine each line from first file with the  corresponding line in second file.

def combine_files(file1_path, file2_path, output_path):
    with open(r"C:\Users\maury\Desktop\file handling\file01.txt", 'r') as file1, open(r"C:\Users\maury\Desktop\file handling\file03.txt", 'r') as file2, open(output_path, 'w') as output_file:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        # Ensure that both files have the same number of lines
        if len(lines1) != len(lines2):
            raise ValueError("The input files must have the same number of lines.")

        for line1, line2 in zip(lines1, lines2):
            combined_line = f"{line1.strip()} {line2.strip()}\n"
            output_file.write(combined_line)


# Example usage
file1_path = r'C:\Users\maury\Desktop\file handling\file01.txt'
file2_path = r'C:\Users\maury\Desktop\file handling\file03.txt'
output_path = 'combined.txt'

combine_files(file1_path, file2_path, output_path)
