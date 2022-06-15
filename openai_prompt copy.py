import openai
import nltk

def gpt3(stext):
  openai.api_key = "secret key"
  response = openai.Completion.create(engine="text-davinci-002",
                                      prompt=stext,
                                      temperature=0.9,
                                      max_tokens=2048)
  content = response.choices[0].text.split('.')
  #print(content)
  return response.choices[0].text

query = "Write long science fiction in Mary Shelley's style"
output = gpt3(query)

# Open a file with access mode 'w'
with open("unwritten.txt", "a") as file_object:
    # Append output at the end of file
    file_object.write("\n\nNEW STORY")
    file_object.write(output)
    file_object.close()


with open("unwritten.txt", "r") as file:
    data = file.read()
    number_of_characters = len(data)
    print('Number of characters in text file :', number_of_characters)

    nltk_tokens = nltk.word_tokenize(data)
    print("Number of Words: ", len(nltk_tokens))
    file.close()
print(output)
