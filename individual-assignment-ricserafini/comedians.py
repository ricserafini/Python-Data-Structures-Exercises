#%%
import csv


def parse_csv_to_graph(path):
    rows = []
    with open(comedians, 'r') as f:
        reader = csv.reader(f)

        # Skip header row
        next(reader, None)

        for row in reader:
            rows.append(row)


    graph = dict()
    for row in rows:
        commedians, target, relation = row
        if not target in graph:
            graph[target] = []
        graph[target].append((commedians, relation))

    return graph
print(parse_csv_to_graph(comedians))

#%%
def influence_chains(diagram, start, end=None):
    pass

#%%
def top_10_influencers(diagram):
    pass

#%%
def draw_graph(diagram, node_size = 4, edge_size = 0.2):
    pass
#%%
