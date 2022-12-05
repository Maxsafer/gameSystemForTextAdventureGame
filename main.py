import json
import os

def breadcrumb(json_dict_or_list, value):
  if json_dict_or_list == value:
    return [json_dict_or_list]
  elif isinstance(json_dict_or_list, dict):
    for k, v in json_dict_or_list.items():
      p = breadcrumb(v, value)
      if p:
        return [k] + p
  elif isinstance(json_dict_or_list, list):
    lst = json_dict_or_list
    for i in range(len(lst)):
      p = breadcrumb(lst[i], value)
      if p:
        return [str(i)] + p

def action(listx, previousdict):    
  print(list(previousdict.keys())[int(optioninp)-1], "selected")
  print("_________________________________")
  print("1. Interact")
  print("2. Inspect")
  print("> ", end = ' ')
  actionina = input()
    
  if listx[0] == 0 and any((listx[5])[0:len(listx[5])-1] in x for x in inventory) and listx[1] == 0:
    listx[0] = 1
  if listx[0] == 0 and actionina == "1":
    print("============================================================")
    print(listx[2])
    print("============================================================")
  elif listx[0] == 1 and actionina == "1":
    print("============================================================")
    print(listx[3])
    print("============================================================")
    if listx[1] == 1:
      listx[0] = 0
      saveToInventory(listx, previousdict)
  elif actionina == "2":
    print("============================================================")
    print(listx[4])
    print("============================================================")

def options(dict, previousdict):
  if str(type(dict)) == "<class 'list'>":
    action(dict, previousdict)
    back.pop()
    return None
  else:
    tempoptions = []
    for x,room in enumerate(dict.keys()):
      tempoptions.append(dict[room])
    return tempoptions
  
def saveToInventory(list, previousdict):
  inventory.append(list)
  print(list[5], "added to the inventory.")
  removeItem(previousdict)

def removeItem(previousdict):
  looking4 = next(iter(previousdict.keys()))
  dirlist = breadcrumb(mainlevel, looking4)
  tempvar = mainlevel
  for x,item in enumerate(dirlist):
    if dirlist[x] != looking4:
      tempvar = tempvar[item]
    elif dirlist[x] == looking4:
      tempvar.pop(item)
      break

def showInventory(inventory):
  if len(inventory) == 0:
    print("============================================================")
    print("Your inventory is empty!")
    print("============================================================")
  else:
    print("_________________________________")
    for x, item in enumerate(inventory):
      print(f'{x+1}. {item[5]}')
    print()
    print("> ", end = ' ')
    actionini = input()
    if actionini.isnumeric() == False or actionini == '' or int(actionini) > len(inventory):
      print("Huh? What was I thinking...")
    else:
      print("============================================================")
      print((inventory[int(actionini)-1])[4])
      print("============================================================")
      
if __name__ == '__main__':
  # [STATE, CAN BE KEPT IN INVENTORY, TEXT FOR INTERACT IN STATE 0, TEXT FOR INTERACT IN STATE 1, TEXT FOR INSPECT, ITEM]
  # More rooms, more places or more things could be added as the game is being played by adding it to the dictionary.
  # This information could be stored on different files catalogued as levels, or progressions.
  # To save the progress, saving the main dictionary, e.g. "mainlevel" would do the job.
  
  f = open('house.json')
  mainlevel = json.load(f)
  f.close()
  
  inventory = []
  surroundings = mainlevel
  previousdict = surroundings
  back=[]
  back.append(previousdict)
  
  while True:
    temp = options(surroundings, previousdict)

    if temp != None:
      optionsdiclist = temp
    print("_________________________________")
    print("You are looking at")
    if str(type(surroundings)) == "<class 'dict'>":
      previousdict = surroundings
      for x,opt in enumerate(surroundings.keys()):
        print(f'{x+1}. {opt}')

    else:
      for x,opt in enumerate(previousdict.keys()):
        print(f'{x+1}. {opt}')

    print()
    print("0. back or i. Inventory")
    print("> ", end = ' ')
    optioninp = input()

    os.system('clear') #depends on the OS

    if optioninp == "i":
      showInventory(inventory)
      if str(type(surroundings)) != "<class 'dict'>":
        surroundings = back[-1]
        if len(back) > 1: 
          back.pop()
    elif optioninp.isnumeric() == False or optioninp == '' or int(optioninp) > len(optionsdiclist):
      print("Huh? What was I thinking...")
      if str(type(surroundings)) != "<class 'dict'>":
        surroundings = back[-1]
        if len(back) > 1: 
          back.pop()
    elif int(optioninp) == 0:
      surroundings = back[-1]
      if len(back) > 1: 
        back.pop()
    else:
      if previousdict not in back: 
        back.append(previousdict)
      surroundings = optionsdiclist[int(optioninp)-1]
    print("")