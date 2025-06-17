while True:
    prompt += "Enter 'quit' when finished."
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"{city.title()}!")