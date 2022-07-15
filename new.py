import networkx as nx
import matplotlib.pyplot as plt

# Draws the graphs with their edges and weights along side
def nor_graph(n,G):

  for i in range(1, n + 1):
    G.add_node(i)

  e = int(input("Enter number of edges : "))
  print("Format : From_node, To_node, weight")

  for j in range(e):
    x = input()
    x = x.split(',')
    G.add_edge(int(x[0]), int(x[1]),weight = int(x[2]))

  plt.figure() 
  pos = nx.shell_layout(G)
  nx.draw(G,pos, node_color=['grey'], with_labels=True,font_color = 'white')
  labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# show_spath() finds the shortest path between 2 nodes

def show_spath(from_node, to_node):
    plt.figure()    
    pos = nx.shell_layout(G)
    
    weight_labels = nx.get_edge_attributes(G,'weight')
    
    path = nx.dijkstra_path(G, source = from_node, target = to_node)

    edges_path = list(zip(path,path[1:]))
    edges_path_reversed = [(y,x) for (x,y) in edges_path]
    edges_path = edges_path + edges_path_reversed
    edge_colors = ['black' if not edge in edges_path else 'red' for edge in G.edges()]

    nx.draw(G, pos, with_labels = True, font_color = 'white', edge_color= edge_colors,node_color=['grey']) 
    nx.draw_networkx_edge_labels(G,pos,edge_labels= weight_labels)


G = nx.Graph()
n = int(input("Enter number of nodes : "))
nor_graph(n, G)
show_spath(1,2)
