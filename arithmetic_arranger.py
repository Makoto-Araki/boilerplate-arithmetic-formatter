'''
library imoport
'''

import re

''' (function)
maximum_characters(["32", "+", "8"]) => 2
'''

def maximum_characters(strings):
    if len(strings[0]) > len(strings[2]):
        return len(strings[0])
    else:
        return len(strings[2])

''' (function)
result_added(["32", "+", "8"]) => ["32", "+", "8", "40"]
'''

def result_added(strings):
    result = strings
    if strings[1] == '+':
        calculation = int(strings[0]) + int(strings[2])
    else:
        calculation = int(strings[0]) - int(strings[2])
    result.append(str(calculation))
    return result

''' (main function)
arithmetic_arranger(["32 + 8", "42 - 5"], True) =>
  32      42
+  8    -  5
----    ----
  40      37
'''

def arithmetic_arranger(*problems):
    
    '''
    Initialize return value
    '''
    
    arranged_problems = ''
    
    '''
    Too many problems
    '''
    
    if len(problems[0]) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    
    '''
    Operator must be + or -.
    '''
    
    for i in range(len(problems[0])):
        if '*' in problems[0][i] or '/' in problems[0][i]:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
    
    '''
    Numbers cannot be more than four digits.
    '''
    
    for i in range(len(problems[0])):
        temp = problems[0][i].split()
        if len(temp[0]) > 4 or len(temp[2]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems

    '''
    Numbers must only contain digits.
    '''
    
    pattern = re.compile(r'[^0-9]')
    for i in range(len(problems[0])):
        temp = problems[0][i].split()
        if pattern.search(temp[0]) or pattern.search(temp[2]):
          arranged_problems = 'Error: Numbers must only contain digits.'
          return arranged_problems
  
    '''
    problems[0] == [
      "32 + 8",
      "42 - 5",
    ]
    '''
    
    input = []
    for i in range(len(problems[0])):
        input.append(problems[0][i].split())
    
    '''
    input == [
      ["32", "+", "8"],
      ["42", "-", "5"],
    ]
    '''
    
    terms = []
    for i in range(len(input)):
        terms.append(result_added(input[i]))
    
    '''
    terms == [
      ["32", "+", "8", "40"],
      ["42", "-", "5", "37"],
    ]
    '''
    
    for i in range(len(terms)):
        maximum = maximum_characters(terms[i]) + 2
        terms[i].insert(3, '-' * maximum)
    
        '''
        terms == [
          ["32", "+", "8", "----", "40"],
          ["42", "-", "5", "----", "37"],
        ]
        '''
        
        for j in range(len(terms[i])):
            if j == 1: continue
            if j == 2: continue
            if j == 3: continue
            terms[i][j] = terms[i][j].rjust(maximum, ' ')
        
        ''' (blank == "_")
        terms == [
          ["__32", "+", "8", "----", "__40"],
          ["__42", "-", "5", "----", "__37"],
        ]
        '''
        
        backup1 = terms[i][1]
        backup2 = terms[i][2]
        blank = ' ' * (maximum - len(backup1) - len(backup2))
        del terms[i][1:3]
        terms[i].insert(1, backup1 + blank + backup2)
        
        ''' (blank == "_")
        terms == [
          ["__32", "+__8", "----", "__40"],
          ["__42", "-__5", "----", "__37"],
        ]
        '''
        
    result = [[], [], [], []]
    
    for i in range(len(terms)):
        for j in range(len(terms[i])):
            result[j].append(terms[i][j])
    
    ''' (blank == "_")
    result == [
      ["__32", "__42"],
      ["+__8", "-__5"],
      ["----", "----"],
      ["__37", "__37"],
    ]
    '''
    
    for i in range(len(result)):
        separater = ' ' * 4
        if len(problems) == 1:
            if i == 3: break
            arranged_problems += separater.join(result[i]) + '\n'
            
            '''
            arranged_problems == 
              "  32      42\n" +
              "+  8    -  5\n" +
              "----    ----\n" => Delete the trailing newline code
            '''
            
        else:
            arranged_problems += separater.join(result[i]) + '\n'
            
            '''
            arranged_problems == 
              "  32      42\n" +
              "+  8    -  5\n" +
              "----    ----\n" +
              "  37      37\n" => Delete the trailing newline code
            '''
    
    return arranged_problems[:-1]