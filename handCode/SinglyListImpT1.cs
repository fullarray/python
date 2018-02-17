public class Node{
	public Node Next;
	public object Value;
}

public class LinkedList{
	private Node head;
	private Node current;
	public int count;
}

public LinkedList(){
	head = new Node();
	current = head;
}

public void addAtLast(object data){
	Node newNode = new Node();
	newNode.Value = data;
	current.Next = newNode;
	current = newNode;
	count++;
}

public void addAtStart(object data){
	Node newNode = new Node() {	Value = data };
	newNode.Next = head.Next;
	head.Next = newNode;
	count++;
}

public void removeFromStart(){
	if(count > 0){
		head.Next = head.Next.Next;
		Count--;
	}else{
		Console.WriteLine("No element.");
	}
}

public void printAllNode(){
	Console.Write("Head ->");
	Node curr = head;
	while(curr.Next != null){
		curr = curr.Next;
		Console.Write(curr.Value);
		Console.Write("->");
	}
	Console.Write("NULL");
}

class Program{
	static void Main(string[] args){
		LinkedList lnkList = new LinkedList();
		lnkList.printAllNode();
		Console.WriteLine();
		
		lnkList.addAtLast(15);
		lnkList.addAtLast("Mike");
		lnkList.addAtLast(76);
		lnkList.addAtLast(20);
		lnkList.printAllNode();
		Console.WriteLine();
		
		lnkList.addAtStart(93);
		lnkList.printAllNode();
		Console.WriteLine();
		
		lnkList.removeFromStart();
		lnkList.printAllNode();
		
		Console.ReadKey();
	}
}