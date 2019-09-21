#!/usr/bin/env python3

from timeit import default_timer as timer
import random
import pprint


def sequential_search(a_list, item):
    pos = 0
    found = False

    t_start = timer()
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    t_end = timer()
    t_elapsed = t_end - t_start

    result = (found, t_elapsed)

    return result


def ordered_sequential_search(ordered_list, item):
    pos = 0
    found = False

    t_start = timer()
    while pos < len(ordered_list) and not found:
        if ordered_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    t_end = timer()
    t_elapsed = t_end - t_start
    result = (found, t_elapsed)

    return result


def binary_search_iterative(ordered_list, item):
    first = 0
    last = len(ordered_list) - 1
    found = False

    t_start = timer()
    while first <= last and not found:

        midpoint = (first + last) // 2

        if ordered_list[midpoint] == item:
            found = True
        else:
            if item < ordered_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    t_end = timer()
    t_elapsed = t_end - t_start
    result = (found, t_elapsed)

    return result


def binary_search_recursive(ordered_list, item):
    t_start = timer()
    if len(ordered_list) == 0:
        t_end = timer()

        t_elapsed = t_end - t_start
        result = (False, t_elapsed)
        return result
    else:
        midpoint = len(ordered_list) // 2

    if ordered_list[midpoint] == item:
        t_end = timer()

        t_elapsed = t_end - t_start
        result = (True, t_elapsed)
        return result
    else:
        if item < ordered_list[midpoint]:
            return binary_search_recursive(ordered_list[:midpoint], item)
        else:
            return binary_search_recursive(ordered_list[midpoint + 1:], item)


def list_generator(size):
    main_list = []

    for i in range(100):
        inner_list = [random.randrange(0, size + 1, 1) for i in range(size)]
        main_list.append(inner_list)

    return main_list


def calc_average(times):
    total = sum(times)

    return total / len(times)


def order_list(a_dict):

    for value in a_dict.values():

        for lst in value:
            lst.sort()

    return a_dict


def main():

    rand_lists = {"list_500": list_generator(500),
                  "list_1000": list_generator(1000),
                  "list_10000": list_generator(10000)}

    ##############################
    # Run sequential search algo #
    ##############################
    num_to_find = -1
    ss_result = []
    final_results = []

    for value in rand_lists.values():

        # Value contain a list of lists size x
        for lst in value:
            # Run algo
            res = sequential_search(lst, num_to_find)

            # add duration to result_list
            ss_result.append(res[1])

    ave = calc_average(ss_result)

    print_msg = "Sequential Search took {} seconds to run on average.".format(ave)
    final_results.append(print_msg)

    # Order lists
    rand_lists = order_list(rand_lists)

    ######################################
    # Run ordered sequential search algo #
    ######################################
    ss_result.clear()

    for value in rand_lists.values():

        # Value contain a list of lists size x
        for lst in value:
            # Run algo
            res = ordered_sequential_search(lst, num_to_find)

            # add duration to result_list
            ss_result.append(res[1])

    ave = calc_average(ss_result)

    print_msg = "Ordered Sequential Search took {} seconds to run on average.".format(ave)
    final_results.append(print_msg)

    ####################################
    # Run binary_search_iterative algo #
    ####################################
    ss_result.clear()

    for value in rand_lists.values():

        # Value contain a list of lists size x
        for lst in value:
            # Run algo
            res = binary_search_iterative(lst, num_to_find)

            # add duration to result_list
            ss_result.append(res[1])

    ave = calc_average(ss_result)

    print_msg = "Binary Search Iterative took {} seconds to run on average.".format(ave)
    final_results.append(print_msg)

    ####################################
    # Run binary_search_recursive algo #
    ####################################
    ss_result.clear()

    for value in rand_lists.values():

        # Value contain a list of lists size x
        for lst in value:
            # Run algo
            res = binary_search_recursive(lst, num_to_find)

            # add duration to result_list
            ss_result.append(res[1])

    ave = calc_average(ss_result)

    print_msg = "Binary Search Recursive took {} seconds to run on average.".format(ave)
    final_results.append(print_msg)

    pprint.pprint(final_results)


if __name__ == '__main__':
    main()
