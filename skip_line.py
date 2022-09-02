with open("file1.txt", "r") as rf:
    with open("file2.txt", "w") as wf:
        for i, line in enumerate(rf, 1):
            if i == 5: continue
            wf.write(line)

