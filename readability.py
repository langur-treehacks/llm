import re
import math

def count_capitals(text):
    return sum(1 for char in text if char.isupper())

def lixCalculation(text):
    #replace ?,! with .
    #text = re.sub(r'[?!,]', '.', text)
    words=text.split()
    num_words = len(words)
    #count number of . : and capital letters
    num_periods= text.count('.')+ text.count(':')+ count_capitals(text)
    num_long_words = len([word for word in words if len(word) > 6])
    if num_periods==0:
        return 20
    if num_words==0:
        return 20
    return (num_words/num_periods) + (num_long_words * 100 / num_words)

def lix_score(text):
    """
    This function calculates the LIX score of a given text and returns a readability rating.
    :param text: The input text
    :return: The readability rating of the text, between 1 and 10
    """
    lix_score= lixCalculation(text)
    # print(lix_score)
    lix_score = max(6, min(60, lix_score))
    readability_rating = (lix_score / 6)
    return round(readability_rating,1)


if __name__=="__main__":
    easyText = "I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food! My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much."
    print(lix_score(easyText))
    medText="Keith recently came back from a trip to Chicago, Illinois. This midwestern metropolis is found along the shore of Lake Michigan. During his visit, Keith spent a lot of time exploring the city to visit important landmarks and monuments. Keith loves baseball, and he made sure to take a visit to Wrigley Field. Not only did he take a tour of this spectacular stadium, but he also got to watch a Chicago Cubs game. In the stadium, Keith and the other fans cheered for the Cubs. Keith was happy that the Cubs won with a score of 5-4. Chicago has many historic places to visit. Keith found the Chicago Water Tower impressive as it is one of the few remaining landmarks to have survived the Great Chicago Fire of 1871. Keith also took a walk through Jackson Park, a great outdoor space that hosted the World’s Fair of 1892. The park is great for a leisurely stroll, and it still features some of the original architecture and replicas of monuments that were featured in the World’s Fair. During the last part of his visit, Keith managed to climb the stairs inside of the Willis Tower, a 110-story skyscraper. Despite the challenge of climbing the many flights of stairs, Keith felt that reaching the top was worth the effort. From the rooftop, Keith received a gorgeous view of the city’s skyline with Lake Michigan in the background."
    print(lix_score(medText))
    hardText="The deadliest virus in modern history, perhaps of all time, was the 1918 Spanish Flu. It killed about 20 to 50 million people worldwide, perhaps more. The total death toll is unknown because medical records were not kept in many areas. The pandemic hit during World War I and devastated military troops. In the United States, for instance, more servicemen were killed from the flu than from the war itself. The Spanish flu was fatal to a higher proportion of young adults than most flu viruses. The pandemic started mildly, in the spring of 1918, but was followed by a much more severe wave in the fall of 1918. The war likely contributed to the devastating mortality numbers, as large outbreaks occurred in military forces living in close quarters. Poor nutrition and the unsanitary conditions of war camps had an effect. A third wave occurred in the winter and spring of 1919, and a fourth, smaller wave occurred in a few areas in spring 1920. Initial symptoms of the flu were typical: sore throat, headache, and fever. The flu often progressed rapidly to cause severe pneumonia and sometimes hemorrhage in the lungs and mucus membranes. A characteristic feature of severe cases of the Spanish Flu was heliotrope cyanosis, where the patient’s face turned blue from lack of oxygen in the cells. Death usually followed within hours or days. Modern medicine such as vaccines, antivirals, and antibiotics for secondary infections were not available at that time, so medical personnel couldn’t do much more than try to relieve symptoms. The flu ended when it had infected enough people that those who were susceptible had either died or developed immunity."
    print(lix_score(hardText))
    spanishEasyText="En mi casa, por ejemplo, cuando me lavo los dientes, cierro la llave para no desperdiciar el agua. También, cuando quiero lavar la ropa, lleno la lavadora de ropa completamente antes de usarla. Y también tengo un reloj en la ducha y así me ducho en cinco minutos. Máximo, cinco minutos."
    print(lix_score(spanishEasyText))
    spanishMediumText="En una granja de Kansas, mientras Dori se paseaba con su perrito Totó, un fuerte ciclón se los llevó por los aires hasta el país de Oz. La Bruja del Norte les dijo que sólo el Mago de Oz sabía el modo de regresar a su país. Por el camino, encontraron un espantapájaros que les quiso seguir. Más adelante, un leñador de hojalata les explicó que deseaba tener un corazón para amar y se unió a ellos para acompañarles. Algo después, un león cobarde les confesó que necesitaba tener valor para ser el rey de la selva y también se unió a ellos. Los cinco amigos siguieron el Camino Dorado en busca de la Ciudad Esmeralda, donde vivía el Mago. Al cabo de unos días de andar y pasar aventuras, divisaron a lo lejos el Castillo Esmeralda, de color verde. Cada uno expuso al Mago su deseo: volver a Kansas; tener cerebro en lugar de serrín ; un corazón para amar y valor para ser rey. -Con una condición: tenéis que matar a la Bruja del Oeste -que le estaba escuchando-. La malvada Bruja se abalanzó sobre nuestros amigos, pero tropezó con un pozal de agua, lo único que podía destruirla, y murió. Al instante se les apareció la buena Bruja del Sur que les concedió a cada uno lo que tanto deseaban. A Dori, además, le reveló un secreto: -Cuando salgas de la Ciudad Esmeralda, tienes quedar tres golpes con los tacones y volverás a tu país. Y así fue."
    print(lix_score(spanishMediumText))
    spanishHardText="Los abanicos, a lo largo de la historia y en las diversas regiones cálidas del planeta, han variado de tamaño, forma y materiales de fabricación. En el siglo XVI el abanico plegable llegó a Europa, pero donde más se extendió su empleo y fabricación fue en España, y desde allí, se difundió por las colonias americanas de climas cálidos. Una de las curiosidades que aportó la cultura hispana fue el lenguaje secreto del abanico, empleado para comunicar diferentes mensajes. Uno de estos es pasar el abanico por la mejilla, el cual significa «te amo»."
    print(lix_score(spanishHardText))