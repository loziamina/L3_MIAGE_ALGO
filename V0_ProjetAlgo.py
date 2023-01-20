#first step 
        
#approche du graphe 
if __name__ == "__main__":
    # -----------------------
    # Partie 1 du sujet de TP
    # -----------------------
    #A very simple graph to test functions locally

    G = {
        "a": ["b"],
        "b": ["c"],
        "c": ["d", "a"],
        "d": ["a"],
       
    }
    ParcoursLargeur(G, "a")

# fonction interne a la classe du graphe "le constructeur"
class Graph :
    def __init__(self, n=0) :
        self.n = n
        self.adj = [[0]*n for _ in range(n)]

    def add_vertice(self) :
        self.n +=1
        for l in self.adj :
            l.append(0)
        self.adj.append([0]*(self.n))

    def add_edge(self, s, e, p=1) :
        self.adj[s][e] = p

    def exist_edge(self, s, e) :
        return self.adj[s][e] !=0

    def get_order(self) :
        return self.n

    def get_neighbours(self,s) :
        neighbours = []
        for i in range(self.n) :
            if self.adj[s][i] !=0 :
                neighbours.append(i)
        return neighbours

    def get_degree(self, s):
        deg = 0
        for i in range(self.n) :
            deg += self.adj[s][i]!=0
            deg += self.adj[i][s]!=0
        return deg

    def get_vertices(self) :
        return [i for i in range(self.n)]

    def is_directed(self) :
        for i in range(self.n) :
            for j in range(i,self.n) :
                if self.adj[i][j] != self.adj[j][i] :
                    return True
        return False

    def is_undirected_and_eulerian(self) :
        if self.is_directed() :
            return False
        degrees=[]
        for i in range(self.n) :
            # ATTENTION ! La méthode get_degree renvoie le double
            # du degré réel dans le cas d'un graphe non-orienté
            # Pour que le théorème d'Euler fonctionne
            # il faut donc diviser par 2 la valeur obtenue !
            degrees.append((self.get_degree(i)//2)%2)
        print(degrees)
        if sum(degrees) == 0 :
            return True
        elif sum(degrees) == 2 :
            return degrees.index(1), self.n-1-degrees[::-1].index(1)
        return False

    def delete(self,s, e) :
        self.adj[s][e] = 0


    def __repr__(self) :
        rep =""
        for l in self.adj :
            for e in l :
                rep+=f'{e: >3} '
            rep += "\n"
        return rep
