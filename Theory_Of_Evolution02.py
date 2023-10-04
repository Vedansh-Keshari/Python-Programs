with open("document.txt","w") as file:
# "a" is appending mode (does not erases the pre written content of the file)
# "r" is reading mode (reads only)
# "w" is writing mode (writes only)
# "r+" is special read and write mode (used to handle both reading and writing actions)
    print(file.read())
    file.write("\nI am fine.")
file.close()

