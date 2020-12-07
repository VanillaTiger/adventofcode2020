#cid
import re
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open("exercise_4.txt", 'r') as f:
    lines = f.readlines()
    number=0
    valid=True
    EOP=False
    passport = {'byr':0,'iyr':0,'eyr':0,'hgt':0,'hcl':0,'ecl':0,'pid':0}
    for part in lines:
        print (part)
        if part=="\n":
            for value in passport.values():
                if value !=1:
                    valid=False
                    break
            if valid == True:
                number+=1
                print("valid",number)
            valid=True
            EOP=True
            for key, values in passport.items():
                passport[key] = 0
            print("----------------")
            continue

        elements = part.split()
        for item in elements:
            print(item[:3])
            field=item[:3]
            value=item[4:]
            if field in fields:
                if field=='byr':
                    if (1920<=int(value) <=2002) and len(value)==4:
                        passport[field] = 1
                    else: print("wrong",field,"-",value)
                if field=='iyr':
                    if (2010<=int(value) <=2020) and len(value)==4:
                        passport[field] = 1
                    else:
                        print("wrong", field, "-", value)
                if field=='eyr':
                    if (2020<=int(value) <=2030) and len(value)==4:
                        passport[field] = 1
                    else:
                        print("wrong", field, "-", value)
                if field=='hgt':
                    if value[-2:]=="cm":
                        if 150<=int(value[:-2])<=193:
                            passport[field] = 1
                    elif value[-2:]=='in':
                        if 59<=int(value[:-2])<=76:
                            passport[field] = 1
                    else:
                        print("wrong", field, "-", value, "-", "None")
                if field=='hcl':
                    match=re.match(r'#[0-9a-f]{6}', value)
                    if match!=None and len(value)==7:
                        if len(match.group(0))==len(value):
                            passport[field] = 1
                        else:
                            print("wrong", field, "-", value,"-",match.group(0))
                    else:
                        print("wrong", field, "-", value, "-", "None")

                list_ecl=["amb",'blu','brn','gry','grn','hzl','oth']
                if field=='ecl':
                    if len(value)==3:
                        if value in list_ecl:
                            passport[field] =1
                        else:
                            print("wrong", field, "-", value)
                    else:
                        print("wrong", field, "-", value)

                if field=='pid':
                    match=re.match(r'\d{9}',value)
                    if match!=None and len(value)==9:
                        if len(match.group(0))==len(value):
                            passport[field] = 1
                        else:
                            print("wrong", field, "-", value,"-",match.group(0))
                    else:
                        print("wrong", field, "-", value, "-", "none")

            if field not in fields:
                if item[:3] != 'cid':
                    valid=False
                    passport.clear()
                    EOP=True
                    break
    print("final=",number)
