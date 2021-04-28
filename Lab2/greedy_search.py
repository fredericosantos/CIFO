def getDistance(node1, node2):
    return np.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)


def getPair(distances, path, nodes_to_remove=[], maximize=True):
    distance_pairs = [(d, (path[i], path[i + 1])) for i, d in enumerate(distances)]
    pairs_to_remove = []
    for i, (d, (n0, n1)) in enumerate(distance_pairs):
        if (n0 in nodes_to_remove) or (n1 in nodes_to_remove):
            pairs_to_remove.append(distance_pairs[i])
    for p in pairs_to_remove:
        distance_pairs.remove(p)
    if maximize == True:
        n_longest = distance_pairs.index(max(distance_pairs, key=lambda x: x[0]))
    if maximize == False:
        n_longest = distance_pairs.index(min(distance_pairs, key=lambda x: x[0]))
    return distance_pairs[n_longest][1]


def getMaxValueKey(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def getWorstNode(distances, path, nodes_to_remove=[], maximize=True):
    distance_pairs = [(d, (path[i], path[i + 1])) for i, d in enumerate(distances)]
    pairs_to_remove = []
    for i, (d, (n0, n1)) in enumerate(distance_pairs):
        if (n0 in nodes_to_remove) or (n1 in nodes_to_remove):
            pairs_to_remove.append(distance_pairs[i])
    for p in pairs_to_remove:
        distance_pairs.remove(p)
    node_distances = {}
    for i, node in enumerate(path[:-1]):
        if i == 0:
            node_distances[node] = distances[0] + distances[-1]
        else:
            node_distances[node] = distances[i - 1] + distances[i]
    for node in nodes_to_remove:
        node_distances.pop(node, None)
    return getMaxValueKey(node_distances)


def checkNodeLinked(network, node):
    if len(network[node]) > 1:
        return True
    else:
        return False


def linkNode(network, node, closest_node, nodes_to_remove):
    tmp_node = [i for i in network[node]]
    if checkNodeLinked(network, node):
        nodes_to_remove.append(node)
    if checkNodeLinked(network, closest_node):
        tmp_node2 = [i for i in network[closest_node]]
        network[network[closest_node][-1]] += tmp_node
        network[tmp_node[-1]] += tmp_node2
        nodes_to_remove.append(closest_node)
    else:
        network[network[node][-1]] += network[closest_node]
        network[network[closest_node][-1]] += tmp_node
    return network, nodes_to_remove


def getClosestNode(search_space, node, available_nodes):
    closest_node, _ = min(
        [(i, d) for i, d in enumerate(search_space[node]) if i in available_nodes],
        key=lambda x: x[1],
    )
    return closest_node


def getAvailableNodes(search_space, network, node, nodes_to_remove):
    nodes_to_remove = list(set(nodes_to_remove))
    nodes = list(range(len(search_space)))
    total_nodes_to_remove = nodes_to_remove + [network[node][0], network[node][-1]]
    for n in total_nodes_to_remove:
        if n in nodes:
            nodes.remove(n)
    return nodes


def cleanNetwork(network, nodes_to_remove):
    nodes_to_remove = list(set(nodes_to_remove))
    for node in nodes_to_remove:
        if node in network.keys():
            del network[node]
    return network, nodes_to_remove


def initNode(search_space, network, node_init, nodes_to_remove):
    if node_init in network.keys():
        return network[node_init]
    else:
        for node_key, linked_nodes in network.items():
            if node_init in linked_nodes:
                idx = linked_nodes.index(node_init)
                closest_node = getClosestNode(
                    search_space,
                    node_init,
                    [linked_nodes[idx - 1], linked_nodes[idx + 1]],
                )
                if linked_nodes[idx + 1] == closest_node:
                    return network[node_key]


def findPath(search_space, network, node_init, nodes_to_remove):
    path = [i for i in initNode(search_space, network, node_init, nodes_to_remove)]
    available_nodes = getAvailableNodes(search_space, network, path[0], nodes_to_remove)
    node = path[-1]
    while len(available_nodes) > 0:
        node = getClosestNode(search_space, node, available_nodes)
        path += network[node]
        for n in network[node]:
            if n in available_nodes:
                available_nodes.remove(n)
    path.append(path[0])
    return path


def findDistancePath(search_space, path):
    distance = []
    for i, node in enumerate(path[:-1]):
        distance.append(search_space[node][path[i + 1]])
    return distance