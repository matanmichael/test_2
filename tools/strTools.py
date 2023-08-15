class StringComparator:
    def get_longer_string(self, str1, str2):
        if len(str1) > len(str2):
            return str1
        elif len(str2) > len(str1):
            return str2
        else:
            return "Both strings have the same length."
        
    def replace_symbols(self, input_str):
        modified_str = input_str.replace('$', ' ').replace('%', ' ')
        return modified_str

