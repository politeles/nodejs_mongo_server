# coding=utf-8
from pymongo import MongoClient
import pprint
import re
import enchant
d = enchant.Dict('es_ES')

client = MongoClient('172.17.0.9', 27017)
db = client.users
collection = db.users


test1Answers = [
  {"number":15,"question":"","answers":6,"correctAnswer":2,"set":1},
  {"number":16,"question":"","answers":6,"correctAnswer":1,"set":1},
  {"number":17,"question":"","answers":8,"correctAnswer":8,"set":1},
  {"number":18,"question":"","answers":6,"correctAnswer":3,"set":1},
  {"number":19,"question":"","answers":8,"correctAnswer":7,"set":1},
  {"number":20,"question":"","answers":8,"correctAnswer":1,"set":2},
  {"number":21,"question":"","answers":8,"correctAnswer":4,"set":2},
  {"number":22,"question":"","answers":8,"correctAnswer":6,"set":2},
  {"number":23,"question":"","answers":8,"correctAnswer":5,"set":2},
  {"number":24,"question":"","answers":6,"correctAnswer":5,"set":2},
  {"number":25,"question":"","answers":8,"correctAnswer":1,"set":3},
  {"number":26,"question":"","answers":8,"correctAnswer":8,"set":3},
  {"number":27,"question":"","answers":8,"correctAnswer":4,"set":3},
  {"number":28,"question":"","answers":8,"correctAnswer":8,"set":3},
  {"number":29,"question":"","answers":8,"correctAnswer":3,"set":3},
  {"number":30,"question":"","answers":8,"correctAnswer":4,"set":4},
  {"number":31,"question":"","answers":8,"correctAnswer":2,"set":4},
  {"number":32,"question":"","answers":8,"correctAnswer":7,"set":4},
  {"number":33,"question":"","answers":8,"correctAnswer":7,"set":4},
  {"number":34,"question":"","answers":8,"correctAnswer":7,"set":4},
  {"number":35,"question":"","answers":8,"correctAnswer":3,"set":5},
  {"number":36,"question":"","answers":8,"correctAnswer":5,"set":5},
  {"number":37,"question":"","answers":8,"correctAnswer":3,"set":5},
  {"number":38,"question":"","answers":8,"correctAnswer":4,"set":5},
  {"number":39,"question":"","answers":8,"correctAnswer":1,"set":5},
  {"number":40,"question":"","answers":8,"correctAnswer":8,"set":6},
  {"number":41,"question":"","answers":8,"correctAnswer":1,"set":6},
  {"number":42,"question":"","answers":8,"correctAnswer":8,"set":6},
  {"number":43,"question":"","answers":8,"correctAnswer":2,"set":6},
  {"number":44,"question":"","answers":8,"correctAnswer":1,"set":6},
  {"number":45,"question":"","answers":8,"correctAnswer":2,"set":7},
  {"number":46,"question":"","answers":8,"correctAnswer":2,"set":7},
  {"number":47,"question":"","answers":8,"correctAnswer":1,"set":7},
  {"number":48,"question":"","answers":8,"correctAnswer":7,"set":7},
  ]

test4Answers = [
  {"number":0,"correctAnswer":"Asustado","answerSet":["Celoso","Asustado","Arrogante","Odio"]},
  {"number":1,"correctAnswer":"Entusiasmado","answerSet":["Entusiasmado","Reconfortante","Irritado","Aburrido"]},
  {"number":2,"correctAnswer":"Compungido","answerSet":["Aterrado","Compungido","Arrogante","Enojado"]},
  {"number":3,"correctAnswer":"Deseo","answerSet":["Bromista","Agitada","Deseo","Convencida"]},
  {"number":4,"correctAnswer":"Insistente","answerSet":["Bromista","Insistente","Entretenido","Relajado"]},
  {"number":5,"correctAnswer":"Preocupado","answerSet":["Irritado","Sarcástico","Preocupado","Simpático"]},
  {"number":6,"correctAnswer":"Fantasiosa","answerSet":["Horrorizada","Fantasiosa","Impaciente","Alarmada"]},
  {"number":7,"correctAnswer":"Intranquilo","answerSet":["Disculpante","Simpático","Intranquilo","Decaído"]},
  {"number":8,"correctAnswer":"Abatido","answerSet":["Abatido","Relajado","Tímido","Excitado"]},
  {"number":9,"correctAnswer":"Acongojada","answerSet":["Enojada","Hostil","Aterrorizada","Acongojada"]},
  {"number":10,"correctAnswer":"Prudente","answerSet":["Prudente","Insistente","Aburrido","Horrorizado"]},
  {"number":11,"correctAnswer":"Arrepentido","answerSet":["Aterrado","Entretenido","Arrepentido","Seductor"]},
  {"number":12,"correctAnswer":"Escéptico","answerSet":["Indiferente","Abochornado","Escéptico","Decaído"]},
  {"number":13,"correctAnswer":"Expectante","answerSet":["Contundente","Expectante","Amenazante","Severo"]},
  {"number":14,"correctAnswer":"Acusar","answerSet":["Irritado","Decepcionado","Deprimido","Acusar"]},
  {"number":15,"correctAnswer":"Pensativa","answerSet":["Pensativa","Agitada","Ilusionada","Entretenida"]},
  {"number":16,"correctAnswer":"Meditativo","answerSet":["Irritado","Meditativo","Ilusionado","Compasivo"]},
  {"number":17,"correctAnswer":"Insegura","answerSet":["Insegura","Afectuosa","Entusiasmada","Horrorizada"]},
  {"number":18,"correctAnswer":"Contundente","answerSet":["Contundente","Entretenida","Horrorizada","Aburrida"]},
  {"number":19,"correctAnswer":"Vacilante","answerSet":["Arrogante","Agradecida","Sarcástica","Vacilante"]},
  {"number":20,"correctAnswer":"Simpático","answerSet":["Imponente","Simpático","Culpable","Aterrorizado"]},
  {"number":21,"correctAnswer":"Fantasiosa","answerSet":["Abochornada","Fantasiosa","Confundida","Asustada"]},
  {"number":22,"correctAnswer":"Acongojada","answerSet":["Acongojada","Agradecida","Insistente","Suplicante"]},
  {"number":23,"correctAnswer":"Desafiante","answerSet":["Satisfecho","Disculpante","Desafiante","Curioso"]},
  {"number":24,"correctAnswer":"Caviloso","answerSet":["Caviloso","Irritado","Excitado","Hostil"]},
  {"number":25,"correctAnswer":"Interesada","answerSet":["Asustada","Incrédula","Abatida","Interesada"]},
  {"number":26,"correctAnswer":"Hostil","answerSet":["Alarmado","Tímido","Hostil","Ansioso"]},
  {"number":27,"correctAnswer":"Prudente","answerSet":["Bromista","Prudente","Arrogante","Tranquilizadora"]},
  {"number":28,"correctAnswer":"Interesada","answerSet":["Interesada","Bromista","Afectuosa","Satisfecha"]},
  {"number":29,"correctAnswer":"Reflexiva","answerSet":["Impaciente","Horrorizada","Irritada","Reflexiva"]},
  {"number":30,"correctAnswer":"Seductora","answerSet":["Agradecida","Seductora","Hostil","Decepcionada"]},
  {"number":31,"correctAnswer":"Segura","answerSet":["Avergonzada","Segura","Entusiasmada","Decaída"]},
  {"number":32,"correctAnswer":"Serio","answerSet":["Serio","Horrorizado","Aturdido","Alarmado"]},
  {"number":33,"correctAnswer":"Fantasioso","answerSet":["Abochornado","Culpable","Fantasioso","Inquieto"]},
  {"number":34,"correctAnswer":"Recelosa","answerSet":["Horrorizada","Desconcertada","Recelosa","Aterrada"]},
  {"number":35,"correctAnswer":"Nerviosa","answerSet":["Confusa","Nerviosa","Insistente","Pensativa"]},
  {"number":36,"correctAnswer":"Desconfiado","answerSet":["Avergonzado","Nervioso","Desconfiado","Indeciso"]},
  ];

test2Answers = [
  {"number":6,"question":"Por donde entra la luz","answers":"__NT_NA","correctAnswer":"VENTANA","set":1},
  {"number":7,"question":"Enredo","answers":"_IO","correctAnswer":"LIO","set":1},
  {"number":8,"question":"Vive en una zona muy fría","answers":"__Q__M_L","correctAnswer":"ESQUIMAL","set":1},
  {"number":9,"question":"Un pariente","answers":"_RI__","correctAnswer":"PRIMO","set":1},
  {"number":10,"question":"Anotar","answers":"E_C_I___","correctAnswer":"ESCRIBIR","set":1},
  {"number":11,"question":"Responder a un favor","answers":"__RA__CE_","correctAnswer":"AGRADECER","set":2},
  {"number":12,"question":"Relacionado con la investigación","answers":"_XP___M____","correctAnswer":"EXPERIMENTO","set":2},
  {"number":13,"question":"Afable, cariñoso o afectuoso","answers":"COR___L","correctAnswer":"CORDIAL","set":2},
  {"number":14,"question":"Excluir, no contar  con...","answers":"P_ES_I_D__","correctAnswer":"PRESCINDIR","set":2},
  {"number":15,"question":"Agradable, alegre","answers":"_I_P___CO","correctAnswer":"SIMPATICO","set":2},
  {"number":16,"question":"Dibujo con rasgos exagerados","answers":"_A_IC_T_R_","correctAnswer":"CARICATURA","set":3},
  {"number":17,"question":"Odio","answers":"_E_C_R","correctAnswer":"RENCOR","set":3},
  {"number":18,"question":"Un tipo de crimen","answers":"A_EN__D_","correctAnswer":"ATENTADO","set":3},
  {"number":19,"question":"Bastante","answers":"_U_I_I_N_E","correctAnswer":"SUFICIENTE","set":3},
  {"number":20,"question":"Capacidad o fuerza para actuar","answers":"_NE_G__","correctAnswer":"ENERGIA","set":3},
  {"number":21,"question":"Alto","answers":"_L_V___","correctAnswer":"ELEVADO","set":4},
  {"number":22,"question":"Desfavorecido de la suerte","answers":"__FO__U_A_O","correctAnswer":"INFORTUNADO","set":4},
  {"number":23,"question":"\"Pero, Doctor, realmente estoy enfermo; siempre me duele algo\"","answers":"_I_OCO__R_A_O","correctAnswer":"HIPOCONDRIACO","set":4},
  {"number":24,"question":"Obstaculizar","answers":"E__OR__R","correctAnswer":"ESTORBAR","set":4},
  {"number":25,"question":"Perseverante","answers":"C_N_T___E","correctAnswer":"CONSTANTE","set":4},
  {"number":26,"question":"Aceptar sin entusiasmo","answers":"_O_SE__I_","correctAnswer":"CONSENTIR","set":5},
  {"number":27,"question":"Charla","answers":"__N_E__A_I__","correctAnswer":"CONVERSACION","set":5},
  {"number":28,"question":"Necio o imprudente","answers":"__SE_S___","correctAnswer":"INSENSATO","set":5},
  {"number":29,"question":"Uno que destaca","answers":"__B_E_AL__N_E","correctAnswer":"SOBRESALIENTE","set":5},
  {"number":30,"question":"Corregir","answers":"_N_EN__R","correctAnswer":"ENMENDAR","set":6},
  {"number":31,"question":"Como algunas manchas o tintes","answers":"_ND__EB__","correctAnswer":"INDELEBLE","set":6},
  {"number":32,"question":"Con apariencia de verdadero","answers":"_E_O__M__","correctAnswer":"VEROSIMIL","set":6},
  {"number":33,"question":"Secreto y furtivo","answers":"C__ND_S___O","correctAnswer":"CLANDESTINO","set":6},
  {"number":34,"question":"Poderoso, arrogante","answers":"_R__O_E__E","correctAnswer":"PREPOTENTE","set":7},
  {"number":35,"question":"Establecer contacto","answers":"_O__C__R","correctAnswer":"CONECTAR","set":7},
  {"number":36,"question":"Algo oscuro o misterioso","answers":"_N_G__","correctAnswer":"ENIGMA","set":7},
  {"number":37,"question":"Apasionadamente aferrado a sus ideas","answers":"___A_I_O","correctAnswer":"FANATICO","set":7}
  ]

test3Answers = [
  {"number":31,"correctAnswer":"ANCLA","set":7},
  {"number":32,"correctAnswer":"ENCHUFE","set":7},
  {"number":33,"correctAnswer":"CALCULADORA","set":7},
  {"number":34,"correctAnswer":"ANZUELO","set":7},
  {"number":35,"correctAnswer":"SILLA MONTAR","set":7},
  {"number":36,"correctAnswer":"ESCALERA MECANICA","set":8},
  {"number":37,"correctAnswer":"EMBUDO","set":8},
  {"number":38,"correctAnswer":"COMPAS","set":8},
  {"number":39,"correctAnswer":"SALTAMONTES","set":8},
  {"number":40,"correctAnswer":"BALANZA","set":8},
  {"number":41,"correctAnswer":"MICROSCOPIO","set":9},
  {"number":42,"correctAnswer":"EXTINTOR","set":9},
  {"number":43,"correctAnswer":"HEXAGONO","set":9},
  {"number":44,"correctAnswer":"YUNQUE","set":9},
  {"number":45,"correctAnswer":"SALVAVIDAS","set":9},
  ]

def test1Correction(answers):
  index = 0
  itemsFailed = 0
  for answer in answers:
    if answer is not None:
      value = answer.lower().strip()
      if (ord('a')-ord(value)+1) != test1Answers[index-1]['correctAnswer']:
        itemsFailed += 1
  #    print("Answer: {}, Correct: {}").format(value,test1Answers[index-1]['correctAnswer'])
    index += 1
  print("Test 1: {}").format(test1Answers[index-1]['number']-itemsFailed)

def test4Correction(answers):
  index = 0
  correctAnswers = 0
  for answer in answers:
    #print("Answer {}, correct: {}").format(answer,test4Answers[index]['correctAnswer'])
    if answer is None:
      answer = ""
    if answer.lower().strip() == test4Answers[index]['correctAnswer'].lower().strip():
      correctAnswers += 1
    index += 1
  print("Test 4: {}").format(correctAnswers)
  #pp = pprint.PrettyPrinter()
  #pp.pprint(answers)
  return correctAnswers

def test2Correction(answers,correctAnswers):
  index = 0
  itemsFailed = 0
  for answer in answers:
    #spell check:
    try:
      if answer is None or answer == "" or not ((answer.lower().strip() == correctAnswers[index]['correctAnswer'].lower().strip()) or  d.check(answer.lower().strip())  or  correctAnswers[index]['correctAnswer'].lower().strip() in d.suggest(answer.lower().strip())):
        itemsFailed += 1
    except ValueError:
      itemsFailed += 1

    index += 1
  #  print("{} , {}, Correct? {}").format(answer,correctAnswers[index-1]['correctAnswer'].lower().strip(),correct)

  print("Test 2: {} = Item techo {} - fallos {}").format(correctAnswers[index-1]['number']-itemsFailed,correctAnswers[index-1]['number'],itemsFailed)

cursor = collection.find()
bad = set()
newAnswers = dict()

for user in cursor:
  v = False
  answers = user['answers']
  test1 = [None]*len(test1Answers)
  test2 = [None]*len(test2Answers)
  test3 = [None]*len(test3Answers)
  test4 = [None]*len(test4Answers)
  index = 0
  print("Evaluating user: {}").format(user['idUser'])
  for answer in answers:
    if user['idUser'] == 253:
      print("index: ").format(index)

#    print answer
    if answer['testNo'] == 1 and answer['answerNo'] < len(test1):
      test1[answer['answerNo']] = answer['answerValue']    
    elif (answer['testNo'] == 2):
      if answer['answerNo'] < len(test2Answers):
        test2[answer['answerNo']]= answer['answerValue']
    elif (answer['testNo'] == 3):
      if answer['answerNo'] < len(test3Answers):
        test3[answer['answerNo']]= answer['answerValue']
    elif (answer['testNo'] == 4):
      if answer['answerValue'] is None:
        test4[answer['answerNo']] = ""
      else:
        test4[answer['answerNo']]= answer['answerValue']
    index += 1
  print("user: {} test1: {} test2: {} test3: {} test4: {}").format(user['idUser'],len(test1),len(test2),len(test3),len(test4))
  test1Correction(test1)
  test2Correction(test2,test2Answers)
  test2Correction(test3,test3Answers)
  test4Correction(test4)
  if v:
    pp = pprint.PrettyPrinter()
    #pp.pprint(test2)
    print("id user: {}").format(user['idUser'])
    newAnswers[user['idUser']] = answers
    #pp.pprint(newAnswers[user['idUser']])
    #collection.update_one({'_id':user['_id']},{'$set':{'answers':answers}},upsert=False)


    

# find wrong responses:
#print("Bad users:")
#a = list(bad)
#a.sort()
#print("Total number of bad users: {}").format(len(a))
#for e in a:
#  print("user: {}").format(e)
#collection.update_one({'idUser':e})
#{answers: {$elemMatch:{testNo:1,answerValue: {$not : /answer*/}}}},{idUser:1}
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: {$not : /answer*/}}}},{$set:{"answers.$.testNo" :2}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer1'}}},{$set:{"answers.$.answerValue" :'a'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer2'}}},{$set:{"answers.$.answerValue" :'b'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer3'}}},{$set:{"answers.$.answerValue" :'c'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer4'}}},{$set:{"answers.$.answerValue" :'d'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer5'}}},{$set:{"answers.$.answerValue" :'e'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer6'}}},{$set:{"answers.$.answerValue" :'f'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer7'}}},{$set:{"answers.$.answerValue" :'g'}},{multi:true})
#db.users.update({answers: {$elemMatch:{testNo:1,answerValue: 'answer8'}}},{$set:{"answers.$.answerValue" :'h'}},{multi:true})
print("test {}").format(d.check("Balanza"))