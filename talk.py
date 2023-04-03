import re
import random

class Valasz:
    def __init__(self,valaszok,kerdesek,single_response=False,requied_words=[]):
        self.valaszok = valaszok
        self.kerdesek = kerdesek
        self.single_response = single_response
        self.required_words = requied_words

v = []

def isbool(str):
    if str == 'False':
        return False
    elif str == 'True':
        return True

def openfile():
    v.clear()
    with open("be.txt", "r",encoding='utf8') as my_file:
        # a megnyitott fájlra my_file-ként hivatkozhatunk

        tartalom = my_file.readlines()
        for sor in tartalom:
            seged = re.split(r'\n',sor)[0]
            tabla = re.split(r';', seged)
            valasz = re.split(r'/',tabla[0])
            szavak = re.split(r',', tabla[1])
            single = isbool(tabla[2])
            kotelezo_szavak = []
            if(not single):
                kotelezo_szavak = re.split(r',', tabla[3])
            item = Valasz(valasz,szavak,single,kotelezo_szavak)
            v.append(item)

def additem(item):
    with open("be.txt","a",encoding='utf8') as my_file:
        my_file.write("\n"+item)





def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))


    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}


    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response,
                                                              required_words)

    for item in v:
        response(random.choice(item.valaszok), item.kerdesek, item.single_response, item.required_words)

    best_match = max(highest_prob_list, key=highest_prob_list.get)


    return "idk what that means" if highest_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response






if __name__ == '__main__':
    openfile()
    while True:
        print('Bot: ' + get_response(input('You: ')))



