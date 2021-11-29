#Yaseen Nur
#ID:20101218
#Sec:09

#Task1
from LAB1 import palindrome


class Node:
    def __init__(self, intElement, refToNextNode):
      
        self.elem = intElement
        self.refNext = refToNextNode

class LinkedList:
  #Task2
  #Constructor
    def __init__(self, array):
      
        self.head = None #instance variable
        self.size=len(array)
          
        for i in range(0,len(array)):
          newNode=Node(array[i],None)
          
          if(self.head==None):
            self.head=newNode
            tail=newNode
            
          else:
            tail.refNext=newNode
            tail=newNode
    #2
    def showList(self):    
        
      node=self.head
      if self.head==None:
           print('Empty List')
           return
         
      else:
        while (node is not None):
          print(node.elem, end='->')
          node=node.refNext
        
    #3
    def isEmpty(self):
      
        if self.size==0:
          return True
        
        else:
          return False
    #4
    def clear(self):
      
        if self.isEmpty():
          print('List is empty')
          
        else:
          self.head.elem=0
          self.head.refNext=None
          self.size=0
          
    #Used to get a node based on 'index'   
    def get(self,index):
      
      count=0
      node=self.head
      
      while(node is not None):
        
        if (count==index):
          return node
        
        count+=1
        node=node.refNext
        
    #5 and 6      
    def insert(self, newElement, index = None):
      
      node=self.head
      
      #Checking validity of index
      if (index!=None):
        if (index<0 or index>self.size):
          print ('Invalid Index!')
          return 
      
      #Checking duplicates
      while(node is not None):
        if (newElement==node.elem):
          print(f'Element {newElement} already exists!')
          return
        else:
          node=node.refNext
      
      #Inserting element at given index
      
      newNode=Node(newElement,None)
      
      #1inserting element at tail(Task 5)
      if index==None:
        pred=self.get(self.size-1)
        newNode.refNext=pred.refNext
        pred.refNext=newNode
        self.size+=1
        
      #2inserting element at head  
      elif index==0:
        newNode.refNext=self.head
        self.head=newNode
        self.size+=1
      #3inserting element at any other position  
      else:
        pred=self.get(index-1)
        newNode.refNext=pred.refNext
        pred.refNext=newNode
        self.size+=1

    
    #7
    def remove(self,deleteElement):
      node=self.head
      deletedElement=None
      firstIndex=False
      exist=False
      
      #Deleting element head
      if firstIndex==False:
        if  node.elem==deleteElement:
          deletedElement=self.head.elem
          self.head=self.head.refNext
          self.size-=1
          print(deletedElement)
          return
        else:
          firstIndex=True
        
      #Deleting element at any other position
      if firstIndex==True:
        while(node.refNext!=None):
          
          if (node.refNext.elem==deleteElement):
            deletedElement=node.refNext.elem
            node.refNext=node.refNext.refNext
            self.size-=1
            print(deletedElement)
            return
            
          node=node.refNext    
      
      #If element does not exist   
      if exist==False:
        print(f'Element {deleteElement} does not exist!')    
            
          
    #Task3
    #1
    def evenList(self):
      node=self.head
      array=[]
      while(node is not None):
        if node.elem%2==0:
          array+=[node.elem]
          node=node.refNext
        else:
          node=node.refNext
          
      LinkedList(array).showList()
          
    #2
    def find(self, element):
        node=self.head
        while(node is not None):
          if node.elem==element:
            return True
          else:
           node=node.refNext
        return False
    
    #3  
    def reverseList(self):
      
      prev = None
      node = self.head
      while(node is not None):
        nextNode = node.refNext
        node.refNext = prev
        prev = node
        node = nextNode
      self.head = prev
      
                    
    #4
    def sort(self):
        for ind in range(0,self.size):
          node=self.head
          while(node is not None and node.refNext is not None):
            if node.elem>node.refNext.elem:
              (node.refNext.elem,node.elem)=(node.elem,node.refNext.elem)
              node=node.refNext   
            else:
              node=node.refNext    
                               
    #5
    def sum(self):
        node=self.head
        linkSum=0
        while(node is not None):
          linkSum+=node.elem
          node=node.refNext
        return linkSum          

    #6
    #rotates left once
    def rotateLeft(self):
      oldHead=self.head
      self.head=self.head.refNext
      tail=self.head
      while(tail.refNext is not None):
        tail=tail.refNext
      tail.refNext=oldHead
      oldHead.refNext=None
    
    #rotates right once
    def rotateRight(self):
      oldHead=self.head
      tail=self.head.refNext
      while(tail.refNext.refNext is not None):
        # print(tail.elem)
        tail=tail.refNext
      self.head=tail.refNext
      tail.refNext.refNext=oldHead
      tail.refNext=None
      
      def nodeAt(head, size, index):

        if(index<0 or index>=size):

            return None

        n = head

        for i in range(0,index):

            n = n.next


    def rotateKTimes(self, k, direction):
      
      if direction=='left':
        for i in range(k):
          self.rotateLeft()
          
      elif direction=='right':
        for i in range(k):
          self.rotateRight()
    
    def swapDelete(self):
      #swapping nodes
      oldHead=self.head
      tail=self.head.refNext
      while(tail.refNext.refNext is not None):
        tail=tail.refNext
      self.head=tail.refNext
      tail.refNext.refNext=oldHead.refNext
      tail.refNext=oldHead
      oldHead.refNext=None
      
      #counting nodes
      count = 1

      n = self.head

      while n is not None:

          count = count + 1

          n = n.refNext
      
      index=count//2+1+1
      
      counter=0
      node=self.head
      while(node is not None):
        if counter==index:
          break
        
         
    
#==========================Tester Code==========================#
        
#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
array = [10, 20, 30, 40, 50, 60]
l1 = LinkedList(array)
l1.showList() #Should print: 10->20->30->40->50->60
print('\n')

#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = LinkedList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true
print('\n')


#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List
print('\n')


#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
# c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# l3 = LinkedList(c)
# l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
# print('\n')
# l3.insert(100)
# l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
# print('\n')
# l3.insert(0, 0)
# l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
# print('\n')
# l3.insert(110, 5)
# l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
# print('\n')
# l3.insert(120, 12)
# l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
# print('\n')
# l3.insert(50) #Should print: Key 50 already exists
# print('\n')
# l3.insert(199,50) #Should print: Invalid Index
# print('\n')

# #Task-2.7 -- Remove
# print("\n//=======Task 2.7 -- Remove=======//")
# l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
# print('\n')
# l3.remove(0)
# l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
# print('\n')
# l3.remove(110) 
# l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100->120
# print('\n')
# l3.remove(120)
# l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
# print('\n')
# l3.remove(120) #Should print: Key 120 does not exist
# print('\n')


# #Task-2.8 -- EvenList
# print("\n//=======Task 2.8 -- EvenList =======//")
# d = [1, 2, 5, 3, 8]
# l4 = LinkedList(d)
# l4.evenList()#Should print: 2->8
# print('\n')


# #Task-2.9 -- Find
# print("\n//=======Task 2.9 -- Find =======//")
# found = l4.find(5)
# print(found) #Should print: true
# found = l4.find(4)
# print(found) #Should print: false
# print('\n')


# #Task-2.10 -- Reverse List
# print("\n//=======Task 2.10 -- Reverse =======//")
# print("Before Reverse: ", end='')
# l5=LinkedList([1,2,3,4,5])
# l5.showList() #Should print: 1->2->5->3->8
# l5.reverseList()
# print("After Reverse: ", end='')
# l5.showList()#Should print: 8->3->5->2->1
# print('\n')


# #Task-2.11 -- Sort
# print("\n//=======Task 2.11 -- Sort =======//")
# print("Before Sort: ", end='')
# l4.showList() #Should print: 8->3->5->2->1
# l4.sort()
# print("After Sort: ", end='')
# l4.showList() #Should print: 1->2->3->5->8
# print('\n')


# #Task-2.12 -- Sum of Elements
# print("\n//=======Task 2.12 -- Sum of Elements =======//")
# l4.showList() #Should print: 1->2->3->5->8
# total = l4.sum()
# print("Sum of Elements:", total)
# print('\n')


# #Task-2.13 -- Rotate
# print("\n//=======Task 2.13 -- Rotate =======//")
# l4.showList() #Should print: 1->2->3->5->8
# print('\n')
# l4.rotateKTimes(2, "left")
# l4.showList() #Should print: 3->5->8->1->2
# print('\n')
# l4.rotateKTimes(2, "right")
# l4.showList() #Should print: 1->2->3->5->8
# print('\n')
# c = [1,2,3,4,5]
l3 = LinkedList(c)
l3.showList()
print('\n')
l3.swapDelete()
# l3.rotateRight()
l3.showList()
print(5//2)