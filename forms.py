### Forms application ###
'''
This program is to generate the dialog boxes
and buttons (as forms) to input the RS numbers, gene name
and chromosome coordinates 
'''

####### Dependencies #######
# Install flask_wtf from the command line: pip install flask-wtf

# Importing the appropriate packages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length

# Creating the forms

# Concepts: - Each box and button were created under the same class as only input from 1 is required
#			- The information given by the user has to be validated: no empty spaces, short rs values, etc.


# Creating a box for Gene name and rs values that receives a string 
class SNPForm(FlaskForm):
	gene = StringField('Gene Name', validators = [Length(min=2)],
		description='Input a gene name or gene ID')


	rs = StringField('rs ID', validators= [Length(min=2)],
		description='Input an rs value including "rs" and with no spaces')
	
#For the chromosome number selection , only chromosome 21 is used hence the choices list only has [21]
	chrom = SelectField('Chromosome', choices = [21], validators=[Length(min=1)])

#for The start and end coordinates that receives integers  
	start = IntegerField('Start Position',validators=[Length(min=1)])

	end = IntegerField('End Position',validators=[Length(min=1)])
	
#For Window size selection
	Window = IntegerField('Window Size',validators=[Length(min=1)])
	
#Submit button
	submit = SubmitField('Submit')
	
#For Checkboxes
	checkbox = BooleanField('Check')










