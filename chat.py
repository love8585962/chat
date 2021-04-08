#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #如出現\ufeff 就需要再utf-8後面加上sig
        for line in f:
            lines.append(line.strip())
    return lines #回傳清單

#將lines清單傳入convert這個function
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen': #如果沒找到Allen就跳過
            person = 'Allon'
            continue
        elif line == 'Tom': #如果沒找到Tom就跳過
            person = 'Tom'
            continue
        if person:  #如果person有值才做下面那行
            new.append(person + ': ' + line)
    return new  #將轉換好的回傳到new


#寫入檔案
def write_file(filename, lines):  #寫入檔名跟內容 所以需要兩個變數
    with open(filename, 'w') as f:
        for line in lines:        #將內容一行一行寫進去lines
            f.write(line + '\n')

#主程式
def main():
    lines = read_file('input.txt') #呼應def read_file
    lines = convert(lines)  #覆蓋lines
    write_file('output.txt', lines) #正式寫入


main()