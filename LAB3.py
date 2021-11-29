#LAb 03
#Yaseen Nur
#Sec:09
#ID:20101218
#=========== Task 01 =====================
class Node:

    def __init__(self,elem,prev,next):
        self.elem=elem
        self.next=None
        self.prev=None
        
        
class DoublyList:
    
    def __init__(self,array = None):
     
        self.head = Node('dummyHead',None,None)
        tail=self.head
            
        for i in range(0,len(array)):
          
          newNode=Node(array[i],None,None)
          
          tail.next=newNode
          newNode.prev=tail
          tail=newNode
        
        tail.next=self.head
        self.head.prev=tail
            
          
                    
#=========================== Task 02 ============================

    def showList(self):
        
        n=self.head.next
        
        if (n.elem==None):
            print("The list is empty")
            return
        
        while n is not self.head:
            print(n.elem,end=' ')
            n = n.next
            
#=============================================================
    def insertLast(self,newElement):
        
        new=Node(newElement,None,None)
        n=self.head.next
        
        #Duplicate Checker
        while n is not self.head:
            
            if (n.elem==newElement):
                print('Key Already Exists')
                return
            else:
                n=n.next
        #Insert at End
        tail=self.head.prev
        tail.next=new
        new.prev=tail
        new.next=self.head
        self.head.prev=new              
        # new.prev=self.head.prev
        # new.next=self.head
        # self.head.prev.next=new
        # self.head.prev=new
#=============================================================

  #Finds element from an index
    def elementFromInd(self,index):
      n=self.head.next
      ind=0
      while(ind!=index):
        n=n.next
        ind+=1
      return n
    
  #countNodes
    def countNodes(self):
      n=self.head.next
      size=0
      while n is not self.head:
        size+=1
        n=n.next
      return size 

    #USING INDEX
    def insertAt(self,newElement,index):
        n=self.head.next
        
        #SIZE CHECKER
        if index<0 or index>self.countNodes():
          print('Invalid Index')
          return
        #DUPLICATE CHECKER        
        while n is not self.head:
            
            if (n.elem==newElement):              
                print('Key Already Exists')
                return
            else:
                n=n.next
                
        newNode=Node(newElement,None,None)
        
        prevEl=self.elementFromInd(index).prev
        El=self.elementFromInd(index)
        newNode.next=El
        newNode.prev=prevEl
        prevEl.next=newNode
        El.prev=newNode
        
    #USING ELEMENT VALUE
    def insertBeforeValue(self,elementBF,elementIn):
      indexOFElement=self.IndexFromElement(elementBF)
      self.insertAt(elementIn,indexOFElement)
#=============================================================

    def deleteNode(self,index):
        n=self.head.next
            
        if index<0 or index>self.countNodes():
            print("wrong Index")
            
        else:
            El=self.elementFromInd(index)
            El.prev.next=El.next
            El.next.prev=El.prev
            El.next=El.prev=El.ele=None
            
#=============================================================

    def IndexFromElement(self,element):
      n=self.head.next
      ind=0
      
      while (n.elem!=element):
        n=n.next
        ind+=1
      return ind
    
    def removeElem(self,deletekey):
      deleteIndex=self.IndexFromElement(deletekey)
      self.deleteNode(deleteIndex)
      
      
        

                
l1=DoublyList([1,11,2,5,10,3])
print('\n',"ShowList")
l1.showList()
print('\n',"tailInsert")
l1.insertLast(6)
l1.showList()
print('\n',"Insert At any")
l1.insertAt(7,3)
l1.showList()
print('\n',"delete from index")
l1.deleteNode(2)
l1.showList()
print('\n',"Delete By Element")
l1.removeElem(7)
l1.showList()
print('\n',"Before element insertion")
l1.insertBeforeValue(10,9)
l1.showList()
