from sympy import isprime

def trivia_fetch(num):
  diccionario = {
    "type": "trivia",
    "number": num,
    "es par?": num % 2 == 0,
    "es primo":isprime(num),
}
  return diccionario

def main():
  num = int(input("Ingresa un numero entero: "))
  print(trivia_fetch(num))
  
if __name__=="__main__":
  main()