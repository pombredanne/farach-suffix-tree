import farach
from utils import Node


def run_tests():
    inputstr = farach.str2int('1')

    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    expected_result.add_child(Node(aId=1, aStrLength=2))
    expected_result.add_child(Node(aId=2, aStrLength=1))
    constructed_tree.update_leaf_list()
    expected_result.update_leaf_list()
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint())
    # print('actual:')
    # print(constructed_tree.fancyprint())
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)

    inputstr = farach.str2int('12')
    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    expected_result.add_child(Node(aId=1, aStrLength=3))
    expected_result.add_child(Node(aId=2, aStrLength=2))
    expected_result.add_child(Node(aId=3, aStrLength=1))
    constructed_tree.update_leaf_list()
    expected_result.update_leaf_list()
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint(inputstr))
    # print('actual:')
    # print(constructed_tree.fancyprint(inputstr))
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)
    
    inputstr = farach.str2int('11')
    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    innernode = Node(aId='inner', aStrLength=1)
    expected_result.add_child(innernode)
    innernode.add_child(Node(aId=1, aStrLength=3))
    innernode.add_child(Node(aId=2, aStrLength=2))
    expected_result.add_child(Node(aId=3, aStrLength=1))
    constructed_tree.update_leaf_list()
    expected_result.update_leaf_list()
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint(inputstr))
    # print('actual:')
    # print(constructed_tree.fancyprint(inputstr))
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)
    

    inputstr = farach.str2int('111')
    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    inner1 = Node(aId='inner', aStrLength=1)
    inner2 = Node(aId='inner', aStrLength=2)
    leaf1 = Node(aId=1, aStrLength=4)
    leaf2 = Node(aId=2, aStrLength=3)
    leaf3 = Node(aId=3, aStrLength=2)
    leaf4 = Node(aId=4, aStrLength=1)
    expected_result.add_child(inner1)
    expected_result.add_child(leaf4)
    inner1.add_child(inner2)
    inner1.add_child(leaf3)
    inner2.add_child(leaf1)
    inner2.add_child(leaf2)
    constructed_tree.update_leaf_list()
    expected_result.update_leaf_list()
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint(inputstr))
    # print('actual:')
    # print(constructed_tree.fancyprint(inputstr))
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)


    # inputstr = farach.str2int('122')
    # constructed_tree = farach.construct_suffix_tree(inputstr)
    # expected_result = Node(aId='root')
    # expected_result.add_child(Node(aId=1, aStrLength=[12]))
    # assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)

    inputstr = farach.str2int('1222')
    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    inner1 = Node(aId='inner', aStrLength=1)
    inner2 = Node(aId='inner', aStrLength=2)
    leaf1 = Node(aId=1, aStrLength=5)
    leaf2 = Node(aId=2, aStrLength=4)
    leaf3 = Node(aId=3, aStrLength=3)
    leaf4 = Node(aId=4, aStrLength=2)
    leaf5 = Node(aId=5, aStrLength=1)
    expected_result.add_child(leaf1)
    expected_result.add_child(inner1)
    expected_result.add_child(leaf5)
    inner1.add_child(inner2)
    inner1.add_child(leaf4)
    inner2.add_child(leaf2)
    inner2.add_child(leaf3)
    expected_result.update_leaf_list()
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint(inputstr))
    # print('actual:')
    # print(constructed_tree.fancyprint(inputstr))
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)

    # inputstr = farach.str2int('1221')
    # constructed_tree = farach.construct_suffix_tree(inputstr)
    # expected_result = Node(aId='root')
    # expected_result.add_child(Node(aId=1, aStrLength=[12]))
    # assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)

    # inputstr = farach.str2int('2221')
    # constructed_tree = farach.construct_suffix_tree(inputstr)
    # expected_result = Node(aId='root')
    # expected_result.add_child(Node(aId=1, aStrLength=[12]))
    # assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)

    banana_test()

    print('tests succeeded!')


def current_test():
    inputstr = farach.str2int('1222')
    constructed_tree = farach.construct_suffix_tree(inputstr)
    expected_result = Node(aId='root')
    inner1 = Node(aId='inner', aStrLength=[2])
    inner2 = Node(aId='inner', aStrLength=[2])
    leaf1 = Node(aId=1, aStrLength=[1, 2, 2, 2, 3])
    leaf2 = Node(aId=2, aStrLength=[2, 3])
    leaf3 = Node(aId=3, aStrLength=[3])
    leaf4 = Node(aId=4, aStrLength=[3])
    leaf5 = Node(aId=5, aStrLength=[3])
    expected_result.add_child(leaf1)
    expected_result.add_child(inner1)
    expected_result.add_child(leaf5)
    inner1.add_child(inner2)
    inner1.add_child(leaf4)
    inner2.add_child(leaf2)
    inner2.add_child(leaf3)
    # print('-'*80)
    # print('inputstr: %s' % inputstr)
    # print('expected:')
    # print(expected_result.fancyprint(inputstr))
    # print('actual:')
    # print(constructed_tree.fancyprint(inputstr))
    assert constructed_tree.fancyprint(inputstr) == expected_result.fancyprint(inputstr)


def banana_test():
    # banana
    # 123232
    inputstr = farach.str2int('123232')

    root = Node(aId="root")
    root.add_child(Node(7, 1))

    inner = Node(1, "inner")
    root.add_child(inner)

    inner2 = Node(3, "inner")
    inner2.add_child(Node(6, 2))
    inner2.add_child(Node(4, 4))

    inner.add_child(inner2)

    inner.add_child(Node(2, 6))

    inner = Node(2, "inner")

    inner.add_child(Node(5, 3))
    inner.add_child(Node(3, 5))

    root.add_child(inner)

    root.add_child(Node(1, 7))

    constructed_tree = farach.construct_suffix_tree(inputstr)
    root.update_leaf_list()

    # print(constructed_tree.fancyprint(inputstr))
    # print(root.fancyprint(inputstr))

    assert constructed_tree.fancyprint(inputstr) == root.fancyprint(inputstr)


def main():
    run_tests()


if __name__ == '__main__':
    main()
