from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main() -> None:
    # print('===================running get_files_info tests====================')
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))
    # print(get_files_info("calculator", "../"))
    #
    # print('===================running get_file_conten tests===================')
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    #
    # print('===================running write_file tests===================')
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print('==========running main.py...=======')
    print(run_python_file("calculator", "main.py", "3", "+", "2"))
    print('==========running tests.py...=======')
    print(run_python_file("calculator", "tests.py"))
    print('==========running ../main.py...=======')
    print(run_python_file("calculator", "../main.py"))
    print('==========running nonexistent.py...=======')
    print(run_python_file("calculator", "nonexistent.py"))
if __name__=="__main__":
    main()
