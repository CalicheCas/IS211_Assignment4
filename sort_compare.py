#!/usr/bin/env python3

from timeit import default_timer as timer
import random
import pprint


def insertion_sort(a_list):

    t_start = timer()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    t_end = timer()

    return t_end - t_start


def shell_sort(a_list):

    t_start = timer()
    n = len(a_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a_list[i]
            j = i
            while j >= gap and a_list[j - gap] > temp:
                a_list[j] = a_list[j - gap]
                j -= gap
            a_list[j] = temp
        gap //= 2
    t_end = timer()

    return t_end - t_start


def python_sort(a_list):

    t_start = timer()
    a_list.sort()
    t_end = timer()

    return t_end - t_start


def generate_list(size):

    rand_list = [random.randrange(0, size + 1, 1) for i in range(size)]
    return rand_list


def calc_average(a_list):

    return sum(a_list) / len(a_list)


def main():
    rand_lists = {"list_500": generate_list(3),
                  "list_1000": generate_list(5),
                  "list_10000": generate_list(10)}

    time_res = []
    final_res = []

    ###########################
    # Run insertion sort algo #
    ###########################
    for value in rand_lists.values():

        t = insertion_sort(value)

        time_res.append(t)
    ave = calc_average(time_res)

    print_msg = "Insertion sort took {} seconds to run on average.".format(ave)
    final_res.append(print_msg)

    ###########################
    # Run shell sort algo #
    ###########################
    rand_lists = {"list_500": generate_list(3),
                  "list_1000": generate_list(5),
                  "list_10000": generate_list(10)}
    time_res.clear()
    for value in rand_lists.values():
        t = shell_sort(value)

        time_res.append(t)
    ave = calc_average(time_res)

    print_msg = "Shell sort took {} seconds to run on average.".format(ave)
    final_res.append(print_msg)

    ###########################
    # Run python sort algo #
    ###########################
    rand_lists = {"list_500": generate_list(3),
                  "list_1000": generate_list(5),
                  "list_10000": generate_list(10)}
    time_res.clear()
    for value in rand_lists.values():
        t = python_sort(value)

        time_res.append(t)
    ave = calc_average(time_res)

    print_msg = "Python sort took {} seconds to run on average.".format(ave)
    final_res.append(print_msg)

    pprint.pprint(final_res)


if __name__ == '__main__':
    main()


