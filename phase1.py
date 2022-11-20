from slist import SList
from slist import SNode #we imported this because is needed for function insertMiddle
import sys


class SList2(SList):

    def sumLastN(self, n):
        sum = 0
        if self.isEmpty(): #in this case we can't sum any elements, we establish the sum as 0
            return sum
        if n> len(self): #if n is greater than th lenght of the list, sum all of its elements
            n = len(self)
        if n<0: #in this case return None
            return None
        elif n<= len(self):
            counter = 0
            while counter<n:#for all of the last n elements
                elem = self.getAt(len(self)-1-counter) #update index to go backwards
                counter = counter + 1 #to travel throught the list
                sum = sum + elem #keep track of the sum
        return sum


    def insertMiddle(self, elem):
        # method for inserting a new node in the middle
        #we must study the parity of the list first to establish its middle point
        if (len(self) % 2 == 0): #even
            middle = len(self)//2
        else: #odd
            middle = (len(self)+1)//2

        #create a new node with element the value given as input
        middleNode = SNode(elem)

        if middle == 0:#if the list is empty, we must establish the new node as the list's head
            self._head = middleNode
        else:#if it's not the head, we'll just connect its previous node to the newnode
            prevmiddle = self._head
            for i in range(middle - 1): #travel through the list
                prevmiddle =prevmiddle.next

            #relate the previous node with the new one, and the new one to the one that was originally after the one named prevmiddle
            middleNode.next = prevmiddle.next
            prevmiddle.next = middleNode

        self._size += 1 #increase size by one

        return None

    def insertList(self, inputList, start, end):
        if start < 0 or start > end or end >= len(self):
            # invalid parameters
            return None
        else:
            # delete sequence
            delete = end - start + 1  # number of elements to be deleted
            while delete != 0: #loop to delete all the needed elements
                self.removeAt(start)
                delete -= 1

            index = start
            counter = 0
            while counter < len(inputList):  # go through inputList
                elem = inputList.getAt(counter)  # get elements from inputlist
                counter += 1 #to travel through the input list
                self.insertAt(index, elem)  # insert such element in our list
                index += 1 #to travel through the calling list



    def reverseK(self, k):
        "the function must invert the elements of the calling list in groups of k elements."
        if self.isEmpty(): #nothing can be reversed if list is empty
            return None
        if k <= 1: #if k<=1 no transformation is performed
            return None
        if k >= len(self): #if k>=len(self), entire list must be reversed
            k = len(self)

        # ceiling division. this will give us the number of groups there are
        if len(self)%k == 0: #instead of using functions as ceil, we created this algorithm to determine the number of groups there should be
            ngroup = len(self)/k #if it's a multiple of k
        else:
            ngroup = (len(self)+k-1)//k #if it's not a multiple of k


        start = 0 #starting index of the first group
        end = k - 1 #last index of first group

        while ngroup != 0: #repeat for all the groups
            next = 0 #we'll use this variable to change groups

            # we´ll use these variables to transverse through the group. We begin in the extremes of the group and end in the middle components
            index1 = start
            index2 = end

            while next == 0: #change groups

                elem = self.getAt(index1) #get the elements of the said positions
                elem2 = self.getAt(index2)
                self.removeAt(index1) #remove the element at the position
                self.insertAt(index1, elem2) #an insert the one located in position of index2
                self.removeAt(index2) #do the same with the oer extreme
                self.insertAt(index2, elem)
                index1 += 1 #increase index1 to keep travelling through the list
                if index1 == index2: #if the group is even sized then in the last pair after increasing by one the index1, both indexes should be the same
                    next = 1 #traversed the entire group. pass to the next group
                else:
                    index2 -= 1 #decrease index2 to continue reversing
                    if index2 == index1:
                        next = 1 #if we have reached the middle of an odd sized group, continue to next group

            ngroup -= 1 #to keep track of number of groups
            start += k #add k to the starting index
            end += k #decrease k to the last index
            if end >= len(self):
                end = len(self) - 1

        return None





    def maximumPair(self):
        #return maximum value of the sum of equidistant elements in a list
        if self.isEmpty(): #no max pair if list is empty
            return None
        count = 1 #number of the current iteration
        start = 0 #starting index
        maxPair = 0 #set the value maxPair to any number
        end = len(self) -1 #last index

        #depending on the parity of the length of the list, we should performed a number of iterations
        if len(self) % 2 == 0:
            its = len(self)//2
        else:
            its = (len(self)+1)//2

        while count <= its:#see how many iterations the program should go through depending on the size of the list
            if start == end: #in case we are in the middle point of an odd sized list, we should consider only the value of the element
                currsum = self.getAt(start)
            else:
                currsum = self.getAt(start) + self.getAt(end) #if we are not in that special case, consider the sum of both elements

            if (count == 1) or (currsum > maxPair): #if we are in the first iteration, set maxPair to the value of the first sum. if we reach a bigger sum in the next iterations, update maxPair
                maxPair = currsum

            #update indexes
            start += 1
            end -= 1
            count += 1 #increase the number of the current iteration

        return maxPair


