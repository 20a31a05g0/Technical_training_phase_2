def DFS(graph,start):
    s=[start]
    visited=[start]
    while len(s)!=0:
        b=s.pop()
        print(b)
        for i in graph[b]:
            if i not in visited:
                s.append(i)
                visited.append(i)
g={'a':['b','c'],
      'b':['a','c'],
      'c':['a','d'],
      'd':['c','b','e'],
      'e':['d']
   }
DFS(g,'d')
                
