class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.value = new_link 


class Stack:
    def __init__(self, top_item=None):
        self.top_item = top_item 
        self.size = 0 
        self.limit = 1000