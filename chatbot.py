import openai

openai.api_key = "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"

conversation = ""

i = 1
while (i != 0):
	question = input("PANGOZZA: ")
	conversation += "\nPANGOZZA: " + question + "\nDocenteVirtual:"
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=conversation,
		temperature=0.7,
		max_tokens=256,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0,
		stop=["\n", "PANGOZZA:", " DocenteVirtual:"]
		)

	anwer = response.choices[0].text.strip()
	conversation += anwer
	print("DocenteVirtual: " + anwer + "\n")