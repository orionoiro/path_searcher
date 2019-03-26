from graph import Digraph, Node, WeightedEdge


def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph
    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            32 76 54 23
        This entry would become an edge from 32 to 76.
    Returns:
        a Digraph representing the map
    """

    g = Digraph()
    with open(map_filename, 'r') as file:
        read_data = file.read().split('\n')

    for elem in read_data:
        read_data[read_data.index(elem)] = elem.split(' ')
    read_data.remove([''])

    for elem in read_data:
        start = Node(elem[0])
        dest = Node(elem[1])

        try:
            g.add_node(start)
        except ValueError:
            pass
        try:
            g.add_node(dest)
        except ValueError:
            pass

        edge1 = WeightedEdge(start, dest, int(elem[2]), int(elem[3]))
        try:
            g.add_edge(edge1)
        except ValueError:
            pass

    return g


def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    start = Node(start)
    end = Node(end)
    path[0].append(start.get_name())

    if start not in digraph.nodes or end not in digraph.nodes:
        raise ValueError
    elif start == end:
        return tuple([path[0].copy(), path[1]])
    else:
        for edge in digraph.edges[start]:
            if edge.get_destination().get_name() not in path[0]:
                if len(best_path) == 0 or len(path[0]) < len(best_path):
                    if path[2] + edge.get_outdoor_distance() <= max_dist_outdoors:
                        path[1] += edge.get_total_distance()
                        path[2] += edge.get_outdoor_distance()
                        next_path = get_best_path(digraph, edge.get_destination(), end, path,
                                                  max_dist_outdoors, best_dist, best_path)
                        path[0].remove(edge.get_destination().get_name())
                        path[1] -= edge.get_total_distance()
                        path[2] -= edge.get_outdoor_distance()
                    else:
                        continue

                    if next_path is not None:
                        if best_dist == 0 or next_path[1] < best_dist:
                            best_path = next_path[0]
                            best_dist = next_path[1]

        if best_dist == 0:
            return None
        return tuple([best_path, best_dist])


def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search.
    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings).

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    search_result = get_best_path(digraph, start, end, [[], 0, 0], max_dist_outdoors, 0, [])
    try:
        if search_result[-1] <= max_total_dist:
            return search_result[0]
        else:
            raise ValueError
    except TypeError:
        raise ValueError
