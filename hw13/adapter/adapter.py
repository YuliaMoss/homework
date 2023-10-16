"""1 - Implement adapter patter from_txt_to_html

for example, we have a such structure in txt:

name,last_name,age,salary
John,Malkovich,28,1000

I want to see:

<name>John</name>
<last_name>Malkovich</last_name>
.............

It should work with any file with such a structure"""


class TxtAdapter:
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.tags_list = []

    def txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()

        header = lines[0].replace('\n', '').split(',')
        user_data = [user.replace('\n', '').split(',') for user in lines[1:]]
        # html_result = []

        for i in user_data:
            add_tag_to_list = self.combine_data(header, i)

            self.tags_list.extend(add_tag_to_list)
        return ''.join(self.tags_list)

    def combine_data(self, header, list_of_data):
        make_tag_list = []

        combine_list = list(zip(header, list_of_data))
        for name, data in combine_list:
            make_tag_result = self.make_tag(name, data)

            make_tag_list.extend(make_tag_result)
        return make_tag_list

    def make_tag(self, name, data):
        tag_result = f'<{name}>{data}</{name}>\n'
        return tag_result


if __name__ == '__main__':
    html_ = TxtAdapter('structure.txt').txt_to_html()
    print(html_)
