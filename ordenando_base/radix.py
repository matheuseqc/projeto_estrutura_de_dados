import csv

# Função para aplicar o algoritmo Counting Sort
def counting_sort(lst, place):
    RADIX = 10
    freq = [0] * RADIX
    output = [None] * len(lst)

    for i in range(len(lst)):
        index = lst[i][0] // place
        freq[index % RADIX] += 1

    for i in range(1, RADIX):
        freq[i] += freq[i - 1]

    for i in range(len(lst) - 1, -1, -1):
        index = lst[i][0] // place
        output[freq[index % RADIX] - 1] = lst[i]
        freq[index % RADIX] -= 1

    for i in range(len(lst)):
        lst[i] = output[i]

# Função para aplicar o algoritmo Radix Sort
def radix_sort(lst):
    max_element = max(lst, key=lambda x: x[0])[0]
    place = 1
    while max_element // place > 0:
        counting_sort(lst, place)
        place *= 10

# Lendo o arquivo data.csv
with open("ordenando_base/shuffled_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    data = [row for row in csv_reader]

# Ordenando pela coluna "Id" utilizando Radix Sort com Counting Sort
data = [(int(row[0]), row) for row in data]
radix_sort(data)
sorted_data = [row[1] for row in data]


# Escrevendo o resultado em um novo arquivo CSV
with open("ordenando_base/radixSort_data.csv", "w", newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerows(sorted_data)