
def init_node(val):
    new_node = {
        "value": val,
        "next": None
    }

    return new_node


def append_to_ll(tail, value):
    new_node = init_node(value)
    tail["next"] = new_node
    return new_node


def pop_out_ll(head):
    head = head["next"]
    return head


def push_to_ll(head, val):
    new_node = init_node(val)
    new_node['next'] = head
    new_head = new_node
    return new_head


head = tail = init_node(20)

tail = append_to_ll(tail, 40)
tail = append_to_ll(tail, 70)
tail = append_to_ll(tail, 50)
print(head)
print(tail)

head = pop_out_ll(head)

print(head)
print(tail)

head = push_to_ll(head, 79)

print(head)
print(tail)




