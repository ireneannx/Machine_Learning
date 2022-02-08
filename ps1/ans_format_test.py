## Multipe Choice Answer Format Test ##
#-- G. Wheeler, January 18, 2021

# Requires ans, a list .

possible_ans = ['A', 'B', 'C', 'D', 'E', 'F']
if type(ans) == list and all(ii in possible_ans for ii in ans):
    assert True
else:
    raise AssertionError("Inadmissible answer. Check that your answer to the question is a list and correctly formatted.")
