import java.util.NoSuchElementException

public class BST<Key extends Comparable<Key>, Value> {
  private Node root; //The root of the BST
  
  //Many recursive solutions. Iterative approach simple:
  //Replace recursion with while loops.
  
  private class Node {
    private Key key;
    private Value val;
    private Node left, right;
    private int N; //Essentially the size of the tree
    
    public Node(Key key, Value val, int N) {
      this.key = key;
      this.val = val;
      this.N = N;
    }
  }
  
  private int size(Node x) {
    if (x == null) return 0;
    else return x.N;
  }
  
  public int size() {
    return size(root);
  }
  
  public boolean isEmpty() {
    return size() == 0;
  }
  
  private Value get(Node x, Key key) {
    if (x == null) return null;
    int comparator = key.compareTo(x.key);
    if (comparator < 0) return get(x.left, key);
    else if (comparator > 0) return get(x.right, key);
    else return x.val;
  }
  
  public Value get(Key key) {
    return get(root, key);
  }
  
  public boolean contains(Key key) {
    return get(key) != null;
  }
  
  private Node put(Node x, Key key, Value val) {
    if (x == null) return new Node(key, val, 1);
    int comparator = key.compareTo(x.key);
    if (comparator < 0) x.left = put(x.left, key, val);
    else if (comparator > 0) x.right = put(x.right, key, val);
    else x.val = val;
    x.N = 1 + size(x.left) + size(x.right);
    return x;
  }
  
  public void put(Key key, Value val) {
    root = put(root, key, val);
  }
  
  //Could refactor to use min(), max() functions.
  
  private Node deleteMin(Node x) {
    if (x.left == null) return x.right;
    x.left = deleteMin(x.left);
    x.N = size(x.left) + size(x.right) + 1;
    return x;
  }
  
  public void deleteMin() {
    if (isEmpty()) throw new NoSuchElementException("Empty BST");
    root = deleteMin(root);
  }
  
  private Node deleteMax(Node x) {
    if (x.right == null) return x.left;
    x.right = deleteMax(x.right);
    x.N = size(x.left) + size(x.right) + 1;
    return x;
  }
  
  public void deleteMax() {
    if (isEmpty()) throw new NoSuchElementException("Empty BST");
    root = deleteMax(root);
  }
  
  public Key min() {
    if (isEmpty()) return null;
    return min(root).key;
  }
  
  private Node min(Node x) {
    if (x.left == null) return x;
    else return min(x.left);
  }
  
  public Key max() {
    if (isEmpty()) return null;
    return max(root).key;
  }
  
  private Node max(Node x) {
    if (x.right == null) return x;
    else return max(x.right);
  }
  
  private Node delete(Node x, Key key) {
    if (x == null) return null;
    int comparator = key.compareTo(x.key);
    if (comparator < 0) return delete(x.left, key);
    else if (comparator > 0) return delete(x.right, key);
    else {
      if (x.right == null) return x.left;
      if (x.left == null) return x.right;
      Node temp = x;
      x = min(temp.right);
      x.right = deleteMin(temp.right);
      x.left = temp.left;
    }
    
    x.N = size(x.left) + size(x.right) + 1;
    return x;
  }
}