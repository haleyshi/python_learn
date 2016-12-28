import random
import time
import sys

class Node:
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

    def __str__(self):
        str = "value: %d" % self.value

        if self.next == None:
            str += ", next: None"
        else:
            str += ", next: %d" % self.next.value

        if self.random == None:
            str += ", random: None"
        else:
            str += ", random: %d" % self.random.value

        return str


def gen_linklist(size):
    nodes = {}
    nodes[size-1] = Node(value=size-1)

    for i in range(size-2, -1, -1):
        nodes[i] = Node(value=i, next=nodes[i+1])

    for i in range(0, size):
        j = random.randint(0,size+200)
        if j < size:
            if j != i:
                nodes[i].random = nodes[j]

    print "Use memory: %f MB" % (sys.getsizeof(nodes) / 1024 / 1024)

    return nodes[0]


def print_linklist(head_x):
    current = head_x

    while current is not None:
        print current
        current = current.next


def clone_linkset_1(head_x):
    if head_x is None:
        return None

    current = head_x

    while current is not None:
        next = current.next
        current_prime = Node(value=current.value, next=current.next)
        current.next = current_prime
        current = next

    head_prime = head_x.next

    current = head_x
    while current is not None:
        random = current.random
        if random is None:
            current.next.random = None
        else:
            current.next.random = random.next

        current_prime = current.next
        current.next = current_prime.next

        current = current.next
        if current is None:
            current_prime.next = None
        else:
            current_prime.next = current.next

    return head_prime


def clone_linkset_2(head_x):
    if head_x is None:
        return None

    hashmap = {}

    head_prime = Node(value=head_x.value)

    random = head_x.random
    if random is not None:
        random_prime = Node(value=random.value)
        head_prime.random = random_prime
        hashmap[random] = random_prime
    else:
        head_prime.random = None

    current = head_x.next
    previous = head_prime

    while current is not None:
        if hashmap.has_key(current):
            current_prime = hashmap[current]
        else:
            current_prime = Node(value=current.value)

        previous.next = current_prime
        random = current.random

        if random is not None:
            if hashmap.has_key(random):
                random_prime = hashmap[random]
            else:
                random_prime = Node(value=random.value)
                hashmap[random] = random_prime

            current_prime.random = random_prime
        else:
            current_prime.random = None

        current = current.next
        previous = current_prime

    print "Use extra memory: %f MB" % (sys.getsizeof(hashmap) / 1024 / 1024)

    return head_prime


def clone_linkset_3(head_x):
    if head_x is None:
        return None

    hashmap = {}

    head_prime = Node(value=head_x.value)
    hashmap[head_x] = head_prime

    current = head_x.next
    previous = head_prime

    while current is not None:
        current_prime = Node(value=current.value)
        hashmap[current] = current_prime
        previous.next = current_prime
        current = current.next
        previous = current_prime

    current = head_x
    current_prime = head_prime

    while current is not None:
        random = current.random
        if random is not None:
            current_prime.random = hashmap[random]
        current = current.next
        current_prime = current_prime.next

    print "Use extra memory: %f MB" % (sys.getsizeof(hashmap) / 1024 / 1024)

    return head_prime

#print sys.maxsize
size = 2000000
print "creating the sample linkset with %d nodes..." %size
start = time.time()
head = gen_linklist(size)
end = time.time()
print "original linkset created in %f secs" % (end - start)
#print "Original Linkset:"
#print_linklist(head)

print "cloning..."
start = time.time()
head_prime = clone_linkset_1(head)
end = time.time()
print "Clone without hashmap costs %f secs" % (end - start)
#print "Cloned Linkset 1:"
#print_linklist(head_prime)

print "cloning..."
start = time.time()
head_prime2 = clone_linkset_2(head)
end = time.time()
print "Clone with random hashmap costs %f secs" % (end - start)
#print "Cloned Linkset 2:"
#print_linklist(head_prime2)

print "cloning..."
start = time.time()
head_prime3 = clone_linkset_3(head)
end = time.time()
print "Clone with full hashmap costs %f secs" % (end - start)
#print "Cloned Linkset 3:"
#print_linklist(head_prime3)






