import random

# Default story elements
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

def add_custom_elements():
    """Add custom elements to the story categories."""
    print("\nAdd your own story elements or press Enter to skip.")
    
    custom_when = input("Add to 'when' (comma-separated): ").split(',')
    custom_who = input("Add to 'who' (comma-separated): ").split(',')
    custom_name = input("Add to 'name' (comma-separated): ").split(',')
    custom_residence = input("Add to 'residence' (comma-separated): ").split(',')
    custom_went = input("Add to 'went' (comma-separated): ").split(',')
    custom_happened = input("Add to 'happened' (comma-separated): ").split(',')
    
    # Extend the default lists with custom entries if provided
    global when, who, name, residence, went, happened
    when.extend([item.strip() for item in custom_when if item.strip()])
    who.extend([item.strip() for item in custom_who if item.strip()])
    name.extend([item.strip() for item in custom_name if item.strip()])
    residence.extend([item.strip() for item in custom_res
