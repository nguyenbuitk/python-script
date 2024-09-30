def highlight_differences_inline(a, b):
    result_a = []
    result_b = []
    
    # Loop through both strings, character by character
    for i in range(max(len(a), len(b))):
        char_a = a[i] if i < len(a) else ''
        char_b = b[i] if i < len(b) else ''
        
        if char_a != char_b:
            result_a.append(f'\033[91m{char_a}\033[0m' if char_a else ' ')  # Red for differences in 'a'
            result_b.append(f'\033[92m{char_b}\033[0m' if char_b else ' ')  # Green for differences in 'b'
        else:
            result_a.append(char_a)  # Unchanged text as is
            result_b.append(char_b)

    # Join and return the highlighted results
    highlighted_a = ''.join(result_a)
    highlighted_b = ''.join(result_b)
    
    return highlighted_a, highlighted_b

# Example usage
string1 = 'tackoverflow'
string2 = 'stackoverflow'

highlighted_a, highlighted_b = highlight_differences_inline(string1, string2)
print(f"Comparison between:\nString 1: {highlighted_a}\nString 2: {highlighted_b}")

string1 = 'The wall have an insulated layer for keep the house warm'
string2 = 'The walls have an insulated layer to keep the house warm'

highlighted_a, highlighted_b = highlight_differences_inline(string1, string2)
print(f"\nComparison between:\nString 1: {highlighted_a}\nString 2: {highlighted_b}")

