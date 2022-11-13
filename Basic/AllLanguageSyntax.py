('NOTE: This Program only contains the syntaxs , they cant be exicuted in python promt ')

print('''1.BASIC\

2.C++
3.C#
4.F#
5.GOOGLE GO
6.RUBY
7.JAVA
8.JAVASCRIPT
9.c
''')




BASIC=('''10 PRINT 'HELLO WORLD !' \
20 END''')
C=('''#include <stdioh.h>\
int main (void)
{
printf{'HELLO WORLD !'}
}''')
C_PLUS_PLUS=('''#include <iostream>\
int main ()
{
std::cout<<
('HELLO WORLD ');
return 0;''')
c_hash=('''using system;\
class program
{
static void
main(string[]args)
  {
  console.writeline(''HELLO WORLD !'');
  }
}''')
F_hash=('''open system\
console.writeline('HELLO WORLD !')''')
GOOGLE_GO=('''package main\
import 'fmt' func main()
{
fmt.println('HELLO WORLD !')
}''')
RUBY=("printl"+'"'+'HELLO WORLD !'+'"')
JAVA=('''class HELLO WORLD app <\
public static void
main(string[]args)
system.out.println('HELLO WORLD !');''')
JAVASCRIPT=('console.log','('+'"'+'hello world !'+'"',')')
MATLAB=('''class function\
methods function
greet(this)
disp(SOORY !)
    end
  end
 end)''')
x='yes'

while x=='yes':
    a=str(input('choose a language : '))
    s=a.upper()
    if s=='BASIC':
        print(BASIC)
    elif s=='C':
        print(C)
    elif s=='C_PLUS_PLUS':
        print('C_PLUS_PLUS')
    elif s=='C_#':
        print(C_hash)
    elif s=='F_#':
        print(F_hash)
    elif s=='GOOGLE_GO':
        print(GOOGLE_GO)
    elif s=='RUBY':
        print(RUBY)
    elif s=='JAVA':
        print(JAVA)
    elif s=='JAVASCRIPT':
        print(JAVASCRIPT)
    elif s=='POULAMI':
        print(MATLAB)
    x=str(input('Do you want to continue?(yes or no)'))
    if x=='no':
        break
p=str(input('for bonus language type your name ☺☺ :'))
g=p.upper()
if g!='hjhjhj':
    print(MATLAB)
