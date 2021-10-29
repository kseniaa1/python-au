def write_d(file_name, output):
    f = open(file_name, "w")
    f.write(output)
    f.close()


def write_data(file_name, output):
    f = open(file_name, "a")
    for i in range(len(output)):
        f.write(output[i])
    f.close()


def read_data(file_name):
    data = ''
    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    return data


def low(s):
    new_s = s.replace(' ', '-')
    return new_s.lower()[:len(new_s) - 1]


def get_ind(data):
    k = 0
    for i in range(len(data)):
        if (data[i][0] != '\n') :
            if (data[i][0] == data[i][1]):
               if data[i][0] == '#':
                 k = i
               elif k != 0:
                  return k-1
    return 0


def get_md_format_sol(data):
    new_data = [''] * (len(data)+1)
    new_data[0] = '##'+data[0]
    new_data[1] = "\n"
    new_data[2]= data[1]
    new_data[3] = "\n"
    new_data[4] = '```python \n'
    for i in range(5, len(data)-1):
        new_data[i] = data[i-1][4:]
    new_data[len(data)] = '```'
    return new_data


def get_new_md_format_link(data):
    low_title = low(data[0])
    link = '+ [' + data[0][:len(data[0])-1] + '](#' + low_title + ')'
    return link


def get_old_md_solutions(data):
    old_solutions = ['']*(len(data)-get_ind(data)-1)
    for i in range(get_ind(data)+1, len(data)):
        old_solutions[i-get_ind(data)-1] = data[i]
    return old_solutions


def get_new_md_content(old_content, new_content):
    k =0
    lngth = len(old_content) + len(new_sol_md) + 100
    final_data = ['']*lngth
    for i in range(1, get_ind(old_content)):
        final_data[i] = old_content[i+1]
    final_data[get_ind(old_content)] = get_new_md_format_link(new_content)+'\n'
    for i in range(get_ind(old_content)+1, len(get_old_md_solutions(old_content))+1+get_ind(old_content)):
        final_data[i] = get_old_md_solutions(old_content)[i-get_ind(old_content)-1]
    for i in range(len(get_old_md_solutions(old_content))+1+get_ind(old_content), len(get_md_format_sol(new_content))+len(get_old_md_solutions(old_content))+1+get_ind(old_content)):
        final_data[i] = get_md_format_sol(new_content)[i - len(get_old_md_solutions(old_content))-1-get_ind(old_content)]

    return final_data





existing_data = read_data("new.md")
new_data = read_data("aaa.txt")
new_sol_md = get_md_format_sol(new_data)
new_link_md = get_new_md_format_link(new_data)
new_md_data = get_new_md_content(existing_data, new_data)
print(get_ind(existing_data))
write_d("new.md", '#Arrays\n\n')
write_data("new.md", new_md_data)
write_data('new.md', '\n')
