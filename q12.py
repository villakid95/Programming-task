class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  
def in_order(tree):     
    current_node = tree     
    new_list = []           
    condition = False           

    while not condition:
        if current_node is not None:
            new_list.append(current_node)
            current_node = current_node.left 
        elif(len(new_list) >0):
             current_node = new_list.pop()
             print(current_node.value)          
             current_node = current_node.right
        else:
             condition = True       

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
