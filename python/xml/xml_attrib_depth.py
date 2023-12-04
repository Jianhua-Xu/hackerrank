import xml.etree.ElementTree as etree

# find the max depth of the xml file
def depth(elem):
    if len(elem) == 0:
        return 0
    else:
        return 1 + max([depth(child) for child in elem])

# get the total number of attirbutes from the xml
def score(node):
    return sum([score(child) for child in node]) + len(node.attrib)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    print(f"the depth of the xml file is {depth(tree.getroot())}")
    print(f"the total nubmer of attributes is {score(tree.getroot())}")