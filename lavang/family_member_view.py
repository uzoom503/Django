from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse
import json
from django.views.generic import TemplateView
from .models import Family, Member
from .member_form import MemberGridForm,MemberDetailForm, FamilyForm


##########################################################################
# New Family
##########################################################################
class NewFamilyView(TemplateView):
	template_name = 'family/family_new.html'

	def get(self, request):
		return render(request, self.template_name, {'FamilyForm': FamilyForm})
		
	# Create new family
	def post(self, request):
		print(request.POST)
		response_data = {}
		
		form = FamilyForm(request.POST)
		if form.is_valid():
			print('is valid')
			new_family = form.save(commit=True)    
			return redirect('/family/edit/%d/' % new_family.fam_iFamilyID)
		else:
			return HttpResponse("form is not valid! %s "  % form.errors.as_json())

		
##########################################################################
# Update existing Family
##########################################################################
class EditFamilyView(TemplateView):
	template_name = 'family/family_member.html'

	def get(self, request,**kwargs):
		record = get_object_or_404(Family, fam_iFamilyID=kwargs['id'])
		famform = FamilyForm(instance=record)
		
		# Get member(s)
		mem_records = Member.objects.filter(mem_iFamilyID=kwargs['id'])	
		memforms = [];
		
		# build member form for each members
		for mem_record in mem_records:
			memform = MemberGridForm(instance=mem_record)
			memforms.append(memform)
		return render(request, self.template_name, {'FamilyForm': famform, 'MemberForms': memforms})
	                   
	# Save existing family
	def post(self, request,**kwargs):
		print(request.POST)
		record = get_object_or_404(Family, fam_iFamilyID=kwargs['id'])		
		response_data = {}
		
		# the file upload is in the request.FILES
		form = FamilyForm(request.POST, instance=record, files=request.FILES)
		if form.is_valid():
			print('Valid Form')
			family = form.save(commit=True)    
			response_data['result'] = 'Create successful!'
			response_data['FamilyID'] = family.fam_iFamilyID
		else:
			response_data['result'] = json.dumps(form.errors)
		#return HttpResponse(json.dumps(response_data),content_type="application/json")
		return redirect('/family/edit/%d/' % family.fam_iFamilyID)
        


##########################################################################
# Update existing Member
##########################################################################
class EditMemberView(TemplateView):
	template_name = 'family/member.html'

	def get(self, request,**kwargs):
		record = get_object_or_404(Member, mem_iMemberID=kwargs['id'])
		memform = MemberDetailForm(instance=record)
		memform.fields['mem_iFamilyID'].widget.attrs['readonly'] = True
		return render(request, self.template_name, { 'MemberForm': memform})
		
	def post(self, request,**kwargs):
		record = get_object_or_404(Member, mem_iMemberID=kwargs['id'])
		print(request.POST)
		response_data = {}
		
		# instance prevent creating new record
		form = MemberDetailForm(request.POST, instance=record, files=request.FILES)
		if form.is_valid():
			exist_member = form.save(commit=True)    
			return redirect('/member/edit/%d/' % exist_member.mem_iMemberID)
		else:	
			return HttpResponse("form is not valid! %s "  % form.errors.as_json())

##########################################################################
# New Member
##########################################################################
class NewMemberView(TemplateView):
	template_name = 'family/member.html'

	def get(self, request,**kwargs):
		# initialize family id
		form = MemberDetailForm(initial={'mem_iFamilyID':kwargs['famid'] })
		return render(request, self.template_name, {'MemberForm': form})
	
	# Create new member
	def post(self, request,**kwargs):
		#print(request.POST)
				
		form = MemberDetailForm(request.POST, files=request.FILES)
		if form.is_valid():
			print('is valid')
			new_member = form.save(commit=True)    
			return redirect('/member/edit/%d/' % new_member.mem_iMemberID)
		else:
			return HttpResponse("form is not valid! %s "  % form.errors.as_json())
