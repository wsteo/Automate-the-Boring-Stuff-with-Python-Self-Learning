stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v, end=" ")
        print(k)
        item_total += int(v)

    print("Total number of items: " + str(item_total))


displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in inventory:
            inventory.setdefault(addedItems[i], 0)

        inventory[addedItems[i]] += 1

    return inventory


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
