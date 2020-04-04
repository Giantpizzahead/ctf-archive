import tarfile

for i in range(1000, 0, -1):
    path = str(i) + ".tar"
    ar = tarfile.open(path)
    ar.extractall()
    ar.close()
    print("On " + path)
