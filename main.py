import os

def main():
    i = 0
    #add folder location of where files to rename are located
    path = "C:/Users/user123/Desktop/Test/"
    for filename in os.listdir(path):
        #enter the new filename and filetype
        new_name = "test-file" + str(i) + ".txt"
        file_source =path + filename
        new_name =path + new_name
        os.rename(file_source, new_name)
        i += 1

if __name__ == '__main__':
    main()
