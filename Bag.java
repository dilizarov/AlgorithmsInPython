import java.util.Iterator;
import java.util.NoSuchElementException;

public class Bag<Item> implements Iterable<Item> {
  private int N;  //No. of elements
  private Node<Item> first; // Starts bag

  private class Node<Item> {
    private Item item;
    private Node<Item> next;
  }
  
  public Bag() {
    this.first = null;
    this.N = 0;
  }
  
  public boolean isEmpty() {
    return this.first == null;
  }
  
  public int size() {
    return this.N;
  }
  
  public void add(Item item) {
    Node<Item> temp = this.first;
    first = new Node<Item>();
    first.item = item;
    first.next = temp;
    this.N++;
  }
  
  public Iterator<Item> iterator() {
    return new ListIterator<Item>(this.first);
  }
  
  private class ListIterator<Item> implements Iterator<Item> {
    private Node<Item> current;
    
    public ListIterator(Node<Item> first) {
      this.current = first;
    }
    
    //It is intuitive because this condition is checked on calls of "Next"
    //We can't proceed if we're dealing with null, hence it terminates.
    public boolean hasNext() { return current != null; }
    public void remove() { System.out.println("Not supported, brah"); }
    
    public Item next() {
      if (!hasNext()) throw new NoSuchElementException("We're done!");
      Item item = this.current.item;
      current = current.next;
      return item;
    }
  }

  // public static void main(String[] args) {
//     Bag<String> bag = new Bag<String>();
//     bag.add("a"); bag.add("d"); bag.add("b"); bag.add("e");
//     bag.add("h"); bag.add("g"); bag.add("f"); bag.add("Yessssh");
//     for (String s : bag) {
//       System.out.println(s);
//     }
//   }
}