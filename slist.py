# -*- coding: utf-8 -*-
"""
# Implementing a singly linked list

This notebook implements a singly linked list, which only saves the reference to the first node and the size of the list.
"""

class SNode:
  def __init__(self, e, next=None):
    self.elem = e          #1
    self.next = next        #1


class SList:
    """This is the implementation of a singly linked list. We only use 
    a reference to the first node, named head"""
    def __init__(self):
        """This constructor creates an empty list"""
        self._head=None
        self._size=0
    
    def __len__(self):
        """It returns the size of the list"""
        return self._size 


    def isEmpty(self):
        """"It returns True if the list is empty, and False eoc"""
        #return self._head == None
        return len(self)==0 

    def __str__(self):
        """Returns a string with the elements of the list"""
        result=''                                   

        nodeIt=self._head                           

        while nodeIt!=None: #nodeIt!=None           
            result+=str(nodeIt.elem)+", "            
            nodeIt=nodeIt.next                      
        
        if len(result)>0:
            result=result.strip()                           
            result=result[:-1]                       
        
        return "["+result+"]"                               
  

  

    def addFirst(self,e):
        """Add a new element, e, at the beginning of the list"""
        newNode=SNode(e)                                
        newNode.next=self._head                         
        self._head=newNode                              
        self._size+=1                                   
    
    def addLast(self,e):
        """This functions adds e to the end of the list"""
        newNode=SNode(e)

        if self.isEmpty():
            self._head=newNode
        else:
            #we move throught the list until to reach the last node
            lastNode=self._head
            while lastNode.next: #lastNode.next!=None
                lastNode=lastNode.next
            #now, lastNode is the last node
            #the last node must point to the new node (which will be the new last node)
            lastNode.next=newNode
        self._size+=1

        
    
      
    def removeFirst(self):
        """Removes the first element of the list"""
        result=None
        if self.isEmpty():
            print('Error: list is empty!')
        else:  
            #gets the first element, which we will return later
            result=self._head.elem
            #updates head to point to the new head (the next node)
            self._head=self._head.next
            self._size-=1
        
        return result
    


    def removeLast(self):
        """removes and returns the last node of the list. 
        If the list is empty, it prints an error and returns None"""
        result=None
        if self.isEmpty():
            print('Error: list is empty!')
        elif len(self)==1:
            result=self.removeFirst() #O(1)
        else:
            penult=None
            lastNode=self._head
            while lastNode.next:
                penult=lastNode
                lastNode=lastNode.next
            
            result=lastNode.elem
            penult.next=None

            self._size-=1
        
        return result
   
     

    def getAt(self,index):
        """return the element at the position index.
        If the index is an invalid position, the function
        will return -1"""
        result=None
        if index not in range(0,len(self)): 
            print(index,'Error getAt: index out of range')
        else:
            nodeIt=self._head
            i=0
            while nodeIt and i<index:
                nodeIt=nodeIt.next
                i+=1

            #nodeIt is at the position index
            result=nodeIt.elem

        return result

    def index(self,e):
        """returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        nodeIt=self._head
        index=0
        while nodeIt:
            if nodeIt.elem==e:
                return index
            nodeIt=nodeIt.next
            index+=1
            
        #print(e,' does not exist!!!')
        return -1 
      
    
    
    
    def insertAt(self,index,e):
        """This methods inserts a new node containing the element e at the index
        position in the list"""
        
        #first, we must check that index is a right position. 
        #Please, Note that index=len()+1 would be a right position
        #to insert a new element
        if index not in range(0,len(self)+1): 
            print(index, 'Error insertAt: index out of range')
        elif index==0:
            self.addFirst(e)
        elif index==len(self):
            self.addLast(e)
        else:
            #we need to reach the previous node (the node at the index-1 position)
            previous=self._head
            for i in range(index-1):
                previous=previous.next
                    
            #now, previous is the node with index-1
            #create the new node
            newNode=SNode(e)
            #newnode must point to the node after previous (which is previous.next)
            newNode.next = previous.next
            #previous must point with its next reference to the new node
            previous.next = newNode
            self._size+=1

      
    def removeAt(self,index):
        """This methods removes the node at the index position in the list"""
        result=None
        #We must check that index is a right position in the list
        #Remember that the indexes in a list can range from 0 to size-1
        if index not in range(len(self)): 
            print(index,'Error removeAt: index out of range')
        elif index==0:
            result= self.removeFirst()
        elif index==len(self)-1:
            result=self.removeLast()
        else:
            #we must to reach the node before the node at the index position
            previous=self._head
            for i in range(index-1):
                previous=previous.next
                
            #previous is the node at index -1 position
            #previous.next is the node at index position
            result=previous.next.elem
            previous.next = previous.next.next
            self._size-=1
        
        return result


