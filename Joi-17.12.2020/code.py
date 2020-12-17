import json

x = input("User: ")

with open('chatbot.json') as json_file:
    data = json.load(json_file)
    #for p in data['chatbot']:
    #    print('Tag: ' + p['tag'])
    #    for i in p['patterns']:
    #        print("Patterns: " + i)
    #    for j in p['responses']:
    #        print("Responses: " + j)
    # print('\n')
    ok=0
    while ok==0:
        for p in data['chatbot']:
            for i in p['patterns']:
                if i==x:
                    for j in p['responses']:
                        print("Chatbot: "+ j)
                        ok=1
                        break
        if ok==0:
            x=input("Chatbot: Invalid answer. Enter again: ")



