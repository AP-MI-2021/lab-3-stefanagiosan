def alternating_signs(l):
    '''
    determina daca toate numerele au semne alternante in lista
    :param l: lista formata din numere intregi
    :return: True daca lista este formata doar din numere cu semne alternante, sau false in caz contrar
    '''
    if l!=[]:
        if l[0]<0:
            ok=False
        else:
            ok=True
        for i in l[1:]:
            if ok==False and i<0:
                return False
            if ok==True and i>0:
                return False
            ok=not ok
        return True
    return True



def testAreAlternating():
    assert alternating_signs([-5,3]) is True
    assert alternating_signs([3, 4, -6]) is False
    assert alternating_signs([23,56]) is False
    assert alternating_signs([56,-78]) is True
    assert alternating_signs([9,100]) is False
    assert alternating_signs([]) is True

def get_longest_alternating_signs(l):
    '''
    determina cea mai lunga subsecventa formata din numere cu semne alternante
    :param l: lista cu elemente intregi
    :return: cea mai lunga subsecventa formata din numere cu semne alternante
    '''
    subsecventaMax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if alternating_signs(l[i:j + 1]) and len(subsecventaMax) < len(l[i:j + 1]):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([])==[]
    assert get_longest_alternating_signs([1,-2,3,-4,6,7])==[1,-2,3,-4,6]
    assert get_longest_alternating_signs([11,23,-4,5,-7,88,99,100]) == [23,-4,5,-7,88]


def isPrime(n):
    '''
    determina daca un numar este prim
    :param n: numarul intreg verificat
    :return: bool, True, daca x este prim sau False in caz contrar
    '''
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def testIsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True


def formatDinCifrePrime(n):
    '''
    verificam daca un numar contine doar cifre prime sau nu
    :param n: numarul intreg verificat
    :return: bool, True daca are doar cifre prime, iar False in caz contrar
    '''
    while n:
        if isPrime(n % 10) == False:
            return False
        n=n//10
    return True


def TestDoarCifrePrime():
    assert formatDinCifrePrime(223) == True
    assert formatDinCifrePrime(12345) == False
    assert formatDinCifrePrime(3) == True
    assert formatDinCifrePrime(273) == True


def listaCifrePrime(l):
    '''
    verifica daca toate numerele unei liste sunt formate din cifre prime
    :param l: lista verificata
    :return: returneaza True daca toate numerle au doar cifre prime, iar false in caz contrar
    '''
    for n in l:
        if formatDinCifrePrime(n) == False:
            return False
    return True


def get_longest_prime_digits(l):
    '''
    returneaza cea mai lunga secvemta in care numerele sunt formate doar din cifre prime
    :param l: lista din care se citesc numerele
    :return: subsecventa
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if listaCifrePrime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([34,56,78,333,2,55,89,106]) == [333,2,55]
    assert get_longest_prime_digits([2]) == [2]
    assert get_longest_prime_digits([1,56,78]) == []
    assert get_longest_prime_digits([12,45,67,23]) == [23]


def numerePrime(l):
    '''
    verifica daca toate numerele unei liste sunt formate din cifre prime
    :param l: lista verificata
    :return: returneaza True daca toate numerle au doar cifre prime, iar false in caz contrar
    '''
    for n in l:
        if isPrime(n) == False:
            return False
    return True


def get_longest_all_primes(l):
    '''
    returneaza cea mai lunga secvemta in care toate numerele sunt prime
    :param l: lista din care se citesc numerele
    :return: subsecventa
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if numerePrime(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_all_primes():
    assert get_longest_all_primes([11,2,3,7,8,9,6,5]) == [11,2,3,7]
    assert get_longest_all_primes([22,24,56,11,7,3,2]) == [11,7,3,2]
    assert get_longest_all_primes([34]) == []




def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de numere consecutive ce au semne alternate")
    print("3. Afisare cea mai lunga subsecventa de numere ce contin doar cifre prime")
    print("4. Afisare cea mai lunga subsecventa formata doar din numere prime")
    print("5. Iesire")


def citireLista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def main():
    TestDoarCifrePrime()
    test_get_longest_prime_digits()
    test_get_longest_all_primes()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_alternating_signs(l))
        elif optiune == "3":
            print(get_longest_prime_digits(l))
        elif optiune == "4":
            print(get_longest_all_primes(l))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")


if __name__=='__main__':
    main()
