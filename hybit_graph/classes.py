class Node:
    id = ""
    edges_in = []
    edges_out = []

    def __init__(self, id):
        self.id = id
        self.edges_out = []
        self.edges_in = []

    def __repr__(self):
        return self.id

    def node_info(self):
        return '%s (%d in, %d out)' % (self.id, len(self.edges_in), len(self.edges_out))


class Edge:
    node_in = None
    node_out = None
    lbl_category = ""
    lbl_woher = ""
    lbl_was = ""
    lbl_wohin = ""

    def __init__(self, category, woher, was, wohin):
        self.lbl_category = category
        self.lbl_woher = woher
        self.lbl_was = was
        self.lbl_wohin = wohin

    def __repr__(self):
        return '%s - %s: %s' % (self.node_in.id, self.node_out.id, self.lbl_category)
