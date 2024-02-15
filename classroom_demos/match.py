def match_case_demo(value):
    match value:
        case 'apple':
            return "You chose an apple."
        case 'banana':
            return "You chose a banana."
        case 'orange':
            return "You chose an orange."
        case _:
            return "Unknown fruit."

# Example usage
print(match_case_demo('banana'))
