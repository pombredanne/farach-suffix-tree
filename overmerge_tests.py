import farach
import utils

def run_tests():
    sorts_correct()
    case_3_rec()
    case_2_rec()
    mix_case_3_1()
    faked_tree_article()
    faked_tree_book()
    # small_example_2()  # only prints stuff, no asserts
    print('tests succeeded!')


def sorts_correct():

    even = utils.Node(aId="root")
    even.add_child(utils.Node([1], 1))
    even.add_child(utils.Node([4], 2))

    odd = utils.Node(aId="root")
    odd.add_child(utils.Node([2], 3))
    odd.add_child(utils.Node([3], 4))

    result = utils.Node(aId="root")
    result.add_child(utils.Node([1], 1))
    result.add_child(utils.Node([2], 3))
    result.add_child(utils.Node([3], 4))
    result.add_child(utils.Node([4], 2))

    assert farach.overmerge(even, odd).fancyprint() == result.fancyprint()


def case_3_rec():

    even = utils.Node(aId="root")
    inner = utils.Node([1,1,1], "inner")
    even.add_child(inner)

    inner.add_child(utils.Node([1], 1))
    inner.add_child(utils.Node([4], 2))

    odd = utils.Node(aId="root")
    inner = utils.Node([1,2], "inner")
    odd.add_child(inner)
    inner.add_child(utils.Node([2], 3))
    inner.add_child(utils.Node([3], 4))

    result = utils.Node(aId="root")

    inner = utils.Node([1,2], "inner")
    result.add_child(inner)
    inner2 = utils.Node([1], "inner")
    inner2.add_child(utils.Node([1], 1))
    inner2.add_child(utils.Node([4], 2))

    inner.add_child(inner2)

    inner.add_child(utils.Node([2], 3))
    inner.add_child(utils.Node([3], 4))

    overmerged = farach.overmerge(even, odd)

    assert overmerged.fancyprint() == result.fancyprint()


def case_2_rec():

    even = utils.Node(aId="root")

    inner = utils.Node([1,1], "inner")
    even.add_child(inner)
    inner.add_child(utils.Node([1,1,1], 1))

    odd = utils.Node(aId="root")

    inner = utils.Node([1,2], "inner")
    odd.add_child(inner)

    inner.add_child(utils.Node([1,2], 2))

    result = utils.Node(aId="root")

    inner = utils.Node([1,1], "inner")

    result.add_child(inner)

    inner2 = utils.Node([1,2], 2)
    inner.add_child(inner2)

    inner2.add_child(utils.Node([1], 1))

    overmerged = farach.overmerge(even, odd)

    assert overmerged.fancyprint() == result.fancyprint()


def mix_case_3_1():

    even = utils.Node(aId="root")

    even.add_child(utils.Node([1], 1))
    even.add_child(utils.Node([2, 2, 2], 2))

    odd = utils.Node(aId="root")

    odd.add_child(utils.Node([2,1], 3))
    odd.add_child(utils.Node([3], 4))

    result = utils.Node(aId="root")

    result.add_child(utils.Node([1], 1))
    inner = utils.Node([2,1], 3)

    result.add_child(inner)
    inner.add_child(utils.Node([2], 2))

    result.add_child(utils.Node([3], 4))

    overmerged = farach.overmerge(even, odd)

    assert overmerged.fancyprint() == result.fancyprint()


def faked_tree_book():
    t_odd = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_odd.add_child(inner1)
    inner2 = utils.Node(11, 3)
    inner1.add_child(inner2)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(13, 1)
    inner2.add_child(inner3)
    inner3 = utils.Node(9, 5)
    inner2.add_child(inner3)
    inner1 = utils.Node(1, "inner")
    t_odd.add_child(inner1)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(7, 7)
    inner2.add_child(inner3)
    inner3 = utils.Node(3, 11)
    inner2.add_child(inner3)
    inner2 = utils.Node(5, 9)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, 13)
    t_odd.add_child(inner1)


    t_even = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_even.add_child(inner1)
    inner2 = utils.Node(10, 4)
    inner1.add_child(inner2)
    inner2 = utils.Node(6, 8)
    inner1.add_child(inner2)
    inner2 = utils.Node(2, 12)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, "inner")
    t_even.add_child(inner1)
    inner2 = utils.Node(12, 2)
    inner1.add_child(inner2)
    inner2 = utils.Node(3, "inner2")
    inner1.add_child(inner2)
    inner3 = utils.Node(8, 6)
    inner2.add_child(inner3)
    inner3 = utils.Node(4, 10)
    inner2.add_child(inner3)

    t_overmerged_result = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_overmerged_result.add_child(inner1)
    inner2 = utils.Node(10, 4)
    inner1.add_child(inner2)
    inner3 = utils.Node(11, 3)
    inner2.add_child(inner3)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(13, 1)
    inner2.add_child(inner3)
    inner3 = utils.Node(6, 8)
    inner2.add_child(inner3)
    inner4 = utils.Node(9, 5)
    inner3.add_child(inner4)
    inner2 = utils.Node(2, 12)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, "inner")
    t_overmerged_result.add_child(inner1)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(12, 2)
    inner2.add_child(inner3)
    inner3 = utils.Node(7, 7)
    inner2.add_child(inner3)
    inner3 = utils.Node(3, 11)
    inner2.add_child(inner3)
    inner2 = utils.Node(3, "inner2")
    inner1.add_child(inner2)
    inner3 = utils.Node(5, 9)
    inner2.add_child(inner3)
    inner3 = utils.Node(8, 6)
    inner2.add_child(inner3)
    inner3 = utils.Node(4, 10)
    inner2.add_child(inner3)
    inner1 = utils.Node(1, 13)
    t_overmerged_result.add_child(inner1)


    
    inputstr = farach.str2int("1211122122213");
    t_even.update_leaf_list()
    t_odd.update_leaf_list()


    t_overmerged = farach.overmerge(t_even, t_odd, inputstr)

    t_overmerged_result.update_leaf_list()

    
    assert t_overmerged.fancyprint(inputstr) == t_overmerged_result.fancyprint(inputstr)



def faked_tree_article():
    t_odd = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_odd.add_child(inner1)
    inner2 = utils.Node(13, 1)
    inner1.add_child(inner2)
    inner2 = utils.Node(3, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(7, 7)
    inner2.add_child(inner3)
    inner3 = utils.Node(11, 3)
    inner2.add_child(inner3)
    inner1 = utils.Node(1, "inner")
    t_odd.add_child(inner1)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(5, 9)
    inner2.add_child(inner3)
    inner3 = utils.Node(3, 11)
    inner2.add_child(inner3)
    inner2 = utils.Node(9, 5)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, 13)
    t_odd.add_child(inner1)
    t_even = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_even.add_child(inner1)
    inner2 = utils.Node(12, 2)
    inner1.add_child(inner2)
    inner2 = utils.Node(4, 10)
    inner1.add_child(inner2)
    inner2 = utils.Node(2, 12)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, "inner")
    t_even.add_child(inner1)
    inner2 = utils.Node(8, 6)
    inner1.add_child(inner2)
    inner2 = utils.Node(2, "inner2")
    inner1.add_child(inner2)
    inner3 = utils.Node(6, 8)
    inner2.add_child(inner3)
    inner3 = utils.Node(10, 4)
    inner2.add_child(inner3)
    t_overmerged_result = utils.Node(0,"root")
    inner1 = utils.Node(1, "inner")
    t_overmerged_result.add_child(inner1)
    inner2 = utils.Node(12, 2)
    inner1.add_child(inner2)
    inner3 = utils.Node(13, 1)
    inner2.add_child(inner3)
    inner2 = utils.Node(3, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(7, 7)
    inner2.add_child(inner3)
    inner3 = utils.Node(11, 3)
    inner2.add_child(inner3)
    inner3 = utils.Node(4, 10)
    inner2.add_child(inner3)
    inner2 = utils.Node(2, 12)
    inner1.add_child(inner2)
    inner1 = utils.Node(1, "inner")
    t_overmerged_result.add_child(inner1)
    inner2 = utils.Node(2, "inner")
    inner1.add_child(inner2)
    inner3 = utils.Node(5, 9)
    inner2.add_child(inner3)
    inner4 = utils.Node(8, 6)
    inner3.add_child(inner4)
    inner3 = utils.Node(3, 11)
    inner2.add_child(inner3)
    inner2 = utils.Node(2, "inner2")
    inner1.add_child(inner2)
    inner3 = utils.Node(6, 8)
    inner2.add_child(inner3)
    inner4 = utils.Node(9, 5)
    inner3.add_child(inner4)
    inner3 = utils.Node(10, 4)
    inner2.add_child(inner3)
    inner1 = utils.Node(1, 13)
    t_overmerged_result.add_child(inner1)
    

    inputstr = farach.str2int("1112221221213");
    t_even.update_leaf_list()
    t_odd.update_leaf_list()


    t_overmerged = farach.overmerge(t_even, t_odd, inputstr)

    t_overmerged_result.update_leaf_list()

    assert t_overmerged.fancyprint(inputstr) == t_overmerged_result.fancyprint(inputstr)


def small_example():
    t_even = utils.Node("root")
    t_even.add_child(utils.Node([1,1], 2))

    t_odd = utils.Node("root")
    t_odd.add_child(utils.Node([1,2,2], 1))


    print("even")
    print(t_even.fancyprint())

    print("odd")
    print(t_odd.fancyprint())

    t_overmerged = farach.overmerge(t_even, t_odd)

    print("overmerged")
    print(t_overmerged.fancyprint())

def small_example_2():

    t_even = utils.Node("root")
    inner2 = utils.Node([2,1], "inner")
    t_even.add_child(inner2)
    inner2.add_child(utils.Node([2,1,3], 6))
    inner2.add_child(utils.Node([3], 10))

    print("even")
    print(t_even.fancyprint())

    t_odd = utils.Node("root")
   
    t_odd.add_child(utils.Node([2,2,1,3], 9))

    print("odd")
    print(t_odd.fancyprint())

    t_overmerged = farach.overmerge(t_even, t_odd)
    print("t_overmerged")
    print(t_overmerged.fancyprint())
    farach.adjust_overmerge(t_overmerged, t_even, t_odd)


if __name__ == '__main__':
    run_tests()
    
