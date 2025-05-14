# examples.py
# ==========================================================
import math, random, sys, copy, json
import re   #as regex  # Have to do this because re conflicts with sympy
#from decimal import Decimal

import sympy as sp

from pydantic import BaseModel

class ExamplePart(BaseModel):
  pid: int
  type: int  # 0 means input box, 1 means textarea
  question: str
  placeholder: str
  cans: str

class Example(BaseModel):
  qid: int
  rubric: str
  parts: list[ExamplePart]

class Examples(BaseModel):
  id: int
  ex: list[Example]

# ========================================================== 
def getExamples(inNum):
  #return ''  # Q&D fix because we are not showing examples for now
  examples = arithmetic_of_fractions()
  #print(30, examples)
  return formatExamples(examples)
  #return None
# ==========================================================
# The indexing is bq.database id . topic id . question num
# If the question has parts there will be an extra .question part
def formatExamples(inExamples, p=10):
  if p:
    print('e38', inExamples.id)
    for x in inExamples.ex:
      print('e39', x.qid, x.rubric)  #, x.qid, x.question)
      for xp in x.parts:
        print('e39', xp.pid, xp.question, xp.cans)
      print('')
  s = ''

  
  s += '<p>'
  s += '<button class=`btn btn-primary` type=`button` data-toggle=`collapse` data-target=`#collapseExample` aria-expanded=`false` aria-controls=`collapseExample`>'
  s += 'Button with data-target</button>'
  s += '</p>'
  '''
  s += '<div class=`collapse` id=`collapseExample`>'
  s += '<div class=`card card-body`>'
  s += 'Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.'
  s += '</div></div>'''
  

  if inExamples:
    s += '<div class=`collapse` id=`collapseExample`>'
    s += '<div class=`card card-body`>'
    s += '<table class=`table-fixed border-separate border-spacing-y-3`>'
    #n = 1
    for x in inExamples.ex:
      #x.question = x.question.replace('`', '"')
      if p: print('api6353', x.qid, x.rubric)

      if x.rubric:
        s += '<tr><td colspan=`4`>'
        s += str(x.qid) + '.&nbsp;' + x.rubric + '</td></tr>'

      for xp in x.parts:
        if p: print('\ne61', xp.question, '\n', xp.pid, xp.type, xp.placeholder, xp.cans)
        tmpid = str(inExamples.id) + '.' + str(x.qid) + '.' + str(xp.pid)

        s += '<tr><td class=`td70l`>'
        s += str(x.qid) + '.' + chr(xp.pid+97) + '&nbsp;</td>'  # 2.a, 2.b etc
        s += '<td colspan=`3`>' + xp.question + '</td></tr>'

        s += '<tr><td>&nbsp;</td>'
        if xp.type == 0:  # xp.type 0 means single-line answer ie <input>
          s += '<td class=`td400l`><input id=`baex' + tmpid  # baex => babbage example
          if x.qid == 1 and xp.pid == '1':
            s += '` placeholder=`' + xp.placeholder + '` autofocus></td>'
          else:
            s += '` placeholder=`' + xp.placeholder + '`></td>'
        elif xp.type == 1:  # xp.type:1 means multi-line answer ie <textarea>
          s += '<td><textarea id=`be' + tmpid + '` rows=`4` class=`ques-ta` '  # be => babbage example
          if x.qid == 1 and xp.pid == '1':
            s += '` placeholder=`' + xp.placeholder + '` autofocus></textarea></td>'
          else:
            s += '` placeholder=`' + xp.placeholder + '`></textarea></td>'
        
        #s += '<td id=`t' + tmpid + '` ' + 'class=`max-w-[3rem]`>blam</td></tr>'
        s += '<td><span id=`t' + tmpid + '`>&nbsp;</span></td>'  # For the tick/cross
        s += '<td><span style=`display:none` id=`c' + tmpid + '`>' + xp.cans + '</span></td></tr>'  # cans

        s += '<tr><td>&nbsp;</td><td colspan=`3`>'
        s += '<button type=`button` id=`babb'  + tmpid
        s += '` class=`btn btn-success border-dark`>Am I right?</button>'
        #s += '<button type=`button` class=`ques-bb`>Syntax</button>'
        #s += '<button type=`button` class=`ques-br`>Model Answer</button></td></tr>'
        #s += '</td></tr>'

        '''tmpid = str(x.id) + '.' + str(x.qid) + '.' + str(z['QID'])
        #print('api6387', tmpid)
        if qtype < 2:
          if n == 1 and z['QID'] == '0':
            s += '<input type=`text` name=`bq' + tmpid
            s += '` id=`bq' + tmpid + '` autofocus>'
          else:
            s += '<input type=`text` name=`bq' + tmpid
           s += '` id=`bq' + tmpid + '`>'

        elif qtype == 2:
          #print(6397, tmpid, n)
          s += ''  #get2x2MatrixRow(tmpid, n)

        elif qtype == 3:
          #print(6401, tmpid, n)
          s += ''  #get3x3MatrixRow(tmpid, n)'''

        s += '</td></tr><tr><td colspan=`4`>&nbsp;</td></tr>'
    s += '</table>'
    #n += 1

    #s += '<tr><td>&nbsp;</td><td colspan=`2`>'
    #s += '<button type=`text` id=`babb` class=`btn btn-success border-dark` '
    #s += 'style=`font-size: 30px;`>Am I right?</button>'
    #s += '</td></tr></table>'
    s += '</div></div>'
  #print('e122', s)
  return s
# ==========================================================
def mark_example(inSAns, inCans, p=10):
  r = ''
  gotSets = False
  if p: 
    print('\n\n==== mark_example Start =============================')
    print(inSAns)
  
  return 'ok'
  '''
  session['currentweek'] = getCurrentWeek()  # Refresh in case student doesn't log off

  # The input string is all the answers - single lines first
  # sortSAns breaks the input string into the answers for the separate questions
  sanz = sortSAns(inSAns)

  for san in sanz:
    s = '{`'
    for san1 in san:
      if len(san1) == 2:
        s += 'bq' + str(san1[0][0]) + '.'  + str(san1[0][1]) + '.'  + str(san1[0][2]) 
        s += '.'  + str(san1[0][3]) + '.'  + str(san1[0][4]) + '`:``:`'
        s += san1[1].strip() + '`,`'
    if len(s) > 3: s = s[0:-3] + '`}'
    if p: print(6439, s, san[0][0][0], san[0][0][2]) 

    ques = Examples.query.filter_by(id=san[0][0][0]).first()
    ques.sans = s
    if p: print(6443, 'cans =', ques.cans, ', sans =', ques.sans)
    tmp = parse.markAnswer(ques)
    
    r += tmp + ','
    if p: print(6447, tmp)
    if p: print('==========================================================\n')

  if r:
    if r[-1] == ',': r = r[0:-1]  # Strip trailing ,
  #print(6452, r)
  return r '''
# ========================================================== 
# decode examples and collect matrices into a single term
def decodeExamples(inFormData, p=0):
  lst = []

  if p: print('decodeExamples', inFormData)
  #  sans is an immutable dict ('sans', the answers)
  tmp = inFormData.getlist('sans')
  print(6462, tmp)
  sans = []
  if len(tmp) > 0:
    sans = tmp[0].split('`,`')
    if p: print(6466, sans)

  if sans:
    for san in sans:
      tmp2 = san.split('`:`')
      if p: print(6471, tmp2)
      if len(tmp2) == 2:
        tmp2[0] = tmp2[0].replace('`', '')
        #tmp2[0] = tmp2[0].replace('\t', '')
        if tmp2[0][0] == 'a': tmp2[0] = tmp2[0][1:]
        tmp2[1] = tmp2[1].replace('`', '')
        tmp2[1] = tmp2[1].replace('\t', '')
        #tmp2[1] = tmp2[1].replace('plus', '+')
        #tmp2[1] = tmp2[1].replace('equals', '=')
        #if p: print(6480, tmp42
        lst.append(tmp2)

  return lst
  if lst:
    tmp = []
    tmp1 = []
    index = -1
    for i, x in enumerate(lst):
      tmp2 = x[0].split('.')
      if len(tmp2) == 4:
        if tmp == []:
          tmp.append(x)
          tmp1 = tmp2[:]
          lst[i] = ''
          index = i

        else:
          added = 0
          if tmp1[0] == tmp2[0]:
            if tmp1[1] == tmp2[1]:
              if tmp1[2] == tmp2[2]:
                tmp.append(x)
                lst[i] = ''
                added = 1

          if added == 0:
            if index > -1:
              lst[index] = tmp
              tmp = [x]
              tmp1 = tmp2[:]
              lst[i] = ''
              index = i 

      else:
        if tmp:
          if index > -1:
            lst[index] = tmp
            tmp = []
            tmp1 = []
            index = -1

  #print(6522, lst, tmp)
  if tmp: 
    if index > -1:
      lst[index] = tmp

  tmp = []
  for x in lst:
    if x: tmp.append(x)
  #for x in tmp:
  #  print(6531, x)

  return tmp

# ==========================================================
def arithmetic_of_fractions() -> Examples:
  ems = Examples(id=random.randint(1, 1000), ex=[])
  ems.ex.append(fractions1(1))
  #ems.ex.append(fractions2(2))

  return ems
# ==========================================================
def fractions1(qid) -> Example:
  exm = Example(
    qid = qid,
    rubric = 'Without using a calculator express each of the following as a fraction in its simplest form. For example $3/21$ can be written as $1/7$',
    parts = []
  )
  p = [2, 3, 5, 7, 11]

  for i in range(6):
    random.shuffle(p)
    if p[2] < p[1]: p[1], p[2] = p[2], p[1]
    if i < 3:
      n = p[0]*p[1]
      d = p[0]*p[2]
    else:
      n = p[0]*p[1]*p[3]
      d = p[0]*p[2]*p[3]
    qt = 0              # question type
    ph = 'Your answer'  # placeholder

    #tmp = [str(n)+'/'+str(d), str(p[1])+'/'+str(p[2])]
    # cans='2:' means the answer has to be an identical string
    exm.parts.append(ExamplePart(pid=i, type=qt, question=str(n)+'/'+str(d), placeholder=ph, cans='2:'+str(p[1])+'/'+str(p[2])))

  return exm
# ==========================================================
def fractions2(qid) -> Example:
  exm = Example(
    qid = qid,
    rubric = 'Calculate',
    parts = []
  )
  p = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

  for i in range(6):
    random.shuffle(p)
    if p[1] < p[0]: p[0], p[1] = p[1], p[0]
    if p[3] < p[2]: p[2], p[3] = p[3], p[2]
    if p[5] < p[4]: p[4], p[5] = p[5], p[4]
    s = str(p[0]) + '/' + str(p[1])
    if random.random() < 0.5:
      s += '+' + str(p[2]) + '/' + str(p[3])
    else:
      s += '-' + str(p[2]) + '/' + str(p[3])

    if i > 2:
      if random.random() < 0.5:
        s += '+' + str(p[4]) + '/' + str(p[5])
      else:
        s += '-' + str(p[4]) + '/' + str(p[5])

    sp1 = sp.sympify(s)
    print(s, '=', sp1)

    qt = 0                # question type
    ph = 'Your answer'  # placeholder

    # cans='2:' means the answer has to be an identical string
    exm.parts.append(ExamplePart(pid=i, type=qt, question=s, placeholder=ph, cans='2:'+str(sp1)))
  
  return exm
# ==========================================================
'''
1-4: p[2] ÷ p[0]/p[1] = p[2]*p[1]/p[0]
5-9: p[2]/p[3] ÷ p[0]/p[1] = p[2]*p[1]/(p[0]*p[3])
'''
def fractions4() -> str:
  p = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

  for i in range(10):
    random.shuffle(p)
    if p[1] < p[0]: p[0], p[1] = p[1], p[0]
    s = str(p[0]) + '/' + str(p[1])
    if i < 5:
      s = str(p[2]) + '÷' + s  # ÷ is Alt+0247
      s1 = str(p[2]*p[1]) + '/' + str(p[0])

    else:
      s = str(p[2]) + '/' + str(p[3]) + '÷' + s
      s1 = str(p[2]*p[1]) + '/' + str(p[0]*p[3])

    sp1 = sp.sympify(s1)
    print(s, '=', sp1)

# ==========================================================
def fractions5() -> str:
  p = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

  for i in range(10):
    random.shuffle(p)
    if p[0] < p[1]: p[0], p[1] = p[1], p[0]
    s = str(p[0]) + '/' + str(p[1])
    n = int(p[0]/p[1])
    if p[0] == n*p[1]:
      p[0] += 1
      s = str(p[0]) + '/' + str(p[1])
    s1 = str(p[0]-n*p[1]) + '/' + str(p[1])
    sp1 = sp.sympify(s1)

    print(s, '=', n, sp1)

# ==========================================================
def fractions6() -> str:
  p = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

  for i in range(10):
    random.shuffle(p)
    if p[0] < p[1]: p[0], p[1] = p[1], p[0]
    s = str(p[2]) + ' ' + str(p[0]) + '/' + str(p[1])
    n = p[2]*p[1] + p[0]
    s1 = str(n) + '/' + str(p[1])
    sp1 = sp.sympify(s1)

    print(s, '=', sp1)

# ==========================================================
def indices1() -> str:
  c = ['a', 'b', 'c', 'd', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  s = ''
  for i in range(10):
    random.shuffle(c)
    random.shuffle(p)
    # × is Alt+0215
    if i < 6:
      s = c[0] + '^' + str(p[0]) + ' × ' + c[0] + '^' + str(p[1]) + ' × ' + c[0] + '^' + str(p[2])
    else:
      s = c[0] + '^' + str(p[0]) + ' ' + c[0] + '^' + str(p[1]) + ' ' + c[0] + '^' + str(p[2])

    s = s.replace('^1', '')
    s1 = c[0] + '^' + str(p[0]+p[1]+p[2])
    print(s, '=', s1)

# ==========================================================
def indices2() -> str:
  c = ['a', 'b', 'c', 'd', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  s = ''
  for i in range(10):
    random.shuffle(c)
    random.shuffle(p)
    # × is Alt+0215
    s = c[0] + '^' + str(p[0]) + ' / ' + c[0] + '^' + str(p[1])

    s = s.replace('^1', '')
    s1 = c[0] + '^' + str(p[0]-p[1])
    print(s, '=', s1)

# ==========================================================
def indices4() -> str:
  c = ['a', 'b', 'c', 'd', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  s = ''
  for i in range(10):
    random.shuffle(c)
    random.shuffle(p)
    # × is Alt+0215
    if i < 2:
      s = c[0] + '^-' + str(p[0]) + ' ' + c[0] + '^-' + str(p[1])
      s1 = '1/' + c[0] + '^' + str(p[0] + p[1])
    elif i < 5:
      s = c[0] + '^-' + str(p[0]) + ' / ' + c[0] + '^-' + str(p[1])
      if p[1] > p[0]:
        s1 = c[0] + '^' + str(p[1] - p[0])
      else:
        s1 = '1/' + c[0] + '^' + str(p[0] - p[1])
    elif i < 7:
      n1 = random.randint(2, 7)
      n2 = random.randint(2, 9)
      s = '(' + str(n1) + c[0] + '^' + str(p[0]) + ' ' + c[1] + '^' + str(p[1])
      s += ')(' + str(n2) + c[0] + '^-' + str(p[2]) + ' ' + c[1] + '^-' + str(p[3]) + ')'
      s1 = ''
    #else:


    s = s.replace('^1', '')
    s1 = c[0] + '^' + str(p[0]-p[1])
    print(s, '=', s1)

# ==========================================================
def brackets1() -> str:
  c = ['a', 'b', 'c', 'd', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  p = [2, 3, 4, 5, 6, 7, 8, 9]

  s = ''
  for i in range(10):
    random.shuffle(c)
    random.shuffle(p)
    # × is Alt+0215
    if i < 2:
      s = c[0] + '^-' + str(p[0]) + ' ' + c[0] + '^-' + str(p[1])
    elif i < 5:
      s = c[0] + '^-' + str(p[0]) + ' / ' + c[0] + '^-' + str(p[1])
    elif i < 7:
      s = c[0] + '^-' + str(p[0]) + ' / ' + c[0] + '^-' + str(p[1])
    else:
      s = c[0] + '^-' + str(p[0]) + ' / ' + c[0] + '^-' + str(p[1])
      

    s = s.replace('^1', '')
    s1 = c[0] + '^' + str(p[0]-p[1])
    print(s, '=', s1)

# ==========================================================



