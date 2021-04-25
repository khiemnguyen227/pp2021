import os
import zipfile

pw5 = zipfile.ZipFile('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\students.dat', "w")

for folder, subfolders, files in os.walk('D:\\Studies\\B2 subjects\\git\\pp2021\\pw5'):

    for file in files:
        if file.endswith('.py'):
            pw5.write(os.path.join(folder, file),
                      os.path.relpath(os.path.join(folder, file), 'D:\\Studies\\B2 subjects\\git\\pp2021\\pw5\\'),
                      compress_type=zipfile.ZIP_DEFLATED)

pw5.close()
