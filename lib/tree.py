self.root = root
def get_element_by_id(self, id):
    pass
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current

      nodes_to_visit = nodes_to_visit + current['children']
    return None
Footer
