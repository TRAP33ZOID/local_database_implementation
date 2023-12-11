import openai

def num_tokens_from_text_file(file_path, model="gpt-3.5-turbo-1106"):
    # Read the file as plain text
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Assuming cl100k_base encoding is suitable for gpt-3.5-turbo-1106
    encoding = tiktoken.get_encoding("cl100k_base")

    # Count tokens
    num_tokens = len(encoding.encode(text))

    return num_tokens

# Example usage
file_path = 'C:\\Users\\Waleed\\Desktop\\work\\pdfs\\text\\TD.txt'
print(f"Number of tokens: {num_tokens_from_text_file(file_path)}")
