def sort(list):
    if len(list) > 1:
        middle = len(list)//2
        left_list = list[:middle]
        right_list = list[middle:]
        print(left_list)
        print(right_list)
        sort(left_list)
        sort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] > right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1
        
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

list = [4,2,85,54,26,5,8]
sort(list)
print(list)