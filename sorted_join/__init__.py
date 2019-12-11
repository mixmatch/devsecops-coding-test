def sorted_join(arg_lists):
    join_list = []
    for arg_list in arg_lists:
        join_list = join_list + arg_list
    sort_list = sorted(join_list)
    return sort_list
