import re
import os
import codecs

DIR_FROM = "test_from_ide"
DIR_TO = "test_to_execute"

file_n = os.listdir(DIR_FROM)
for file in file_n:
    if file.endswith(".py"):
        file_o = codecs.open(os.path.join(DIR_FROM,file),"r","utf-8")
        text = file_o.readlines()
        file_o.close()
        file_to = codecs.open(os.path.join(DIR_TO,file),"w","utf-8")

        for text_e in text:
            try:
                find_xpath_start = re.search(r".*xpath\(",text_e).end()
                find_xpath_end = re.search(r".*xpath\(.*?\"\)",text_e).end() - 1
                if re.search(r"\.click\(\)",text_e):
                    print("        self.xpath =", text_e[find_xpath_start:find_xpath_end], \
                            "\n        self.action()\n", file=file_to)
                elif re.search(r"\.clear\(\)",text_e):
                    pass
                elif re.search(r"\.send_keys\(",text_e):
                    content_start = re.search(r"\.send_keys\(", text_e).end()
                    content_end = re.search(r"\.send_keys\(.*\"\)", text_e).end()-1
                    print("        self.xpath =", text_e[find_xpath_start:find_xpath_end], \
                            "\n        content =", text_e[content_start:content_end], \
                            "\n        self.action(do = \"send_keys\", content = content)\n", file=file_to)
                elif re.search(r"\.select_by_visible_text\(",text_e):
                    content_start = re.search(r"\.select_by_visible_text\(", text_e).end()
                    content_end = re.search(r"\.select_by_visible_text\(.*\"\)", text_e).end()-1
                    print("        self.xpath =", text_e[find_xpath_start:find_xpath_end], \
                            "\n        content =", text_e[content_start:content_end], \
                            "\n        self.action(do = \"select\", content = content)\n", file=file_to)
                elif re.search(r"self.assertEqual\(",text_e):
                    print("        self.xpath =", text_e[find_xpath_start:find_xpath_end], \
                            "\n        self.action()\n", file=file_to)
                else:
                    print(text_e.rstrip("\r\n"), file=file_to)
            except:
                if re.search(r"class \(test_class.Test_Class\)", text_e):
                    print("class Test_Case(test_class.Test_Class):", file=file_to)
                elif re.search(r"browser = self\.browser", text_e):
                    pass
                elif re.search(r"browser\.get\(self\.base_url \+ ", text_e):
                    pass
                else:
                    print(text_e.rstrip("\r\n"), file=file_to)
        file_to.close()

