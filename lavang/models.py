from django.core.validators import RegexValidator
from django.db import models

CITY_LIST = ( ('Beaverton', 'Beaverton'), ('Portland','Portland' ), ('Vancouver', 'Vancouver'), )

STATE_ABBREV = (('OR', 'OR'),( 'WA','WA'), )

ELIGIBILITY_CHOICES = (
		('registered', 'Thuộc Giáo Xứ'),
		('unregistered', 'Không Thuộc Giáo Xứ'),
	)

MARITAL_CHOICES = (
		('unknown', 'Unknown'),
		('married', 'Lập Gia Ðình'),
		('single', 'Ðộc Thân'),	
		('serve', 'Ði Tu'),				
	)
MEMBER_ROLE_CHOICES = (
		('unknown', 'Unknown'),
		('head', 'Chủ Gia Ðình'),
		('grandparent', 'Ông Bà'),
		('husband', 'Chồng'),	
		('wife', 'Vợ'),				
		('child', 'Con'),				
		('grandchild', 'Cháu'),				
	)
GENDER_CHOICES = (('Male', 'Trai'), ( 'Female', 'Gái'),)

def FormatPhone(sPhone):
	if len(sPhone)==10:
		return "%s%s%s-%s%s%s-%s%s%s%s" % tuple(sPhone)
	else:
		return ''
	
# Create your models here.
class Church(models.Model):
	# Django creates a primary key automatically for each model
	chu_iChurchID = models.AutoField(primary_key=True, serialize=True) 
	chu_sName = models.CharField(max_length=80, blank=True, verbose_name='Name')
	chu_sStreet = models.CharField(max_length=80, blank=True, verbose_name='Street')
	chu_sCity = models.CharField(max_length=32, blank=True, verbose_name='City') 	
	chu_sState = models.CharField(max_length=2, choices=STATE_ABBREV, blank=True, verbose_name='State')
	chu_sPostalCode = models.CharField(max_length=10, blank=True, verbose_name='Zip')
	chu_sPhone = models.CharField(max_length=12, blank=True, verbose_name='Phone')   
	chu_sEmailAddress = models.CharField(max_length=50, blank=True, verbose_name='Email')  
	chu_sURLWebsite   = models.CharField(max_length=255, blank=True, verbose_name='Website')
	chu_sMissionStatement= models.CharField(max_length=255, blank=True, verbose_name='Mission Statement') 
	chu_sMemo  = models.CharField(max_length=255, blank=True, verbose_name='Memo')
	
	def __str__(self):              # __unicode__ on Python 2
		return self.chu_sName	
	class Meta:
		ordering = ('-chu_sName',)
		

class Family(models.Model):   
	fam_iFamilyID = models.AutoField(primary_key=True, serialize=True, verbose_name='Family #') 
	fam_iChurchID = models.ForeignKey(Church,related_name='+', verbose_name='Parish') 

	fam_sStreet = models.CharField(max_length=80, verbose_name='Street') 
	fam_sCity = models.CharField(max_length=32,choices=CITY_LIST,  verbose_name='City')     
	fam_sState = models.CharField(max_length=2, choices=STATE_ABBREV, verbose_name='State')
	fam_sPostalCode = models.CharField(max_length=10, verbose_name='Zip') 
	

	fam_sPhone = models.CharField(max_length=14,blank=True, verbose_name='Phone')

	fam_sFamilyEligibility = models.CharField(max_length=10,choices=ELIGIBILITY_CHOICES, default='registered',verbose_name='Eligibility')  

	# auto_now=True(set every time it's updated)
	# auto_now_add=True(set when it's created)
	fam_dtEntry = models.DateField(blank=True, auto_now_add=True, verbose_name='Entry Date') 
	# set null=True to allow null
	fam_dtExit = models.DateField(blank=True,null=True, verbose_name='Exit Date')
	fam_oPortrait = models.ImageField (upload_to='uploads/%Y/%m/%d/',blank=True, verbose_name='Portrait')  
	def __str__(self):              # __unicode__ on Python 2
		return str(self.fam_iFamilyID)
	def get_address(self):		
		return self.fam_sStreet + ' ' + self.fam_sCity + ' ' + self.fam_sState + ' ' +  self.fam_sPostalCode
	def Phone(self):
		return FormatPhone(self.fam_sPhone)
	
class Member(models.Model):
	#default manager
	objects = models.Manager()
	mem_iMemberID = models.AutoField(primary_key=True, serialize=True, verbose_name='Member #') 
	mem_iFamilyID = models.ForeignKey(Family,related_query_name='+', verbose_name='Family #')   
	mem_sChristianName = models.CharField(max_length=40,blank=True, verbose_name='Tên Thánh') 
	mem_sFirstName = models.CharField(max_length=20, verbose_name='Tên Gọi') 
	mem_sLastName = models.CharField(max_length=20, verbose_name='Tên Họ')  
	mem_sMiddleName= models.CharField(max_length=20,blank=True, verbose_name='Tên Đệm')        
	mem_sMemberRole =  models.CharField (max_length=20, choices=MEMBER_ROLE_CHOICES, default='unknown', verbose_name='Member Role')
	mem_dtDayOfBirth = models.DateField( verbose_name='Ngày Sanh') 
	mem_sCityOfBirth = models.CharField(max_length=32,blank=True, verbose_name='City of Birth')  
	mem_sCountryOfBirth = models.CharField(max_length=18,blank=True, verbose_name='Country of Birth')

	mem_sGender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male', verbose_name='Gender')        #         nchar(2) NULL,
	mem_sNationality = models.CharField(max_length=10,blank=True, verbose_name='Nationality')

	mem_sMartialStatusID = models.CharField (max_length=20, choices=MARITAL_CHOICES, default='unknown', verbose_name='Marital Status')

	# Member's Mobile phone
	mem_sMobile = models.CharField(max_length=14, blank=True, verbose_name='Mobile')

	# Member's email
	mem_sEmailAddress = models.EmailField(max_length=50, blank=True, verbose_name='Email')  
	
	mem_dtEntry = models.DateField(blank=True, auto_now_add=True, verbose_name='Entry Date') 
	mem_dtExit = models.DateField(blank=True, null=True, verbose_name='Exit Date') 
	mem_sMemo = models.CharField(max_length=255,blank=True, verbose_name='Memo')        
	mem_oPortrait = models.ImageField(upload_to='uploads/%Y/%m/%d/',blank=True, verbose_name='Portrait')  
	# return member name with Account Number(family id)
	def __str__(self):              # __unicode__ on Python 2
		return str(self.mem_iMemberID)
	def get_full_name(self):
		return self.mem_sFirstName + ' ' + self.mem_sLastName
	def Mobile(self):
		return FormatPhone(self.mem_sMobile)
