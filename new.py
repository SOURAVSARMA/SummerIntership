import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # Creating a global graph opbject G  
graph_input()
nor_graph()
show_spath()

def graph_input():
  n = int(input("Enter number of nodes : ")) # Number of Nodes

  for i in range(1, n + 1): # Adding nodes
    G.add_node(i)

  e = int(input("Enter number of edges : ")) # Number of edges
  
  # Check for edge
  if not ((e > 0) and (e <= ((n*(n+1))/2-n))) :
    print("Invalid Edge")
    nor_graph(n,G) 

  elif (e == 0):

    plt.figure() 
    pos = nx.shell_layout(G)
    nx.draw(G,pos, node_color=['grey'], with_labels=True,font_color = 'white')
    sys.exit("No shortest path possible") 

  # Taking input of edges with their weights
  print("Format : From_node, To_node, weight") 
  
  for j in range(e): 
    x = input()
    x = x.split(',')

    # Check for valid node and weight 
    if ((int(x[0]) > 0) and (int(x[0]) <= n) and (int(x[1]) > 0) and (int(x[1]) <= n) and (int(x[2]) >= 0)) :
      G.add_edge(int(x[0]), int(x[1]),weight = int(x[2]))
    else :
      print("Invalid Entry")
      nor_graph(n,G)

    # Taking the sorce - destination pair and printing the graph with shortest path
    m = int(input("Enter number of shortest path you want : "))
    for k in range(m):
      a = int(input("Enter source node : "))
      b = int(input("Enter destination node : "))
      show_spath(a,b)

# nor_graph() : Plots the graph after input
def nor_graph(): 

  plt.figure() 
  pos = nx.shell_layout(G)
  nx.draw(G,pos, node_color=['grey'], with_labels=True,font_color = 'white')
  labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# show_spath() finds the shortest path between 2 nodes
def show_spath(from_node, to_node):

    # Check for valid path
    plt.figure()    
    pos = nx.shell_layout(G)
    
    weight_labels = nx.get_edge_attributes(G,'weight')
    
    # Try - catch block for no route possible
    try:
     path = nx.dijkstra_path(G, source = from_node, target = to_node)
    except Exception as err:
      print(err)
      return
  
    edges_path = list(zip(path,path[1:]))
    edges_path_reversed = [(y,x) for (x,y) in edges_path]
    edges_path = edges_path + edges_path_reversed
    edge_colors = ['black' if not edge in edges_path else 'red' for edge in G.edges()]

    nx.draw(G, pos, with_labels = True, font_color = 'white', edge_color= edge_colors,node_color=['grey']) 
    nx.draw_networkx_edge_labels(G,pos,edge_labels= weight_labels)