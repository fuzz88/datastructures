import argparse


def topo_sort(graph):
    sorted_graph = []
    marked = {vertex: "not visited" for vertex in graph}
    found_cycle = False
    for vertex in graph:
        if marked[vertex] == "not visited":
            found_cycle = visit(graph, vertex, marked, sorted_graph,
                                found_cycle)
        if found_cycle:
            break
    if found_cycle:
        sorted_graph = ["Cycle found. Cannot Sort."]
    sorted_graph.reverse()
    return sorted_graph


def visit(graph, vertex, marked, sorted_graph, found_cycle):
    if found_cycle:
        return True
    marked[vertex] = "visiting"
    for edge in graph[vertex]:
        if marked[edge] == "visiting":
            return True
        if marked[edge] == "not visited":
            if visit(graph, edge, marked, sorted_graph, found_cycle):
                return True
    marked[vertex] = "visited"
    sorted_graph.append(vertex)
    return False


def build_graph(filename):
    graph = {}
    values = []
    with open(filename, 'r') as reader:
        for line in reader:
            line = line.strip()
            nodes = [int(node) for node in line.split()]
            key = nodes[0]
            nodes = nodes[1:]
            for i in range(len(nodes)):
                values.append(nodes[i])
            graph[key] = nodes
    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Builds a graph,\
                                     checks for cycles, sorts the graph\
                                     topographically")
    parser.add_argument("file", type=str, help="Location of graph")
    args = parser.parse_args()
    sorted_graph = topo_sort(build_graph(args.file))
    for node in sorted_graph:
        print(node)
