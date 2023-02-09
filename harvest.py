############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
#jgs
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller


    def add_pairing(self, pairing): 
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType(name = "Muskmelon", code = "musk", first_harvest = 1998, color = "green", is_seedless = True, is_bestseller = True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType(name = "Casaba", code = "cas", first_harvest = 2003, color = "orange", is_seedless = True, is_bestseller = None)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType(name = "Crenshaw", code = "cren", first_harvest = 1996, color = "green", is_seedless = True, is_bestseller = None)
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType(name = "Yellow Watermelon", code = "yw", first_harvest = 2013, color = "yellow", is_seedless = True, is_bestseller = True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in melon_types:
        melon_pairings = ', '.join(melon.pairings)
        print(f"{melon.name} pairs with {melon_pairings}")

    return None

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}
    for melon in melon_types:
        melon_dictionary[melon.code] = melon
    return melon_dictionary


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        # Fill in the rest
        # Needs __init__ and is_sellable methods
        self.shape_rating= shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

list_melons = make_melon_types()
print_pairing_info(list_melons)
melon_dictionary = make_melon_type_lookup(list_melons)
print (melon_dictionary)