class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    # make stack
    visit = [self]
    # callback on root value
    cb(self.value)
    # while visit has a value
    while visit:
      # current value = first element in visit stack and is removed
      current = visit.pop(0)
      if current.left:
        # if current.left exists then callback on left.value
        cb(current.left.value)
        # current.left node is added to stack
        visit.append(current.left)
      if current.right:
        # if current.right exists then callback on right.value
        cb(current.right.value)
        # current.right node is added to stack
        visit.append(current.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
