#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #如出現\ufeff 就需要再utf-8後面加上sig
        for line in f:
            lines.append(line.strip())
    return lines #回傳清單

#將lines清單傳入convert這個function
def convert(lines):
    Allen_word_count = 0
    Allen_sticker_count = 0
    Allen_image_count = 0

    Viki_word_count = 0
    Viki_sticker_count = 0
    Viki_image_count = 0

    for line in lines:
        s = line.split(' ') #先對空格進行切割並存成s
        time = s[0]  #將時間存成變數time
        name = s[1]  #將名稱存成變數name
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_image_count += 1
            else:
                for msg in s[2:]:
                    Allen_word_count += len(msg)
#-------------------------------------------------
        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                Viki_image_count += 1
            else :
                for msg in s[2:]:
                    Viki_word_count += len(msg)

    print('Allen說了',Allen_word_count, '個字')
    print('Allen傳了', Allen_sticker_count, '個貼圖')
    print('Allen傳了', Allen_image_count, '個圖片')

    print('Viki說了',Viki_word_count, '個字')
    print('Viki傳了', Viki_sticker_count, '個貼圖')
    print('Viki傳了', Viki_image_count, '個圖片')


#寫入檔案
def write_file(filename, lines):  #寫入檔名跟內容 所以需要兩個變數
    with open(filename, 'w') as f:
        for line in lines:        #將內容一行一行寫進去lines
            f.write(line + '\n')


#主程式
def main():
    lines = read_file('LINE-Viki.txt') #呼應def read_file
    lines = convert(lines)  #覆蓋lines
    #write_file('output.txt', lines) #正式寫入


main()