from django.shortcuts import render
from .models import Family, Member
from .member_form import SearchMemberForm
from django.views.generic import TemplateView

# class-based view
class SearchMemberView(TemplateView):
	form_class = SearchMemberForm
	template_name = 'family/search.html'

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})		
	def post(self,request):
		familyid = request.POST['Family_ID'] if request.POST['Family_ID'] else None
		lastname = request.POST['Last_Name'] 
		firstname = request.POST['First_Name'] 
		street = request.POST['Street']	
		city = request.POST['City']	
		homephone = request.POST['Home_Phone']	
		mobilephone = request.POST['Mobile']	

		form = self.form_class(request.POST)
		#Note that this search is based on members.. so if a family
		# does not have member, then it will not show.
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
									mem_sMobile__icontains = mobilephone,
									)
		
		return render(request, self.template_name, {'form': form, 'members': members})		