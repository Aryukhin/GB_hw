'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>,
<requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
'''

f1 = open("123.txt", 'r', encoding='utf-8')
f2 = open("result.txt", 'w', encoding='utf-8')

for line in f1:
    line_correct = line.split(" ")
    f2.writelines(f"{line_correct[0], line_correct[5][1:], line_correct[6]}\n")
'''
    f2.write(line_correct[0], end = " ")
    f2.write(line_correct[5],end = " ")
    f2.write(line_correct[6], end = "\n")
    '''
'''
        index = line.find("-")
        id = line[:index]+ "\n"
        index_1 = line.find(']')
        index_2 = line.find()
        method = line[index_1 + 2:]
        f2.write(id)
        
'''
  #  for i in line:
   #     ind = line.find("-")
   #    f2.write(x)

f1.close()
f2.close()