def find_common(length:int):
    for i in range(0, length):
        common = []
        for line in lines:
            common.append(line[i])
        counter = Counter(common)
        most_common_num, count = counter.most_common(1)[0]
        print(f'common {most_common_num}')