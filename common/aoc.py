def read_groups(x, map_fn=None, sep="\n\n"):
    groups = [[line for line in group.rstrip().split('\n')] for group in x.split('\n\n')]
    if map_fn:
        for i in range(len(groups)):
            groups[i] = list(map(map_fn, groups[i]))
    return groups

def merge_groups(groups):
    return [item for group in groups for item in group]