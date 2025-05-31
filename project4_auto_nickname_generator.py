import random

def generate_nicknames(first_name,last_name,style):
    nicknames=[]
    nicknames.append(first_name[:3]+last_name[-3:])
    nicknames.append(last_name[:3]+first_name[-3:])
    nicknames.append(first_name +"_"+ last_name)
    nicknames.append(first_name[0]+last_name)
    nicknames.append(first_name+last_name[0])

    if len(first_name)>2 and len(last_name)>2:
        nicknames.append(last_name[:2]+first_name[2:])
        nicknames.append(first_name[:2]+last_name[2:])
        nicknames.append(first_name[::-1]+last_name[:2])
        nicknames.append(first_name.capitalize()+last_name[::-1].capitalize())
        nicknames.append(first_name.upper()+str(random.randint(10, 99)))

    if style=="short":
        nicknames=[n[:6] for n in nicknames]
    elif style=="fun":
        nicknames+=[n.title() for n in nicknames[:3]]
    elif style=="formal":
        nicknames=[n.title() for n in nicknames]
    return list(set(nicknames))

print("Welcome to the Nickname Generator!\n")

first_name=input("Enter your first name please: ").strip()
last_name=input("Enter your last name please: ").strip()

print("\nChoose your preferred nickname style:")
print("Options: short, fun, formal")
style=input("Enter your style: ").strip().lower()

nicknames=generate_nicknames(first_name, last_name, style)

print("\nGenerated Nicknames:")
for i,nickname in enumerate(nicknames, 1):
    print(f"{i}.{nickname}")

print("\nAll Nicknames in a List:")
print(nicknames)

save_option=input("\nDo you want to save these nicknames to file?(yes/no): ").strip().lower()
if save_option=="yes":
    filename=f"{first_name}_{last_name}_nicknames.txt"
    with open(filename, "w") as file:
        file.write("Generated Nicknames:\n")
        for i, nickname in enumerate(nicknames, 1):
            file.write(f"{i}.{nickname}\n")
    print(f"Nicknames saved to '{filename}'")

