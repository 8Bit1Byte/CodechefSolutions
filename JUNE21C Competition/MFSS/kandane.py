def find_max_sub_array(my_list, beg, end):
    max_end_at_i = max_seen_till_now = my_list[beg]
    max_left_at_i = max_left_till_now = beg
    max_right_till_now = beg + 1
    for i in range(beg + 1, end):
        if max_end_at_i > 0:
            max_end_at_i += my_list[i]
        else:
            max_end_at_i = my_list[i]
            max_left_at_i = i
        if max_end_at_i > max_seen_till_now:
            max_seen_till_now = max_end_at_i
            max_left_till_now = max_left_at_i
            max_right_till_now = i + 1
    return max_left_till_now, max_right_till_now, max_seen_till_now


my_list = input('Enter the list of numbers... ')
my_list = my_list.split()
my_list = [int(x) for x in my_list]
beg, end, max_val = find_max_sub_array(my_list, 0, len(my_list))
print('The maximum subarray begins at index {}, ends at index {}'
      ' and its sum is {}.'.format(beg, end - 1, max_val))
