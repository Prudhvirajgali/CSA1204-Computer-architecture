hex_number = input("Enter a hexadecimal number: ")
dec_number = int(hex_number, 16)
bin_number = bin(dec_number)
print("The binary equivalent of", hex_number, "is", bin_number)
