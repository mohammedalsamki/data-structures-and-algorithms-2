def left_join(table_1, table_2):
    """
    A function takes two hashtables and performs left join and adding the joined hashes to a list.
    Arguments:
        table_1 : The left hashtbale instance.
        table_2 : The right hashtable instance.
    Returns:
        output: a list of values after left join.
    """
    output = []
    table_1_buckets=table_1.buckets
    for item in table_1_buckets:
        if item:
            current = item.head
            while current:
                hashed = table_1.hash(current.value[0])
                target = table_2.buckets[hashed]
                if not target:
                    output.append((current.value[0], (current.value[1], None)))
                    current = current.next
                    continue
                target = target.head
                while target:
                    if target.value[0] == current.value[0]:
                        output.append((current.value[0], (current.value[1], target.value[1])))
                    target = target.next
                current = current.next
    return output
