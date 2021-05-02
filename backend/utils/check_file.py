# 拡張子の確認
def allwed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in 'mp3'


if __name__ == "__main__":
    pass
