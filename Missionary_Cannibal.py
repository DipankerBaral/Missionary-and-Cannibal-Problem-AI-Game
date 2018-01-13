__author__ = 'Saugat Adhikari'

from collections import deque
import pydot
import os
import turtle
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class State(object):

	def __init__(self, missionaries, cannibals, boat_position, by_move):
		self.missionaries = missionaries
		self.cannibals = cannibals
		self.boat_position = boat_position
		self.by_move = by_move


	def __str__(self):
		return "%s, %s %s %s" %(self.by_move, self.missionaries, self.cannibals, self.boat_position)

	def is_valid(self):
		if self.missionaries < 0 or self.missionaries > 3:
			return False
		if self.cannibals < 0 or self.cannibals > 3:
			return False
		if self.missionaries < self.cannibals and self.missionaries > 0:
			return False
		# Check for the other side
		if self.missionaries > self.cannibals and self.missionaries < 3 :
			return False

		return True

	def is_goal(self):
		return self.missionaries == 0 and self.cannibals == 0 and self.boat_position == 0

	def new_states(self):
		op = -1
		boat_move = ""
		if self.boat_position == 0:   #boat_position = 0, Boat is on the right river bank
			op = 1       			  #boat_position = 1, Boat is on the left river bank
			boat_move = ""

		for x in range(3):
			for y in range(3):
				by_move = "%sMissionary %sCannibal %s" %(x, y, boat_move)
				new_state = State(self.missionaries + op*x, self.cannibals + op*y, self.boat_position + op*1, by_move)
				if x+y >= 1 and x+y <= 2 and new_state.is_valid():
					yield new_state


class Node(object):
	def __init__(self, parent, state, depth):
		self.parent = parent
		self.state = state
		self.depth = depth
		self.dot_node = pydot.Node(str(self), style="filled", fillcolor="white")

	def __str__(self):
		return self.state.__str__()


	def successors(self):
		for state in self.state.new_states():
			yield Node(parent=self, state=state, depth=self.depth+1)

	def solution_states(self):
		print ("Solution States:")
		solution = []
		node = self
		solution.append(node)
		while node.parent is not None:
			solution.append(node.parent)
			node = node.parent
		solution.reverse()
		return solution


def Breadth_First_Search(root):
	graph = pydot.Dot(graph_type='digraph')
	graph.add_node(root.dot_node)

	queue = deque([root])
	test_list = []
	while True:
		if not queue:
			return None
		node = queue.popleft()
		if str(node) in test_list:
			continue
		test_list.append(str(node))

		dot_node = node.dot_node
		graph.add_node(node.dot_node)
		if node.parent:
			graph.add_edge(pydot.Edge(node.parent.dot_node, node.dot_node))
		if node.state.is_goal():
			graph.write_png('tree.png')
			return node.solution_states()

		for child in node.successors():
			queue.append(child)



def main():
	initial_state = State(3, 3, 1, "Initial State")
	root = Node(parent=None, state=initial_state, depth=0)
	for state in Breadth_First_Search(root):
		print (state)

	#Turtle
	wn = turtle.Screen()
	wn.screensize(1000,599)
	wn.bgcolor("lightgreen")
	wn.bgpic("E://Study//7th sem//AI//Graphics Downloads//background.gif")

	missionary1 = turtle.Turtle()
	missionary1.color("blue")
	missionary1.shape("E://Study//7th sem//AI//Graphics Downloads//missionary.gif")
	# missionary1.shapesize(2,2,12)
	missionary1.setpos(-170,0)
	missionary1.penup()
	missionary1.speed(0)


	missionary2 = turtle.Turtle()
	missionary2.color("blue")
	missionary2.shape("E://Study//7th sem//AI//Graphics Downloads//missionary.gif")
	missionary2.setpos(-200,0)
	missionary2.penup()
	missionary2.speed(0)

	missionary3 = turtle.Turtle()
	missionary3.color("blue")
	missionary3.shape("E://Study//7th sem//AI//Graphics Downloads//missionary.gif")
	missionary3.setpos(-230,0)
	missionary3.penup()
	missionary3.speed(0)



	cannibal1 = turtle.Turtle()
	cannibal1.color("red")
	cannibal1.shape("E://Study//7th sem//AI//Graphics Downloads//cannibal.gif")
	cannibal1.setpos(-170,-50)
	cannibal1.penup()
	cannibal1.speed(0)

	cannibal2 = turtle.Turtle()
	cannibal2.color("red")
	cannibal2.shape("E://Study//7th sem//AI//Graphics Downloads//cannibal.gif")
	cannibal2.setpos(-200,-50)
	cannibal2.penup()
	cannibal2.speed(0)

	cannibal3 = turtle.Turtle()
	cannibal3.color("red")
	cannibal3.shape("E://Study//7th sem//AI//Graphics Downloads//cannibal.gif")
	cannibal3.setpos(-230,-50)
	cannibal3.penup()
	cannibal3.speed(0)

	boat = turtle.Turtle()
	#boat.color("grey")
	boat.shape("E://Study//7th sem//AI//Graphics Downloads//boat.gif")
	boat.setpos(-50,-40)
	boat.penup()
	boat.speed(0)

	start = turtle.Turtle()
	#start.color("black")
	start.shape("E://Study//7th sem//AI//Graphics Downloads//start.gif")
	start.setpos(0,210)
	start.up()
	#start.speed(0)

	missionary1.showturtle()
	missionary2.showturtle()
	missionary3.showturtle()
	cannibal1.showturtle()
	cannibal2.showturtle()
	cannibal3.showturtle()
	boat.showturtle()


	def startGame(x,y):
	   start.hideturtle()
	   cannibal1.setpos(-20,-25)
	   cannibal2.setpos(-60,-25)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   cannibal1.forward(3)
		   cannibal2.forward(3)
	   cannibal1.setpos(430,-50)

	   while boat.position() >= (-50,-40):
		   boat.backward(3)
		   cannibal2.backward(3)

	   cannibal3.setpos(-20,-25)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   cannibal2.forward(3)
		   cannibal3.forward(3)
	   cannibal2.setpos(470,-50)

	   while boat.position() >= (-50,-40):
		   boat.backward(3)
		   cannibal3.backward(3)
	   cannibal3.setpos(-230,-50)

	   missionary1.setpos(-20,-10)
	   missionary2.setpos(-60,-10)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   missionary1.forward(3)
		   missionary2.forward(3)

	   missionary1.setpos(430,0)
	   cannibal1.setpos(380,-10)
	   while boat.position() >= (-50,-40):
		   boat.backward(3)
		   missionary2.backward(3)
		   cannibal1.backward(3)

	   cannibal1.setpos(-170,-50)
	   missionary3.setpos(-20,-10)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   missionary2.forward(3)
		   missionary3.forward(3)
	   missionary2.setpos(470,0)
	   missionary3.setpos(510,0)
	   cannibal2.setpos(370,-25)
	   while boat.position() >= (-50,-40):
		   boat.backward(3)
		   cannibal2.backward(3)
	   cannibal1.setpos(-60,-25)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   cannibal1.forward(3)
		   cannibal2.forward(3)
	   cannibal1.setpos(430,-50)
	   while boat.position() >= (-50,-40):
		   boat.backward(3)
		   cannibal2.backward(3)
	   cannibal3.setpos(-70,-25)
	   while boat.position() <= (350,-40):
		   boat.forward(3)
		   cannibal2.forward(3)
		   cannibal3.forward(3)
	   cannibal2.setpos(470,-50)
	   cannibal3.setpos(510,-50)
	   boat.showturtle()
	   turtle.write("BRAVO!!! Game Over", True, align="center",font=("Arial", 30, "normal"))
	   boat.showturtle()
	   missionary1.showturtle()
	   missionary2.showturtle()
	   missionary3.showturtle()
	   cannibal1.showturtle()
	   cannibal2.showturtle()
	   cannibal3.showturtle()


	start.onclick(startGame)


#if __name__ == "__main__":





if __name__ == '__main__':
	main()
	turtle.mainloop()

	# for i in range(1):
	# 	variable_name = input("Press any key to Exit")
		

delay = input("Press Enter to finish")
	
	
