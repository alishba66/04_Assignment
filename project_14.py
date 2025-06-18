# 
import random

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}

    for i in range(len(words) - 1):
        curr_word = words[i]
        next_word = words[i + 1]

        if curr_word not in markov_chain:
            markov_chain[curr_word] = []
        markov_chain[curr_word].append(next_word)

    return markov_chain

def generate_text(chain, start_word, length=50):
    if start_word not in chain:
        start_word = random.choice(list(chain.keys()))

    word = start_word
    result = [word]

    for _ in range(length - 1):
        if word not in chain:
            break
        word = random.choice(chain[word])
        result.append(word)

    return ' '.join(result)

def main():
    # Sample training text (you can load from a file instead)
    sample_text = """ChatGPT is an AI developed by OpenAI. It can generate human-like responses. You can use it for code, writing, learning, or just chatting."""
    
    markov_chain = build_markov_chain(sample_text)

    start = input("Enter a start word (or press Enter for random): ").strip()
    text = generate_text(markov_chain, start if start else random.choice(list(markov_chain)), length=30)

    print("\n📝 Generated Text:\n")
    print(text)

if __name__ == "__main__":
    main()
