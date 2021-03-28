#!/usr/bin/env python
# coding: utf-8

# # Singly_linked_list

# In[3]:


#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


# In[43]:


#creating_head
class LinkedList:
    def __init__(self):
        self.head=None
    
    #inserting in empty list
    def inserting_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked List is not empty")
            
            
    #insertin_at_begin 
    def inserting_bgn(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.ref=self.head
            self.head=new_node
     
    
    #inserting_at_end
    def inserting_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            n=n.ref
        n.ref=new_node
    
    #inserting a node after another data
    def inserting_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("data not in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
        
    #inserting befor another node
    def inserting_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        if x==self.head.data:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("data not in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
    #inserting specific position
    def inserting_spcf(self,data,index):
        if index==1:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        i=1
        n=self.head
        while i<index-1 and n is not None:
            n=n.ref
            i=i+1
        if n is None:
            print("data not in the list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    #count
    def count(self):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        count=0
        while n is not None:
            count=count+1
            n=n.ref
        return count
    
    #searching
    def search(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                print("item found")
                return True
            n=n.ref
        print("item not found")
        return False
        
            
        
    #traversing
    def traverse_LL(self):
        if self.head is None:
            print("Linked List is empty")
        n=self.head
        while n!=None:
            print(n.data)
            n=n.ref
    


# In[44]:


LL=LinkedList()


# In[45]:


LL.inserting_empty(10)
LL.traverse_LL()


# In[46]:


LL.inserting_bgn(40)
LL.inserting_bgn(50)
LL.inserting_bgn(60)
LL.traverse_LL()


# In[47]:


LL.inserting_end(20)
LL.inserting_end(70)
LL.inserting_end(30)
LL.traverse_LL()


# In[48]:


LL.inserting_after(80,30)
LL.traverse_LL()


# In[49]:


LL.inserting_before(90,10)
LL.traverse_LL()


# In[50]:


LL.inserting_spcf(110,3)
LL.inserting_spcf(120,5)
LL.traverse_LL()


# In[51]:


LL.count()


# In[52]:


LL.search(30)

