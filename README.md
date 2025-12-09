# The-Run-Length-Encoder-Compression-
input_string = str(input("Enter a string to compress: "))
compressed = ""

count = 1
current = input_string[0]

for i in range(1, len(input_string)):
    if input_string[i] == current:
        count += 1
    else:
        compressed += str(count) + current
        current = input_string[i]
        count = 1

compressed += str(count) + current

print(compressed)
