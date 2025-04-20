matters = {}  # Store all matters

def addMatter(name):
    if name not in matters:
        matters[name] = 'gas'

def deleteMatter(name):
    if name in matters:
        del matters[name]

def changeMatterState(name, new_state):
    if name in matters and matters[name] != 'solid':
        if new_state in ['liquid', 'solid'] and matters[name] == 'gas':
            matters[name] = new_state
        elif new_state in ['gas', 'solid'] and matters[name] == 'liquid':
            matters[name] = new_state
        if matters[name] == 'solid':
            writeToFile(name)

def writeToFile(matter_name):
    try:
        with open('solid_matters.txt', 'r') as f:
            solid_matters = f.read().splitlines()
    except FileNotFoundError:
        solid_matters = []
    
    if matter_name not in solid_matters:
        solid_matters.append(matter_name)
    with open('solid_matters.txt', 'w') as f:
        f.write('\n'.join(solid_matters))
      
def countByState(state):
    return sum(1 for matter_state in matters.values() if matter_state == state)

def totalMatters():
    return len(matters)

def loadSolidMatters():
    try:
        with open('solid_matters.txt', 'r') as f:
            solid_matters = f.read().splitlines()
            for name in solid_matters:
                matters[name] = 'solid'
    except FileNotFoundError:
        pass

# Load previously saved solid matters on system start
loadSolidMatters()

# Example usage:
# addMatter('Water')
addMatter('Iron')
addMatter('Petrol')
addMatter('Oxygen')
addMatter('Mercury')
# changeMatterState('Water', 'liquid')
# changeMatterState('Water', 'solid')
changeMatterState('Iron', 'solid')
changeMatterState('Petrol', 'liquid')
changeMatterState('Oxygen', 'liquid')
changeMatterState('Oxygen', 'gas')
changeMatterState('Mercury', 'solid')
changeMatterState('Mercury', 'liquid') # can't convert solid to liquid

print("Solid matters:", countByState('solid'))
print("Liquid matters:", countByState('liquid'))
print("Gaseous matters:", countByState('gas'))
print("Total matters:", totalMatters())


while True:
    print("\nMenu:")
    print("1. Add Matter")
    print("2. Delete Matter")
    print("3. Change Matter State")
    print("4. Count Matters by State")
    print("5. Total Matters")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter matter name to add: ")
        addMatter(name)
    elif choice == '2':
        name = input("Enter matter name to delete: ")
        deleteMatter(name)
    elif choice == '3':
        name = input("Enter matter name to change state: ")
        new_state = input("Enter new state (gas, liquid, solid): ")
        changeMatterState(name, new_state)
    elif choice == '4':
        state = input("Enter state to count (gas, liquid, solid): ")
        print(f"Number of matters in {state} state: {countByState(state)}")
    elif choice == '5':
        print("Total matters:", totalMatters())
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
