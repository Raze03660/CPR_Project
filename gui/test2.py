# 引入random模組
import random
import time


# 定義一個函數，用來將數字取到小數點第一位
def round_to_one_decimal(num):
    return round(num, 1)


# 定義一個函數，用來將數字陣列去重並排序
def append_and_sort(numbers):
    only_numbers = list(set(numbers))  # 移除重複值
    sorted_numbers = sorted(only_numbers)  # 排序由小到大
    sorted_numbers = [round_to_one_decimal(num) for num in sorted_numbers]  # 將每個數字取到小數點第一位
    return sorted_numbers


# 定義一個函數，用來計算數字陣列的平均值
def calculate_average(numbers):
    length = len(numbers)
    if length % 2 == 1:  # 奇數個值 取中間
        middle_index = length // 2
        print("我有奇數個")
        return numbers[middle_index]
    else:  # 偶數個值 中間那2個值的算術平均值就是這群數據的中位數。
        upper_middle_index = length // 2
        lower_middle_index = upper_middle_index - 1
        print("我有偶數個")
        return (numbers[lower_middle_index] + numbers[upper_middle_index]) / 2


# 定義一個空的浮點數陣列
float_array = []

# 定義一個空的時間戳陣列
press_times = []
start_time = time.time()

cpr_press_count = 0
# 使用for迴圈，生成10個隨機的浮點數，範圍在360-405之間，並取到小數點第四位
for i in range(29):
    num = random.uniform(360, 405)
    num = round(num, 4)
    float_array.append(num)
    time.sleep(0.5)
    current_time = time.time() - start_time
    press_times.append(current_time)  # 紀錄每次按壓回彈後進入下一個循環的時間點

# 使用append_and_sort函數，將浮點數陣列去重並排序
sorted_numbers = append_and_sort(float_array)

# 使用calculate_average函數，計算浮點數陣列的平均值並將平均值取到小數點第一位
average = round(calculate_average(sorted_numbers), 1)

# 結果
print("隨機生成的浮點數陣列：", float_array)
print("排序後的數字：", sorted_numbers)
print("平均值：", average)

# 計算CPR按壓的過程次數及每分鐘幾下的頻率
y_coordinates = float_array  # 陣列可能要給容錯誤差值
press_intervals = []
sum_press_intervals = 0

for i in range(1, len(y_coordinates) - 1):
    diff1 = y_coordinates[i] - y_coordinates[i - 1]
    diff2 = y_coordinates[i + 1] - y_coordinates[i]
    if diff1 > 0 and diff2 < 0:
        cpr_press_count += 1  # 之後可以紀錄1下的時間 再去推算頻率
        press_intervals = press_times[i]
        sum_press_intervals += press_times[i] - press_times[i - 1]
        print("CPR按壓的時間戳：", round(press_intervals, 3))

# 結束計時
end_time = time.time()

# 計算經過的時間
elapsed_time = end_time - start_time

# 計算平均頻率（每分鐘幾下）
average_frequency = int(cpr_press_count / elapsed_time * 60)  # (len(y_coordinates) - 2) 之後改成記錄到1次循環的時間
sum_average_frequency = round(sum_press_intervals / cpr_press_count, 3)
average_sum_average_frequency = int(60 / sum_average_frequency)
print("CPR按壓過程次數：", cpr_press_count)
print("總時間", elapsed_time)
print("平均按壓間隔:", round(sum_average_frequency, 3))
print("平均頻率（每分鐘幾下）：", average_frequency)
print("以平均按壓間隔推算頻率:", average_sum_average_frequency)