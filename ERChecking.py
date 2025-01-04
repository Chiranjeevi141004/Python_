def is_equivalence_relation(set_elements, relation):
    # Check Reflexivity
    for element in set_elements:
        if (element, element) not in relation:
            print("The relation is not reflexive.")
            return False

    # Check Symmetry
    for a, b in relation:
        if (b, a) not in relation:
            print("The relation is not symmetric.")
            return False

    # Check Transitivity
    for a, b in relation:
        for c, d in relation:
            if b == c and (a, d) not in relation:
                print("The relation is not transitive.")
                return False

    print("The relation is an equivalence relation.")
    return True

# Get user input for set elements
set_elements = set(map(int, input("Enter the set elements: ").split(',')))

# Get user input for relation
relation_input = input("Enter the pairs in the relation separated by parentheses (e.g., '(1,2) (2,1)'): ")
relation = set(eval(pair) for pair in relation_input.split())

# Check if the relation is an equivalence relation
if not is_equivalence_relation(set_elements, relation):
    print("The relation is not equivalence relation.")
