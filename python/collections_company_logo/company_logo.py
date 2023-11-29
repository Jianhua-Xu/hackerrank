import collections
import itertools



if __name__ == '__main__':
    s = input()
    # use Counter to counts occurences
    d = collections.Counter(s)
    # sorted dictionary by value and then key
    # sort value by descending, and key by ascending order
    # the ascending/descending order can be achieved by -1 *
    # use itertools.islice to cut first 3 from a dict
    for k, v in itertools.islice(sorted(d.items(), key=lambda x: (-x[1], x[0])), 3):
        print(k, v)
   