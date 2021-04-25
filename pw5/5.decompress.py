import zipfile

pw5 = zipfile.ZipFile('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\students.dat')
pw5.extractall('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\Compress and Decompress\\')

pw5.close()