import json


def calculate(val):
    data = json.load(open('data.json', 'r'))

    temp = []
    def calc_node(seed):
        # check if seed is already in data
            # if yes, return nodes + seed.children
            # if no
                # create node = seed * 3 + 1 if seed is odd
                # create node = seed / 2 if seed is even
                # add node to nodes
                # add node to data
                # return calc_node(node)
        if str(seed) in data:
            return temp + data[str(seed)]['children']
        node = seed // 2 if seed % 2 == 0 else seed * 3 + 1
        temp.append(node)
        return calc_node(node)
    
    return calc_node(val)


def write_file(nodes):
    data = json.load(open('data.json', 'r'))

    nodes.sort()
    new_data = {
        str(node): {
            'children': nodes[i + 1 :],
            'parent': 0 if i == 0 else nodes[i - 1],
            'numberOfChildren': len(nodes[i + 1 :]),
        }
        for i, node in enumerate(nodes)
    }
    data.update(new_data)
    keys = sorted(int(a) for a in data.keys())
    data = {key: data[str(key)] for key in keys}
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

def main():
    nodes = calculate(7)
    print(nodes)
    write_file(nodes)
    

    # merge new_data with data

if __name__ == '__main__':
    main()