#შექმენით თქვენი რაზმელებისგან სია, ამოირჩიეთ რენდომულად 3 ბავშვი და მიუწერეთ გვერდში "კარგად სწავლობს".
# ვისი სახელიც "ი"-ზე მთავრდება, დაუპრინტეთ გვერდით "cool"

import random 
crew_members = ['babajanishvili','Rajavi','janezashvili','Anastia','Qatamadze','Takidze','Turmanishvili','Amonashvili','Vako']

print(crew_members[4])
print(crew_members[random.randint(0,6)]) 
print(crew_members[random.randint(0,6)])
for i in range(1,4):
    print('winner N',i,'is',random.choice(crew_members))

crew_members = ['babajanishvili','Rajavi','janezashvili','Anastia','Qatamadze','Takidze','Turmanishvili','Amonashvili','Vako']
crew_members.remove(random.choice(crew_members))
print(crew_members +"good student" ) 

