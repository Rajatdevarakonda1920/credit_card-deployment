import joblib
chrun_model = joblib.load('credit_crd.pkl')

output = chrun_model.predict([[ 2.00e+04,  2.00e+00,  1.00e+00,  2.00e+00,  2.00e+00, -1.00e+00,
        -1.00e+00, -2.00e+00, -2.00e+00,  0.00e+00,  6.89e+02,  0.00e+00,
         0.00e+00,  0.00e+00,  0.00e+00]])
print(output)
if output[0] == 0:
	    print('not default')
	
else:
	    print('default') 