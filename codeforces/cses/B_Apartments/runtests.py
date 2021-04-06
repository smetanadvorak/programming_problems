import sys, os, filecmp, time

if len(sys.argv) > 1:
	scriptname = sys.argv[1]
else:
	scriptname = 'main.py'
	
inputext  = '.in'
refext = '.out'
resext = '.res'

### Get the names of the tests
testnames = os.listdir('./tests')

### Delete previous results
results = [instance for instance in testnames if instance.endswith(resext)]
for result in results:
	os.remove('./tests/'+result)

### Run the target program on a list of tests 
tests = [instance for instance in testnames if instance.endswith(inputext)]
print(tests)
for test in tests:
	print('Running test ' + test + '...', end="", flush=True)
	starttime = time.time()
	os.system('python' + ' ' + scriptname + ' ' + './tests/' + test)
	endtime = time.time()
		
	ref_file = './tests/' + test.split('.')[0] + refext
	res_file = './tests/' + test.split('.')[0] + resext
	if filecmp.cmp(ref_file, res_file):
		print('Correct Answer, Exec Time: %4.2f seconds' % (endtime-starttime))
	else:
		print('Wrong Answer, Exec Time: %4.2f seconds' % (endtime-starttime))
	
	