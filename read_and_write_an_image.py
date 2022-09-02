def read_and_write_an_image(src, dest):
    with open(src, "rb") as rbf:
        with open(dest, "wb") as wbf:
            _bytes_ = rbf.readline()
            while len(_bytes_) > 0: 
                wbf.write(_bytes_)
                _bytes_ = rbf.readline()

read_and_write_an_image("D:/Media/Archives/f8b6acf4dc7699c60e02cebfd9b42355.jpg", "D:/pic.jpg")