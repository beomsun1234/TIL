package main

import "fmt"

type Tree struct {
	Node *Node
}

func NewTree() *Tree {
	return &Tree{}
}

/*
	완전이진트리
*/
func (t *Tree) insert(n *Node) {
	if t.Node == nil {
		t.Node = n
		return
	}
	insertBFS(t.Node, n)

	//insertDFS(t.Node, n)
}
func insertDFS(p *Node, n *Node) {
	if p.left == nil {
		p.left = n
	} else if p.right == nil {
		p.right = n
	} else {
		insertDFS(p.left, n)
	}
}
func insertBFS(p *Node, n *Node) {
	q := make(chan *Node, 100)
	q <- p

	for len(q) > 0 {
		node := <-q
		if node.left == nil {
			node.addLeft(n)
			return
		} else {
			q <- node.left
		}

		if node.right == nil {
			node.addRight(n)
			return
		} else {
			q <- node.right
		}
	}
}

func NewNode(val int) *Node {
	return &Node{
		val: val,
	}
}

type Node struct {
	val   int
	left  *Node
	right *Node
}

func (n *Node) addLeft(left *Node) {
	n.left = left
}

func (n *Node) addRight(right *Node) {
	n.right = right
}

func preorderTraversal(n *Node) {
	if n == nil {
		return
	}
	fmt.Print(n.val, " ")
	preorderTraversal(n.left)
	preorderTraversal(n.right)
}

func inorderTraversal(n *Node) {
	if n == nil {
		return
	}
	inorderTraversal(n.left)
	fmt.Print(n.val, " ")
	inorderTraversal(n.right)
}
func postorderTraversal(n *Node) {
	if n == nil {
		return
	}
	postorderTraversal(n.left)
	postorderTraversal(n.right)
	fmt.Print(n.val, " ")
}

func main() {
	tree := NewTree()
	root := NewNode(1)
	/**
		   1
		2    3
	   4 5  6 7
	**/
	tree.insert(root)
	tree.insert(NewNode(2))
	tree.insert(NewNode(3))
	tree.insert(NewNode(4))
	tree.insert(NewNode(5))
	tree.insert(NewNode(6))
	tree.insert(NewNode(7))

	preorderTraversal(root)
	println("")
	inorderTraversal(root)
	println("")
	postorderTraversal(root)
}
