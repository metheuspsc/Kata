import itertools
import numpy
import math
from typing import List, Tuple


def count_distinct_characters(string: str) -> int:
    """ 
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    """

    stringset = set(string.lower())
    count = 0

    for char in stringset:
        count += 1

    return count


assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
    """
    notes = []

    for note in music_string.split(" "):
        if note == 'o':
            notes.append(4)
        elif note == 'o|':
            notes.append(2)
        elif note == '.|':
            notes.append(1)

    return notes


def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """

    return sum(string[i:].startswith(substring) for i in range(len(string)))


assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """

    words2num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    return " ".join(sorted(numbers.split(" "), key=words2num.get))


assert sort_numbers('three one five') == 'one three five'


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ 
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    lst = sorted(numbers)
    index = -1
    distance = max(lst) - min(lst)
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] < distance:
            distance = lst[i+1] - lst[i]
            index = i
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] == distance:
            return lst[i], lst[i+1]


assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """

    numbers.sort()

    output = []
    n = 0

    for number in numbers:
        output.append(n)
        n += 1/(len(numbers)-1)

    return output


assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [
    0.0, 0.25, 0.5, 0.75, 1.0]


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers"""

    output = []

    for value in values:
        if type(value) == int:
            output.append(value)

    return output


assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]


def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """

    for i in range(2, n):

        if n % i == 0:

            largest_divisor = i

    return largest_divisor


assert largest_divisor(15) == 5


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    output = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                output.append(i)
                break
    return output


assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input."""

    for number in numbers:
        if numbers.count(number) > 1:
            numbers = list(filter(lambda a: a != number, numbers))

    return numbers


assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]


def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase."""

    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)


assert flip_case('Hello') == 'hELLO'


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """

    output = ''
    for string in strings:
        output += string
    return output


assert concatenate([]) == ''
assert concatenate(['a', 'b', 'c']) == 'abc'


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    output = []

    for string in strings:
        if string[0] == prefix:
            output.append(string)
    return output


assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == [
    'abc', 'array']


def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    output = []
    for n in l:
        if n > 0:
            output.append(n)
    return output


assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
                    ) == [5, 3, 2, 3, 9, 123, 1]


def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
assert is_prime(6)
    False
assert is_prime(101)
    True
assert is_prime(11)
    True
assert is_prime(13441)
    True
assert is_prime(61)
    True
assert is_prime(4)
    False
assert is_prime(1)
    False
    """

    if n > 1:
        for num in range(2, n):
            if (n % num) == 0:
                return False
        return True
    else:
        return False


assert is_prime(6) == False
assert is_prime(101) == True
assert is_prime(11) == True
assert is_prime(13441) == True
assert is_prime(61) == True
assert is_prime(4) == False
assert is_prime(1) == False


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    >>> round(find_zero([-6, 11, -6, 1]), 2)
    1.0
    """

    return numpy.roots(xs[::-1])[-1]


assert round(find_zero([1, 2]), 2) == -0.5
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0


def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    return max(l)


assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123


def fizz_buzz(n: int):
    """This function:
    1.  Prints every number smaller than n that's divisible by 11 or 13.
    2.  Returns the number of times the digit 7 appears.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    sevens = 0

    for number in range(n):

        if (number) % 11 == 0 or (number) % 13 == 0:
            for n in str(number):
                if n == '7':
                    sevens += 1

    return sevens


assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3


def sort(l: list):
    l = list(l)
    l.sort()
    return l


def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indexes, while its values at the even indexes are equal
    to the values of the even indexes of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    output = []
    _l = sort(l)

    for num in _l:
        index = _l.index(num)
        if index > 0 and index % 2 != 0:
            output.append(l[index])
        else:
            output.append(_l[index])

    return output


assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]


def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    unique = set(l)

    result = [pair for pair in itertools.combinations(
        unique, 3) if sum(pair) == 0]

    print(result)

    if result:
        return True
    else:
        return False


assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == False
assert triples_sum_to_zero([1, 2, 3, 7]) == False


def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    output = []

    for n in l:
        output.append(n+1)
    return output


assert incr_list([1, 2, 3]) == [2, 3, 4]
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [
    6, 4, 6, 3, 4, 4, 10, 1, 124]


def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x//base, base) + convertString[x % base]


assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'


def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a*h)/2


assert triangle_area(5, 3) == 7.5


def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    a, b, c, d = 0, 0, 2, 0

    for i in range(n):

        a, b, c, d = b, c, d, a+b+c+d

    return a


assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14


def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


assert is_palindrome('') == True
assert is_palindrome('aba') == True
assert is_palindrome('aaaaa') == True
assert is_palindrome('zbcd') == False


def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """

    return (2 ** n) % p


assert modp(3, 5) == 3
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1


def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\\nghijklm")
    'bcdf\\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    output = ''

    for char in text:
        if not char in 'aeiou':
            output += (char)

    return output


assert remove_vowels('') == ''
assert remove_vowels("abcdef\\nghijklm") == 'bcdf\\nghjklm'
assert remove_vowels('abcdef') == 'bcdf'
assert remove_vowels('aaaaa') == ''
assert remove_vowels('zbcd') == 'zbcd'


def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    for n in l:
        if not n < t:
            return False
    return True


def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [xs[i]*i for i in range(1, len(xs))]

    def vowels_count(s):
    """Write a function smallLetterCount which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    """
    count = 0
    for char in s:
        if char in 'aeiou':
            count += 1

    return count


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    return str(x)[shift:] + str(x)[:shift]


def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    currentSum = 0

    # calculate sum of ascii values of each word
    for char in s:
        if char.isupper():
            currentSum += sum(map(ord, char))

    return currentSum


def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 + 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 + 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 + 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 + 1 = 19
    """

    non_mango = 0

    for char in s:
        if char.isnumeric():
            non_mango += int(char)

    return n - non_mango


def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1

    >>> search([4, 1, 2, 2, 3, 1])
    2

    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3

    >>> search([5, 5, 4, 4, 4])
    -1

    '''

    from collections import Counter

    output = -1
    counter = dict(Counter(lst))

    for n, c in counter.items():
        if n <= c:
            output = n

    return output


def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]

    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]

    strange_sort_list([]) == []

    >>> strange_sort_list([])
    []

    '''

    output = []

    while lst:
        output.append(min(lst))
        lst.pop(lst.index(min(lst)))
        output.append(max(lst))
        lst.pop(lst.index(max(lst)))

    return output

    def will_it_fly(q, w):
    '''
    Write a function that returns True if an object will fly, False otherwise.
    The object will fly if it's balanced and the sum of the weight is less than or equal the maximum possible weight w.

    Example:
    >>> will_it_fly([1, 2], 5)
    False

    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    >>> will_it_fly([3, 2, 3], 1)
    False

    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    >>> will_it_fly([3, 2, 3], 9)
    True

    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    >>> will_it_fly([3], 5)
    True

    # 3 is less than the maximum possible weight, and it's balanced.
    '''

    if q[0] == q[-1] and sum(q) < w:
        return True
    else:
        return False


def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.
    >>> smallest_change([1,2,3,5,4,7,9,6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """
    n = len(arr)

    cc = 0

    for i in range(n//2):

        if(arr[i] == arr[n-i-1]):
            continue

        cc += 1

        if(arr[i] < arr[n-i-1]):
            arr[n-i-1] = arr[i]
        else:
            arr[i] = arr[n-i-1]

    return cc


def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    >>> total_match([], [])
    []
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    >>> total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
    ['hI', 'hi', 'hi']
    >>> total_match(['4'], ['1', '2', '3', '4', '5'])
    ['4']
    '''

    char1 = sum(len(i) for i in lst1)
    char2 = sum(len(i) for i in lst2)

    if char1 == char2 or char1 < char2:
        return lst1
    elif char1 > char2:
        return lst2


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:

    >>> is_multiply_prime(30)
    True

    30 = 2 * 3 * 5
    """

    possible_primes = [2, 3, 5, 7, 11, 13]
    under_100 = []
    for l in product(possible_primes, repeat=3):
        multiple = reduce(lambda x, y: x*y, list(l))
        if multiple < 100:
            under_100.append(multiple)

    if a in set(under_100):
        return True

    return False


def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:

    >>> is_simple_power(1, 4)
    True
    >>> is_simple_power(2, 2)
    True
    >>> is_simple_power(8, 2)
    True
    >>> is_simple_power(3, 2)
    False
    >>> is_simple_power(3, 1)
    False
    >>> is_simple_power(5, 3)
    False
    """

    if (n == 1) or (x == 1):
        return (x == 1)

    pw = 1

    while (n ** pw < x):

        pw += 1

    return (n ** pw == x)


def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    >>> hex_key("AB")
    1
    >>> hex_key("1077E")
    2
    >>> hex_key("ABED1A33")
    4
    >>> hex_key("123456789ABCDEF0")
    6
    >>> hex_key("2020")
    2
    """

    return len([c for c in num if c in '2357BD'])


def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """

    return f'db{bin(decimal)[2:]}db'
