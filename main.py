import os


def get_list_of_file_content(filename):
    """Returns content of file with 'filename' as list of lines"""
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


def main():
    directory = 'files'
    files_content = {}
    for filename in os.listdir(directory):
        files_content[filename] = get_list_of_file_content(os.path.join(directory, filename))
    files_content_sorted = sorted(files_content.items(), key=lambda x: len(x[1]))
    with open('output.txt', 'w', encoding='utf-8') as file:
        for content in files_content_sorted:
            file.write(content[0] + '\n')
            file.write(str(len(content[1])) + '\n')
            file.writelines(content[1])
            file.write('\n')


if __name__ == '__main__':
    main()
