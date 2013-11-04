import Bag

public class Graph {
  private final int V; //size
  private Bag<Integer>[] adj;
  
  public Graph(int v) {
    this.V = v;
    this.adj = (Bag<Integer>[]) new Bag[v];
    for(int i = 0; i < v; i++) adj[i] = new Bag<Integer>();
  }
  
  public void addEdge(int v, int w) {
    this.adj[v].add(w);
    this.adj[w].add(v);
  }
  
  public Iterable<Integer> adj(int v) {
    return adj[v];
  }
}