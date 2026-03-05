# Declare a Newspaper class. 

# Each Newspaper will have a 'pages' attribute set to an integer 
# and a 'sections' attribute set to a dictionary.
# The keys in 'sections' will be strings representing a section (i.e. "Politics") 
# and the values will be the starting page for that section (i.e. "A5").

class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections

    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        return self.sections[index]

    def __eq__(self, other):
        return self.pages == other.pages and len(self.sections) == len(other.sections)

# The length of a newspaper should be equal to the number of pages it holds.

# Indexing the newspaper by a section should return the starting page for that section.

# Make it so two newspapers are considered equal if they have the 
# same number of pages AND the same number of sections

# EXAMPLE:
monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False -- np1 has 3 sections while np2 has 2 sections
print(np1 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"