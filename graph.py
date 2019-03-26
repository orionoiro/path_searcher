# A set of data structures to represent graphs


class Node(object):
    """Represents a node in the graph"""

    def __init__(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # This function makes the Nodes hashable so that they can be used as keys in dict, even though Nodes are mutable
        return self.name.__hash__()


class Edge(object):
    """Represents an edge in the dictionary. Includes a source and
    a destination."""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{}->{}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, total_distance, outdoor_distance):
        self.src = src
        self.dest = dest
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance

    def get_total_distance(self):
        return self.total_distance

    def get_outdoor_distance(self):
        return self.outdoor_distance

    def __str__(self):
        return '{}->{} '.format(self.src, self.dest) + str((self.total_distance, self.outdoor_distance))


class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""

    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # dict of Node -> list of edges

    def __str__(self):
        edge_strs = []
        for edges in self.edges.values():
            for edge in edges:
                edge_strs.append(str(edge))
        edge_strs = sorted(edge_strs)
        return '\n'.join(edge_strs)  # concat edge_strs with "\n"s between them

    def get_edges_for_node(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, node):
        """Adds a Node object to the Digraph. Raises a ValueError if it is
        already in the graph."""
        if node in self.nodes:
            raise ValueError
        else:
            self.nodes.add(node)

    def add_edge(self, edge):
        """Adds an Edge or WeightedEdge instance to the Digraph. Raises a
        ValueError if either of the nodes associated with the edge is not
        in the graph."""
        if edge.get_source() not in self.nodes:
            raise ValueError
        elif edge.get_destination() not in self.nodes:
            raise ValueError
        elif edge.get_source() in self.edges:
            self.edges[edge.get_source()].append(edge)
        else:
            self.edges[edge.get_source()] = []
            self.edges[edge.get_source()].append(edge)
