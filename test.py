def round_to_one_decimal(num):
    return round(num, 2)
def append_and_sort(numbers):
    only_numbers = list(set(numbers))  # 移除重複值
    sorted_numbers = sorted(only_numbers)  # 排序由小到大
    sorted_numbers = [round_to_one_decimal(num) for num in sorted_numbers]  # 將每個數字取到小數點第一位
    return sorted_numbers
def calculate_average(numbers):
    length = len(numbers)
    if length % 2 == 1:  # 奇數個值
        middle_index = length // 2
        print("奇數index", middle_index)
        return numbers[middle_index]
    else:  # 偶數個值
        upper_middle_index = length // 2
        lower_middle_index = upper_middle_index - 1
        index = (numbers[lower_middle_index] + numbers[upper_middle_index]) / 2
        print("偶數index", index)
        return index


input_numbers = input("輸入數字，以逗號分隔: ") #之後改成手肘的Y座標
my_numbers = [float(x) for x in input_numbers.split(",")] #之後不用留

sorted_numbers = append_and_sort(my_numbers)
average = calculate_average(sorted_numbers)

print("排序後的數字：", sorted_numbers)
print("平均值：", average)
print("轉換比例：", average//340)