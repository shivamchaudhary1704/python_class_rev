def addTwoNumbers(l1, l2):
    l1_rev = l1[::-1]
    l2_rev = l2[::-1]

    main_list = []

    for i in range(len(l1_rev)):
        main_list.append(l1_rev[i] + l2_rev[i])

    return main_list


l1 = [1, 2, 3, 4]
l2 = [3, 4, 7, 8]
print(addTwoNumbers(l1, l2))
