import language_tool_python
import re
import os
import glob


'''This function is for creating a list of all files in the NLG dir'''
def file_loc(dir_path):
    files_path = os.path.join(dir_path, "*.bxb")
    filenames = glob.glob(files_path)
    return filenames


'''This function perform the actual spell check'''
def spell_check(file_list):
    tool = language_tool_python.LanguageTool('it-IT')
    for f in file_list:
        outfile = open(f, "r", encoding="utf-8")
        text = outfile.readlines()
        # file_path will show me from witch file the errors come
        file_path = os.path.abspath(f)
        outfile.close()
        for i in text:
            text_elab = re.findall('"([^"]*?)"', str(i))
            for l in text_elab:
                oki = re.sub(' \[*#(.*?)\}\]*', "", str(l))
                matches = tool.check(oki)
                if matches == []:
                    continue
                else:
                    print(matches)
                    print(l)
                    print(file_path)
                    print("\n")


files_path = file_loc(input("Directory path: "))
spell_check(files_path)


