class Graph:
  def __init__(self, gdict=None):
    if gdict is None:
      gdict = {}
    self.gdict = gdict
  def getVertices(self):
    return list(self.gdict.keys())
  def getEdges(self):
    res = []
    for key, values in self.gdict.items():
      for vert in values:
        edge = [key, vert]
        sorted_edge = sorted(edge)
        if {key, vert} not in res:
          res.append({key, vert})
    return res

graph = {
    "a": ["b", "c"],
    "b": ["a", "d"], 
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
    }

gr = Graph(graph)
# print(gr.getVertices())
print(gr.getEdges())
