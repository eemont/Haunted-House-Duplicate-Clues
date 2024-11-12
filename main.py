class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list_with_cycle(values):
    head = ListNode(values[0])
    current = head
    nodes = {values[0]: head}
    
    # Traverse and create the linked list
    cycle_start = None
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        
        # Create the cycle if the value has been seen before
        if val in nodes and cycle_start is None:
            cycle_start = nodes[val]
        
        # Store the node reference
        nodes[val] = new_node

    # Create the cycle at the first duplicate encountered
    if cycle_start:
        current.next = cycle_start

    return head

def find_duplicate_clue(rooms):
    # Step 1: Detect the cycle
    slow = rooms
    fast = rooms
    
    # Move `slow` by 1 step and `fast` by 2 steps, checking for None
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # If there's no cycle, return None or raise an exception
        raise ValueError("No duplicates found")

    # Step 2: Find the start of the cycle (duplicate)
    slow2 = rooms
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next

    return slow.val

if __name__ == "__main__":
    # Input
    user_input = input("\nInput: \n\n")
    values = list(map(int, user_input.split()))

    # Build the linked list with a cycle for the duplicate clue
    rooms = build_linked_list_with_cycle(values)

    # Output
    try:
        duplicate_clue = find_duplicate_clue(rooms)
        print(f"\nOutput:\n\n{duplicate_clue}\n")
    except ValueError as e:
        print(e)
