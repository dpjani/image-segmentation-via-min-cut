# This is a script for comparing time complexity of min-cut algorithm and karger's algorithm for simple random graph with n = 10,20,... nodes. 


import time
import networkx as nx
import matplotlib.pyplot as plt

def karger_min_cut(graph):
    while len(graph) > 2:
        u, v = random.choice(list(graph.edges))
        graph = nx.contracted_edge(graph, (u, v))
    return graph

def max_flow_min_cut(graph):
    # Use NetworkX's built-in max-flow min-cut algorithm
    cut_value, partition = nx.minimum_cut(graph, 's', 't')
    reachable, non_reachable = partition
    return graph.subgraph(reachable), graph.subgraph(non_reachable)

def compare_algorithms(graph_sizes):
    karger_times = []
    max_flow_min_cut_times = []
    for n in graph_sizes:
        graph = nx.complete_graph(n)
        graph.add_node('s')
        graph.add_node('t')
        for node in graph.nodes:
            if node != 's' and node != 't':
                graph.add_edge('s', node, capacity=1)
                graph.add_edge(node, 't', capacity=1)

        start_time = time.time()
        karger_result = karger_min_cut(graph.copy())
        karger_time = time.time() - start_time
        karger_times.append(karger_time)

        start_time = time.time()
        max_flow_min_cut_result, _ = max_flow_min_cut(graph.copy())
        max_flow_min_cut_time = time.time() - start_time
        max_flow_min_cut_times.append(max_flow_min_cut_time)

    plt.plot(graph_sizes, karger_times, label="Karger's Algorithm")
    plt.plot(graph_sizes, max_flow_min_cut_times, label="Max-Flow Min-Cut Algorithm")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Algorithms')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graph_sizes = [10, 20, 50, 100, 200, 500]  # Adjust the sizes as needed
    compare_algorithms(graph_sizes)
