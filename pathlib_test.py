from pathlib import Path
# p = Path()
# print([x for x in p.iterdir() if x.is_dir()])
import sys
def main():
    # with open('./test.txt') as f:
    #     print(f.read())
    # __file__ このファイルの絶対パス
    # p=Path(__file__)
    # print(p.resolve())
    # print(p.parent.resolve())
    # print(p.is_dir())
    # print(p.parent.resolve())#一つ上の階層を取得
    # print(p.parent.parent.resolve())#二つ上の階層を取得
    # test_txt_pass=p.parent/"test.txt"
    # print(test_txt_pass.resolve())
    # encording="ANSI"
    # print(test_txt_pass.read_text()) #withを使って開いてくれる。

    #以下、各フォルダにある”test2”ファイルを検索して表示してくれる
    test=Path("test_dir")
    print(test.exists())
    print(test.is_file())
    test_search = test.glob("**/test2")
    for test_search in test_search:
        print(test_search.read_text())
    print(sys.platform)


if __name__ == '__main__':
    main()
