import statistics
import itertools

def distance(X, Y):
    return sum([(x-y)**2 for (x,y) in zip(X,Y)])

class kdNode:
    def __init__(self, value = [], dim = None, parent = None):
        self.value = value      # Indices of points located under this node
        self.dim = dim          # Dimension along which the splitting was done
        self.separator = None   # Point along self.dim where plitting plane crosses the axis
        self.parent = parent
        self.l = None
        self.r = None

class kdTree:
    def __init__(self):
        self.pts = []
        self.ndim = 0
        self.nsplits = 0
        self.root = kdNode([])
        pass

    def build(self, pts):
        self.ndim = len(pts[0])
        self.pts = pts
        self.root.value = list(range(len(self.pts)))
        self.root.dim = 0       # Start by splitting the first dimension
        self.split(self.root)   # Call recursive splitting function

    def split(self, node):
        if len(node.value) <= 1:
            return

        proj = [self.pts[i][node.dim] for i in node.value] # Projection onto splitting axis
        # If number of points is even, append Inf to make it uneven and always split across an existing point
        node.separator = statistics.median(proj if len(proj) % 2 else proj + [float('inf')])

        l_half = [node.value[i] for (i,v) in enumerate(proj) if v <  node.separator]
        r_half = [node.value[i] for (i,v) in enumerate(proj) if v >= node.separator]

        node.l = kdNode(l_half, dim = (node.dim+1) % self.ndim, parent = node)
        self.split(node.l)

        node.r = kdNode(r_half, dim = (node.dim+1) % self.ndim, parent = node)
        self.split(node.r)

    def find_leaf(self, pt, start=None):
        # Traverse the tree by choosing left or right to find the leaf
        # to which the point falls.
        if not start:
            start = self.root

        current_node = start
        while len(current_node.value) > 1: # While not in an empty node or a node with a single point
            if   pt[current_node.dim] > current_node.separator:
                current_node = current_node.r
            else:
                current_node = current_node.l
        return current_node

    def insert(self, pt):
        # Insert the new point to the leaf it falls in, split further.
        leaf = self.find_leaf(pt) # Find the leaf to which the new
                                  # point should be attached,
        self.pts.append(pt)       # attach it there,
        leaf.value.append(len(self.pts)-1)
        self.split(leaf)          # split the leaf.


    def remove(self, pt):
        # Remove a point from the tree.
        # Find the leaf in which the point dwells and delete it.
        pass

    def balance(self):
        # Rebalance the tree. 
        pass

    def nn_search(self, pt, start=None, nn=[], best_dist=float('inf')):
        ## Nearest neighbour search
        if start == None:
            start = self.root

        leaf = self.find_leaf(pt, start)
        if distance(self.pts[leaf.value[0]], pt) < best_dist:
            best_dist = distance(self.pts[leaf.value[0]], pt)
            nn = leaf.value[0]

        current_node = leaf
        while current_node != start:
            current_node = current_node.parent
            if abs(pt[current_node.dim] - current_node.separator) < best_dist:
                # There can be closer points on the other side
                if pt[current_node.dim] >= current_node.separator:
                    closest_cand, dist_cand = self.find_leaf(pt, current_node.l)
                else:
                    closest_cand, dist_cand = self.find_leaf(pt, current_node.r)

                if dist_cand < best_dist:
                    nn = closest_cand

        return nn, best_dist

if __name__ == '__main__':
    from itertools import combinations

    ndim = 3
    pts = list(itertools.product([-1,1], repeat=ndim))
    print(pts)
    tree = kdTree()
    tree.build(pts)
    tree.insert([2,2,2])
    tree.insert([0.8,-0.8,-0.8])
    print(tree.pts)
    print(tree.nn_search([-0.7,-0.7,-0.7]))
