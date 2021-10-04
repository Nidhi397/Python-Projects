from pywebio.input import *
from pywebio.output import *


def BMI_Calculator():
  height=input("Please Enter the Height in CM",type=FLOAT)
  weight=input("Please Enter the Weight in KG",type=FLOAT)
  bmi= weight/(height/100)**2
  bmi_output={16:'severely underweight',18.5:'Underweight',25:'Normal',30:'Overweight',35:'Moderately Obese',float('inf'):'Severely Obese'}
  for i in bmi_output:
    if bmi<=i:
      put_text('Your BMI is: %.1f and you are: %s'%(bmi,bmi_output[i]))
      break


if __name__=='__main__':
  BMI_Calculator()    
