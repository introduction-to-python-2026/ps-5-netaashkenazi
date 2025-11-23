


def split_before_each_uppercases(formula):
    start = 0 
    end = 0
    i = 0
    split_formula = []
    if not formula:
        return []
    for i in range(1,len(formula)):
      end = i
      if formula[i].isupper() : 
       split_formula.append(formula[start:end])
       start = end
    split_formula.append(formula[start:])
    return split_formula

def split_at_first_digit(formula):
   digit_location = 1
   new_formula = ()
   for char in formula[1:]:
      if char.isdigit():
          break
      digit_location += 1

   if digit_location == len(formula):
       return formula,1
   else :
      figure = int(formula[digit_location:])
      return formula[:digit_location],figure

   
       
def count_atoms_in_molecule(formula):
    atoms_count_dict = {}
    

    for atom in split_before_each_uppercases(formula):
        atom_name, atom_count = split_at_first_digit(atom)
        

        atoms_count_dict[atom_name] = atom_count

    return atoms_count_dict


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count

