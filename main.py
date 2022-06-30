file = open("facebook-israel.txt", "r", encoding="utf8")
phone_list = open("phonelist.txt", "w", encoding="utf8")
gender_list = open("genderlist.txt", "w", encoding="utf8")
id_list = open("idlist.txt", "w", encoding="utf8")
name_list = open("namelist.txt", "w", encoding="utf8")
all = open("all.txt", "w", encoding="utf8")
gender = ""
name = ""
id = ""
x = file.read()
x = x.split("\n")
for i in range(len(x) - 1):
    x[i] = x[i].replace(":", "")
    if "male" in x[i]:
        gender_list.write("male\n")
        gender = "male"
    else:
        gender_list.write("female\n")
        gender = "female"

    phone_list.write(x[i][x[i].index("972"):x[i].index("972") + 12].replace("972", "0") + "\n")
    id = x[i].replace(":", "").replace(x[i][x[i].index("972"):x[i].index("972") + 12], "").replace("gender", "")
    for ele in id:
        if not ele.isdigit():
            id = id.replace(ele, "")
    id_list.write(id + "\n")
    name=x[i].replace(":", "").replace(x[i][x[i].index("972"):x[i].index("972") + 12], "").replace(gender, "").replace(id, "")
    name_list.write(name.split(",",1)[0]+"\n")
    all.write(x[i][x[i].index("972"):x[i].index("972") + 12].replace("972", "0") + "," + gender + "," + id+","+name.split(",",1)[0]+ "\n")
    print(x[i][x[i].index("972"):x[i].index("972") + 12].replace("972", "0") + "," + gender + "," + id+","+name.split(",",1)[0])

# me =female need check if this הפוך
#add name maybe remove description
