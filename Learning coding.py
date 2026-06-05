tree_dot="*"
empty_space=" "

while True:
    print("Lets build a tree")
    print("what shape should it be?")
    choice = str(input("what type of tree do you want? [right,left or normal?]: "))
    size = int(input("How big or small do you want your tree to be?: "))
    
    first_character=f"{empty_space}"

    if choice == "right":
        first_character=f"{tree_dot}"
        second_character=f"{empty_space}"
        
    elif choice == "left":
        first_character=f"{empty_space}"
        second_character=f"{tree_dot}"
    elif choice == "normal":
        first_character=f"{empty_space}"
        second_character=f"{tree_dot}"
        third_character=f"{empty_space}"

    
    for i in range(size):
        print(first_character * i) if choice == "right" else print(second_character * i)    

        
        
