import os



filepath = "C:/Users/dell/Desktop/chinapower crawler/trafiltura/网页们"
filelist = os.listdir(filepath)
# s = ''
# print('start decoding')
# for file in filelist:
#     with open(filepath + '/' + file, 'rb') as f1:
#         print(file)
#         text = f1.readline()
#         print(text.decode('utf-8'))
#         s += text.decode('utf-8')

# Name of the output combined file
output_file = "combined_output.txt"

# Open the output file in write mode
with open("C:/Users/dell/Desktop/chinapower crawler/整合1.txt", 'w', encoding="utf-8") as combined_file:
    for input_file in filelist:
        print(input_file)
        # Open each input file in read mode
        with open(filepath + '/' + input_file, "r", encoding="utf-8") as current_file:
            # Read the content of the current input file
            file_content = current_file.read()
            # Write the content to the output file
            combined_file.write(file_content)

print("Files combined successfully.")
        
        
# print(type(s))
# print(s)

# print('start writing')
# with open("C:/Users/dell/Desktop/chinapower crawler/整合1.txt", 'wb') as f:
#     f.write(s.encode('utf-8'))