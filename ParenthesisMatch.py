'''
Given a set of parenthesis, check if they match properly
can validate only () [] {}
'''


strParenthesis = '(){}[]'

dict = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def MatchParenthesis(input: str) -> bool:
    for i in range(0, len(input) - 1):
            pass


print(MatchParenthesis(strParenthesis))
