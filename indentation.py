‘’’
Most of the previous programming languages uses pair of curly braces { } to define a logical block. But Python uses indentation.
A logical block of code (such as, body of a function, loop, classes etc) starts with indentation and ends with the first and unintended line. The amount of indentation is up to you, but it must be consistent throughout that block. For ease of programming most of the programmers are prefers as single space or tab.
 ‘’’
Def test_function():
	f =1 
	for i in range(1,11):
	if i % 3 ==0 :
	continue
	print(i)
	print(“out of loop”)