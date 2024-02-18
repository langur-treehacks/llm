from deep_translator import GoogleTranslator

# Use any translator you like, in this example GoogleTranslator
def deepTranslator(target,language):
    translated = GoogleTranslator(source='auto', target=language).translate(target) 
    return translated
if __name__=="__main__":
    print(deepTranslator("I like to play soccer","spanish"))