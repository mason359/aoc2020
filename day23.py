from aocutils import get_raw

def problem1():
    num_moves = 100
    cups = [int(cup) for cup in get_raw(23)]
    head, mapping = setup(cups)
    simulate(head, mapping, num_moves, len(cups))
    string = ''
    curr = mapping[1].next
    while curr.num != 1:
        string += str(curr.num)
        curr = curr.next
    return string

def problem2():
    num_cups = 1_000_000
    num_moves = 10_000_000
    cups = [int(cup) for cup in get_raw(23)] + list(range(10, num_cups + 1))
    head, mapping = setup(cups)
    simulate(head, mapping, num_moves, num_cups)
    one = mapping[1]
    return one.next.num * one.next.next.num

class Node:

    def __init__(self, num):
        self.num = num
        self.next = None

def setup(cups):
    mapping = {}
    head = Node(cups[0])
    mapping[cups[0]] = head
    current = head
    for cup in cups[1:]:
        current.next = Node(cup)
        mapping[cup] = current.next
        current = current.next
    current.next = head
    return head, mapping

def simulate(current, mapping, num_moves, num_cups):
    for i in range(num_moves):
        removed = current.next
        removed_nums = [node.num for node in [removed, removed.next, removed.next.next]]
        current.next = removed.next.next.next
        destination = current.num - 1 if current.num != 1 else num_cups
        while destination in removed_nums:
            destination -= 1
            if destination < 1: destination = num_cups
        destination = mapping[destination]
        temp = destination.next
        destination.next = removed
        removed.next.next.next = temp
        current = current.next
    return current