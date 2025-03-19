#print("Apple"     " Price: 5000 Krw")
#print("Banana"    " Price: 4000 Krw")
#print("Grape"     " Price: 5300 Krw")
#print("Melon"     " Price: 6500 Krw")

#второй вариант задачи
#fruits_dic = {
#    "Apple": " Price: 5000 Krw",
#    "Banana": " Price: 4000 Krw",
#    "Grape" : " Price: 5300 Krw",
#    "Melon" : " Price: 6500 Krw"
#}
#print(fruits_dic["Apple, Banana, Grape, Melon"])

#3 задача
#fruits_dic = {
#    "apple":  " Price: 6000 Krw",
#    "banana": " Price: 5000 Krw",
#    "orange": " Price: 4000 Krw",
#    "melon" : " Price: 3500 Krw"
#}
#choice = input("выберите что хотите проверить: ").lower()
#if choice in fruits_dic:
#    print(f"{choice} is in fruits_dic")
#else:
#    print(f"{choice} is not in fruits_dic")

#3 задача. проверяем прогноз
#t1 = "a","b","c"
#t2 = ('a', 'b ', 'c')
#t3 = ('d','e')
#print(t1 == t2)
#print(t1 > t2)
#print(t1 < t2)
#print(t1 + t2)
#print([t1 + t2])
#print(t1)

#4задач
#sales = (100,121,120, 130, 140, 120, 122, 123, 190, 125)
#redused_sales_days = sum((sales[i] < sales[i - 1]) for i in range(1, len(sales)))
#print(f"In the past 10 days, {redused_sales_days} days had reduced sales comprared to the previous day.")

#5 задача
t = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
freq_dic = {num: t.count(num) for num in set(t)}
max_freq = max(freq_dic.values())
most_freq_num = [num for num, freq in freq_dic.items()
if freq == max_freq]
most_freq = max(most_freq_num)
print(f"The most frequent element: {most_freq}")