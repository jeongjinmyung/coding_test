import re


def solution(files):
    answer = []
    my_files = []
    for idx, i in enumerate(files):
        num = re.findall("\d+",i)[0]
        header = i[:i.index(num)]
        num = int(num)
        header = header.lower()
        my_files.append([header,num,idx])
    my_files.sort(key=lambda x : (x[0],x[1]))
    answer = [files[j[2]] for j in my_files ]
    return answer