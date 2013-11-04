import java.util.NoSuchElementException

public class BST<Key extends Comparable<Key>, Value> {
  private Node root; //The root of the BST
  
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
  
  private Node delete(Node x, Key key) {
    if (x == null) return null;
    int comparator = key.compareTo(x.key);
    if (comparator < 0) return delete(x.left, key);
    else if (comparator > 0) return delete(x.right, key);
    else {
      if (x.right == null) return x.left;
      if (x.left == null) return x.right;
      
    }
  }
}