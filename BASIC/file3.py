
dic = {}
key_list = ["name","price","amount"]
res = []

with open("./work.txt","r") as f:
    for line in f:
        line = line.strip().split()
        if line != []:
            for key in range(len(line)):
                dic[key_list[key]] = line[key]
            res.append(dic.copy())

print(res)


       
            




            