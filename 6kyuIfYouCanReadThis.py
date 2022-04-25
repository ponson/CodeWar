NATO = { 'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
       'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',
       'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',
       'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',
       'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee',
       'Z':'Zulu'
      }


def to_nato_v1(words):
       result = ""
       for x in words:
              if x.isalnum() == True:
                     result = result + " " + NATO[x.upper()]
              elif x == ' ':
                     continue
              else:
                     result = result + " " + x

       return result.lstrip()


def to_nato(words):
    return " ".join(NATO.get(char, char) for char in words.upper() if char != " ")


print(to_nato("If you can read"))