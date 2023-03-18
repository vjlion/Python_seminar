# Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}]
n = set()
for dict_i in dictionary:
    #print(i)
    for key in dict_i:
        #print(i[j])
        n.add(dict_i[key])
print(n)

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# unique_values = []
# for item in data:
#     for value in item.values():
#         value = value.strip() # удаляем лишние пробелы вокруг значений
# if value not in unique_values:
#     unique_values.append(value)
# print(set(unique_values))