from core.service import get_txtimg

# test
if __name__ == '__main__':
    path = "test.jpg"
    scale = 5
    # get_imgtxt(img, "PIL_"+path.replace(".jpg", ".txt"))
    get_txtimg(path, scale=scale).save("PIL_" + path)
