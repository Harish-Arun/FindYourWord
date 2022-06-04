#AVL trees final
class NODE2:
  def __init__(self,length):
    self.val = length
    self.tree = None
    self.right= None
    self.left = None
    self.height=1

class NODE:
    def __init__(self,data,pos):
        self.val = data
        self.data=[data]
        self.right=None
        self.left=None
        self.pos = [pos]
        self.height=1

def get_height(node):
    if(node == None):
        return 0
    else:
        return node.height
        
def insert(root2, key ,pos):
    
    if not root2:
      return NODE(key,pos)
      
    elif(key == root2.val):
        root2.data.append(key)
        root2.pos.append(pos)      
    
    elif(key == root2.val):
        root2.data.append(key)
        root2.pos.append(pos)      
      
    elif key < root2.val:
      root2.left = insert(root2.left, key, pos)
      
    else:
      root2.right = insert(root2.right, key, pos)
    
    root2.height=1+max(get_height(root2.right), get_height(root2.left))
    
    balance=check_balance(root2)
    if balance > 1 and key < root2.left.val:
      return rightRotate(root2)
    
    if balance < -1 and key > root2.right.val:
      return leftRotate(root2)
    
    if balance > 1 and key > root2.left.val:
      root2.left = leftRotate(root2.left)
      return rightRotate(root2)
    
    if balance < -1 and key < root2.right.val:
      root2.right = rightRotate(root2.right)
      return leftRotate(root2)
    
    return root2

		
def check_balance(root):
	if not root:
		return 0    
	return (get_height(root.left) - get_height(root.right))
    
def rightRotate(root):
    new=root.left
    temp=new.right
    new.right=root
    root.left=temp
    
    root.height=1+max(get_height(root.right), get_height(root.left))
    new.height=1+max(get_height(new.right), get_height(new.left))
    
    return new

def leftRotate(root):
    new=root.right
    temp=new.left
    new.left=root
    root.right=temp
    
    root.height=1+max(get_height(root.right), get_height(root.left))
    new.height=1+max(get_height(new.right), get_height(new.left))
    
    return new

def insert2(root,key2,key,pos):
    
    if not root:
          
      root = NODE2((key))
      root.tree = insert(root.tree,key2,pos)
      return root
    
    elif((key) == root.val):
        root.tree = insert(root.tree, key2, pos)

        
    elif ((key) < root.val):
      root.left = insert2(root.left, (key2), key, pos)
      
    else:
      root.right = insert2(root.right, key2, key, pos)
    
    root.height=1+max(get_height(root.right), get_height(root.left))
    
    balance=check_balance(root)
    if balance > 1 and (key) < root.left.val:
      return rightRotate(root)
    
    if balance < -1 and (key) > root.right.val:
      return leftRotate(root)
    
    if balance > 1 and (key) > root.left.val:
      root.left = leftRotate(root.left)
      return rightRotate(root)
    
    if balance < -1 and (key) < root.right.val:
      root.right = rightRotate(root.right)
      return leftRotate(root)
    
    return root

def search(root,key):
     
    if root is None or root.val == key:
        
        return root
      
    if root.val < key:
        return search(root.right,key)
    elif root.val > key:  
        return search(root.left,key)
    else:
      return None

preorder_str=''
def preOrder(root):
    global preorder_str
    def preOrder2(root):
        global preorder_str
        if(root == None):
            return 0
        preorder_str+=str(root.val)
        preorder_str+='<br>'
        preOrder2(root.left)
        preOrder2(root.right)
        
    if(root == None):
        return 0
    preorder_str+='<br>'
    preorder_str+='<b>'
    preorder_str+=str(root.val)
    preorder_str+='</b>'
    preorder_str+='<br>'
    
    preOrder2(root.tree)
    preOrder(root.left)
    preOrder(root.right)

  
