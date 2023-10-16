filenames = ["1.Data_Karyawan.txt", "2.Report.txt", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)


rank = filenames.index("2.Report.txt")+ 1
print(rank)