from django.shortcuts import render
from .models import Family, Member
from .search_form import SearchMemberForm
# Create your views here.

def MemberView(request):

	if request.method == 'POST':
		familyid = request.POST['Family_ID'] if request.POST['Family_ID'] else None
		lastname = request.POST['Last_Name'] 
		firstname = request.POST['First_Name'] 
		street = request.POST['Street']	
		city = request.POST['City']	
		homephone = request.POST['Home_Phone']	
		mobilephone = request.POST['Mobile']	
		
		# populate initial value
		form = SearchMemberForm(initial={'Family_ID': familyid, 'Last_Name': lastname, 'First_Name' : firstname, 'Street': street, 'City': city, 'Home_Phone': homephone, 'Mobile': mobilephone})
		# note the foreign key mem_iFamilyID which then reference to Family's fields
		if familyid:
			members = Member.objects.filter(mem_iFamilyID=familyid)
		else:
			members = Member.objects.all()	
		# if filter value is empty then it becomes '%'
		members = members.filter(mem_sLastName__icontains=lastname,
									mem_sFirstName__icontains=firstname,
									mem_iFamilyID__fam_sStreet__icontains = street,
									mem_iFamilyID__fam_sCity__icontains = city,				
									mem_iFamilyID__fam_sPhone__icontains = homephone,
									mem_iFamilyID__fam_sMobile__icontains = mobilephone,
									)
		
		return render(request, 'family/search_form.html', {'form': form, 'members': members})		
	else:
		form = SearchMemberForm()
		# request, template, context
		# Don't need the "templates" folder specified
		return render(request, 'family/search_form.html', {'form': form})