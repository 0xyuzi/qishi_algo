import sys
from heapq import heappush, heappop, heapify 
def shortest_path(adj_list, start_node, end_node):
    distance = { node: sys.maxsize for node in adj_list.keys()}
    distance[start_node] = 0
    visited =set()
    pq = []
    heappush(pq, (0, start_node))
    print(pq)
    # print(distance)
    while pq:
        path_len, node = heappop(pq)
        # print(path_len,node)
        visited.add(node)

        for neighbour, cost in adj_list[node]:
            if neighbour in visited:
                continue 

            if  path_len + cost < distance[neighbour]:
                distance[neighbour] = path_len + cost 
                heappush(pq, (distance[neighbour], neighbour))



    print(distance)
    return distance[end_node]





adj_list = {'Memphis': [('New Orleans', 3), ('Mobile', 7), ('Atlanta', 10), ('Nashville', 15)],
            'New Orleans': [('Mobile', 3), ('Memphis', 3)],
            'Mobile': [('Atlanta', 2), ('Savannah', 6), ('Memphis', 7), ('New Orleans', 3)],
            'Savannah': [('Atlanta', 1), ('Mobile', 6)],
            'Atlanta': [('Nashville', 2), ('Savannah', 1), ('Nashville', 2)],
            'Nashville': [('Memphis', 15), ('Atlanta', 2)]
           }
start_node = 'Memphis'
end_node = 'Nashville'
best_cost = shortest_path(adj_list, start_node, end_node)