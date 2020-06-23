Data = [1, 4, 6, 8, 3, 22, 87, 23]
# mengakses list
# print(Data)
Subdata1 = Data[3]
Subdata2 = Data[-3]
Subdata5 = Data[-0]

# memotong list
Subdata3 = Data[0:4]
Subdata4 = Data[2:]
Subdata6 = Data[:4]

Data2 = [100, 200, 300, 500, 400, 600]

# menambah list
Data3 = Data + Data2

# merubah content dari list
Data[4] = 87

# mengcopy list ke variabel baru
a = Data[:]
a[4] = 87

# merubah content list dengan menggunakan metode slicing
Data[3:5] = [11, 12]

# List dalam List
x = [Data, Data2]
# mengakses List dalam multidimensional list
y = x[0][5]

# method untuk List
Data.append(Data2)
Data.append(222)

# Function yang bisa digunakan pada List
panjang_list = len(Data)
print(panjang_list)
