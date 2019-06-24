import json
with open("C:\\Users\\meb\\Desktop\\binlist.json","r",encoding="utf-8") as dosya:
    data = json.load(dosya)
    dosya2 = open("C:\\Users\\meb\\Desktop\\deneme.xlsx","a",encoding="utf-8")
    dosya2.write("CardType"+"\t"+"isBussinessCard"+"\t"+"MemberName"+"\t"+"MemberNo"+"\t"+"PrefixNo"+"\n")
    for i in data["list"]:
        dosya2.write(i["cardType"] + "\t"+i["isBusinessCard"] + "\t"+i["memberName"] + "\t"+str(i["memberNo"]) + "\t"+str(i["prefixNo"]) + "\n")
        print(i["cardType"] + "\t"+i["isBusinessCard"] + "\t"+i["memberName"] + "\t"+str(i["memberNo"]) + "\t"+str(i["prefixNo"]) + "\n")

    dosya.close()