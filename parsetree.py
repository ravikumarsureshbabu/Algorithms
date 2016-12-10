

def print_text_in_tree(tree_unit,indent=""):
    print("%s%s" %(indent,tree_unit['text']))
    for each in tree_unit['kids']:
        print_text_in_tree(each, indent + " ")

data = {'count': 2,
        'text': '1',
        'kids': [{'count': 3,
                  'text': '1.1',
                  'kids': [{'count': 1,
                            'text': '1.1.1',
                            'kids': [{'count':0,
                                      'text': '1.1.1.1',
                                      'kids': []}]},
                           {'count': 0,
                            'text': '1.1.2',
                            'kids': []},
                           {'count': 0,
                            'text': '1.1.3',
                            'kids': []}]},
                 {'count': 0,
                  'text': '1.2',
                  'kids': []}]}

print_text_in_tree(data)
