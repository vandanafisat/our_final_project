# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms
import datetime
from models import Approval,Source
import xlrd
import io
import xlwt
from xlsxwriter.workbook import Workbook
from xlrd.sheet import ctype_text

# Create your views here.
from django.http import HttpResponse


class UploadFileForm(forms.Form):
    file = forms.FileField()

class ManifiestosForm(forms.Form):
    a = forms.CharField()
    b = forms.CharField()
    c = forms.CharField()
    d = forms.CharField()
    e = forms.CharField()
    f = forms.CharField()
    g = forms.CharField()
    h = forms.CharField()
    i = forms.CharField()
    j = forms.DateTimeField()
    k = forms.CharField()
    l = forms.CharField()

class ManifiestosForm1(forms.Form):
    A = forms.CharField()
    B = forms.DateTimeField()
    C = forms.CharField()
    D = forms.CharField()
    E = forms.CharField()
    F = forms.CharField()
    G = forms.CharField()
    H = forms.CharField()
    I = forms.CharField()
    J = forms.CharField()
    K = forms.CharField()
    L = forms.CharField()
    M = forms.DateTimeField()
    N = forms.CharField()
    O = forms.CharField()
    P = forms.EmailField()
    Q = forms.CharField()
    R = forms.CharField()
    S = forms.CharField()
    T = forms.CharField()
    U = forms.CharField()
    V = forms.CharField()
    W = forms.CharField()
    X = forms.CharField()
    sou_id = forms.CharField()


class SearchForm(forms.Form):
    hid = forms.CharField()

class DeleteForm(forms.Form):
    del_id = forms.CharField()


class additionalForm(forms.Form):
    Aa = forms.CharField()
    Bb = forms.CharField()
    Cc = forms.CharField()
    Dd = forms.CharField()
    Ee = forms.DateTimeField()
    sou_id1 = forms.CharField()

# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        form1 = ManifiestosForm(request.POST)
        form2 = ManifiestosForm1(request.POST)
        if form1.is_valid():
            approval = Approval(RGS_ID=request.POST.get('a'), RGS_status=request.POST.get('b'), role=request.POST.get('c'),rqd_skset = request.POST.get('d'),
                tot_exp = request.POST.get('e'),
                branch = request.POST.get('f'),
                IOU = request.POST.get('g'),
                req_IOU = request.POST.get('h'),
                cust_name = request.POST.get('i'),
                ass_date = request.POST.get('j'),
                req_branch = request.POST.get('k'),
                staff_branch = request.POST.get('l'))
            approval.save()

        if form2.is_valid():
            source = Source(RGS_ID= Approval.objects.get(RGS_ID=request.POST.get('A')),
                DOT=request.POST.get('B'),
                branch=request.POST.get('C'),
                who_sourced_name= request.POST.get('D'),
                who_sourced_eno= request.POST.get('E'),
                cand_name= request.POST.get('F'),
                epno  = request.POST.get('G'),
                source_dtls= request.POST.get('H'),
                main_skills = request.POST.get('I'),
                ISU_name =  request.POST.get('J'),
                customer_name  = request.POST.get('K'),
                weekend_weekday = request.POST.get('L'),
                dt_of_interview = request.POST.get('M'),
                status = request.POST.get('N'),
                contact_number = request.POST.get('O'),
                email_id =  request.POST.get('P'),
                tot_yrs_exp =request.POST.get('Q'),
                R_exp =request.POST.get('R'),
                current_org = request.POST.get('S'),
                current_loc = request.POST.get('T'),
                pref_loc = request.POST.get('U'),
                current_ctc = request.POST.get('V'),
                exp_ctc = request.POST.get('W'),
                notice_period = request.POST.get('X'))
            source.save()

        if form.is_valid():
            filehandle = request.FILES['file']


            workbook = xlrd.open_workbook(filename=None, file_contents=filehandle.read())
            worksheet = workbook.sheet_by_index(0)

            row_count = worksheet.nrows

            if worksheet.cell(0, 1).value =='RGS ID Status':
                for x in xrange(1,row_count):
                  # Get cell object by row, col
                    approval=Approval(RGS_ID=worksheet.cell(x, 0).value, RGS_status=worksheet.cell(x, 1).value, role=worksheet.cell(x, 2).value,rqd_skset = worksheet.cell(x, 3).value,
                        tot_exp = worksheet.cell(x, 4).value,
                        branch = worksheet.cell(x, 5).value,
                        IOU = worksheet.cell(x, 6).value,
                        req_IOU = worksheet.cell(x, 7).value,
                        cust_name = worksheet.cell(x, 8).value,
                        ass_date = datetime.datetime(*xlrd.xldate_as_tuple(worksheet.cell(x, 9).value, workbook.datemode)),
                        req_branch = worksheet.cell(x, 10).value,
                        staff_branch = worksheet.cell(x, 11).value)

                    approval.save()
               # do what you have to do
                
            else:
                for x in xrange(1,row_count):
                    source=Source(RGS_ID= Approval.objects.get(RGS_ID=worksheet.cell(x, 0).value),
                        DOT=datetime.datetime(*xlrd.xldate_as_tuple(worksheet.cell(x, 1).value, workbook.datemode)),
                        branch=worksheet.cell(x, 2).value,
                        who_sourced_name= worksheet.cell(x, 3).value,
                        who_sourced_eno= worksheet.cell(x, 4).value,
                        cand_name= worksheet.cell(x, 5).value,
                        epno  = worksheet.cell(x, 6).value,
                        source_dtls= worksheet.cell(x, 7).value,
                        main_skills = worksheet.cell(x, 8).value,
                        ISU_name =  worksheet.cell(x, 9).value,
                        customer_name  = worksheet.cell(x, 10).value,
                        weekend_weekday = worksheet.cell(x, 11).value,
                        dt_of_interview = datetime.datetime(*xlrd.xldate_as_tuple(worksheet.cell(x, 12).value, workbook.datemode)),
                        status = worksheet.cell(x, 13).value,
                        contact_number = worksheet.cell(x, 14).value,
                        email_id =  worksheet.cell(x, 15).value,
                        tot_yrs_exp = worksheet.cell(x, 16).value,
                        R_exp = worksheet.cell(x, 17).value,
                        current_org = worksheet.cell(x, 18).value,
                        current_loc = worksheet.cell(x, 19).value,
                        pref_loc = worksheet.cell(x, 20).value,
                        current_ctc = worksheet.cell(x, 21).value,
                        exp_ctc = worksheet.cell(x, 22).value,
                        notice_period = worksheet.cell(x, 23).value)
                    
                    source.save()  
        appr = Approval.objects.all()
        sou = Source.objects.all()
        return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'form1':form1,
            'form2':form2,
            'approvals': appr,
    
            'sources': sou})

    elif request.method == "GET":
        form = UploadFileForm(request.POST, request.FILES)
        form1 = ManifiestosForm(request.POST)
        form2 = ManifiestosForm1(request.POST)
        delete_id = request.GET.get('del_id')
        Approval.objects.filter(RGS_ID=delete_id).delete()
        appr = Approval.objects.all()
        sou = Source.objects.all()
        return render(
            request,
            'upload_form.html',
            {
            'form': form,
            'form1':form1,
            'form2':form2,
            'approvals': appr,
            'sources': sou
            })

    else:
        form = UploadFileForm()
        form1 = ManifiestosForm()
        form2 = ManifiestosForm1()


    appr = Approval.objects.all()
    sou = Source.objects.all()
    return render(
        request,
        'upload_form.html',
        {
            'form1':form1,
            'form': form,
            'form2':form2,
            'approvals': appr,
            'sources':sou,
        })


def applicant(request):
    if request.method == "POST":
        form2 = ManifiestosForm1(request.POST)
        form3 = additionalForm(request.POST)
        search_query=request.GET.get('hid', '')
        source1 = Source.objects.filter(RGS_ID=search_query)
        approval1 = Approval.objects.get(RGS_ID=search_query)

        form4 = DeleteForm(request.POST)

        if form4.is_valid():
            delete_id = request.POST.get('del_id')
            Source.objects.filter(id=delete_id).delete()
            source1 = Source.objects.filter(RGS_ID=search_query)
            approval1 = Approval.objects.get(RGS_ID=search_query)
            return render(
                request,
                'applicants.html',
                {
                'form2':form2,
                'sources':source1,
                'search_query':search_query,
                'approvals':approval1
                })

        if form2.is_valid():
            search_id=request.POST.get('sou_id')
            if(search_id!='hello'):
                s = Source.objects.get(id=search_id)
                s.DOT=request.POST.get('B')
                s.branch=request.POST.get('C')
                s.who_sourced_name= request.POST.get('D')
                s.who_sourced_eno= request.POST.get('E')
                s.cand_name= request.POST.get('F')
                s.epno  = request.POST.get('G')
                s.source_dtls= request.POST.get('H')
                s.main_skills = request.POST.get('I')
                s.ISU_name =  request.POST.get('J')
                s.customer_name  = request.POST.get('K')
                s.weekend_weekday = request.POST.get('L')
                s.dt_of_interview = request.POST.get('M')
                s.status = request.POST.get('N')
                s.contact_number = request.POST.get('O')
                s.email_id =  request.POST.get('P')
                s.tot_yrs_exp =request.POST.get('Q')
                s.R_exp =request.POST.get('R')
                s.current_org = request.POST.get('S')
                s.current_loc = request.POST.get('T')
                s.pref_loc = request.POST.get('U')
                s.current_ctc = request.POST.get('V')
                s.exp_ctc = request.POST.get('W')
                s.notice_period = request.POST.get('X')
                s.save()
            
            else:
                source = Source(RGS_ID= Approval.objects.get(RGS_ID=request.POST.get('A')),
                    DOT=request.POST.get('B'),
                    branch=request.POST.get('C'),
                    who_sourced_name= request.POST.get('D'),
                    who_sourced_eno= request.POST.get('E'),
                    cand_name= request.POST.get('F'),
                    epno  = request.POST.get('G'),
                    source_dtls= request.POST.get('H'),
                    main_skills = request.POST.get('I'),
                    ISU_name =  request.POST.get('J'),
                    customer_name  = request.POST.get('K'),
                    weekend_weekday = request.POST.get('L'),
                    dt_of_interview = request.POST.get('M'),
                    status = request.POST.get('N'),
                    contact_number = request.POST.get('O'),
                    email_id =  request.POST.get('P'),
                    tot_yrs_exp =request.POST.get('Q'),
                    R_exp =request.POST.get('R'),
                    current_org = request.POST.get('S'),
                    current_loc = request.POST.get('T'),
                    pref_loc = request.POST.get('U'),
                    current_ctc = request.POST.get('V'),
                    exp_ctc = request.POST.get('W'),
                    notice_period = request.POST.get('X'))
                source.save()
            return render(
                request,
                'applicants.html',
                {
                'form2':form2,
                'sources':source1,
                'search_query':search_query,
                'approvals':approval1
                })

        if form3.is_valid():
            search_id1=request.POST.get('sou_id1')
            s = Source.objects.get(id=search_id1)
            s.TR_status=request.POST.get('Aa')
            s.MR_status=request.POST.get('Bb')
            s.HR_status= request.POST.get('Cc')
            s.offers_made= request.POST.get('Dd')
            s.DOJ= request.POST.get('Ee')
            s.save()

            offerscount=0
            sources = Source.objects.filter(RGS_ID=s.RGS_ID)
            approvals = Approval.objects.get(RGS_ID=s.RGS_ID)
            flag = 0
            for j in sources:
                if j.offers_made == 'Yes' and flag == 0:
                    approvals.c1_epno = j.epno
                    approvals.c1_name = j.cand_name
                    approvals.c1_DOJ = j.DOJ
                    approvals.save()
                    flag=1
                    offerscount = offerscount+1
                elif j.offers_made == 'Yes' and flag ==1:
                    approvals.c2_epno = j.epno
                    approvals.c2_name = j.cand_name
                    approvals.c2_DOJ = j.DOJ
                    approvals.save()
                    offerscount = offerscount+1
            if offerscount == 1:
                approvals.c2_epno = '-'
                approvals.c2_name = '-'
                approvals.save()
            if offerscount == 0:
                approvals.c2_epno = '-'
                approvals.c2_name = '-'
                approvals.c1_epno = '-'
                approvals.c1_name = '-'
                approvals.save()
            approvals.No_offers_processed = offerscount
            approvals.save() 

    elif request.method == "GET":
        form2 = ManifiestosForm1(request.POST)
        form3 = SearchForm(request.POST)

        if form3.is_valid():
            search_query = form3.cleaned_data['hid']
            source1 = Source.objects.filter(RGS_ID=search_query)
            approval1 = Approval.objects.get(RGS_ID=search_query)
            return render(
                request,
                'applicants.html',
                {
                'form2':form2,
                'sources':source1,
                'search_query':search_query,
                'approvals':approval1
                })

    search_query=request.GET.get('hid', '')
    source1 = Source.objects.filter(RGS_ID=search_query)
    approval1 = Approval.objects.get(RGS_ID=search_query)
    return render(
        request,
        'applicants.html',
        {
            'form2':form2,
            'sources':source1,
            'search_query':search_query,
            'approvals':approval1
        })

def download(request):
    approvals = Approval.objects.all()
    for x in approvals:
        count=0
        TRcount=0
        MRcount=0
        HRcount=0
        flag =0
        sources = Source.objects.filter(RGS_ID=x.RGS_ID)
        for y in sources:
            count=count+1
            if y.TR_status == 'Yes':
                TRcount=TRcount+1
            if y.HR_status == 'Yes':
                HRcount=HRcount+1
            if y.MR_status == 'Yes':
                MRcount=MRcount+1

        x.no_cv_shared = count
        x.TR_selects_holds = TRcount
        x.TR_rejects = count - TRcount
        x.MR_selects_holds = MRcount
        x.MR_rejects = count - MRcount
        x.HR_selects_holds = HRcount
        x.HR_rejects = count - HRcount
        x.save()


	output = io.BytesIO()
	
	workbook = Workbook(output,{'in_memory': True})
	workbook = Workbook(output, {'remove_timezone': True})
	format = workbook.add_format()
	format1 = workbook.add_format()
	date_format = workbook.add_format({'num_format': 'dd/mm/yy'})

    #format.set_pattern(1)  # This is optional when using a solid fill.
	format.set_fg_color('#99FFFF')
	format.set_bold()
	format.set_text_wrap()
	format.set_border(style=1)
	format1.set_fg_color('#9DC3E5')
	format1.set_text_wrap()
	format1.set_border(style=1)

	worksheet = workbook.add_worksheet()

	worksheet.write(0, 0, 'RGS ID',format)
	worksheet.write(0, 1, 'RGS ID Status',format)
	worksheet.write(0, 2, 'Role',format)
	worksheet.write(0, 3, 'Required Skill Set',format)
	worksheet.write(0, 4, 'Total Experience',format)
	worksheet.write(0, 5, 'Branch',format)
	worksheet.write(0, 6, 'IOU',format)
	worksheet.write(0, 7, 'Requirement IOU',format)
	worksheet.write(0, 8, 'Customer Name',format)
	worksheet.write(0, 9, 'Assigned Date',format)
	worksheet.write(0, 10, 'Requirement Branch',format)
	worksheet.write(0, 11, 'Staffing Branch',format)

	worksheet.write(0, 12, 'Recruiter',format1)
	worksheet.write(0, 13, 'Remarks',format1)
	worksheet.write(0, 14, 'Status',format1)
	worksheet.write(0, 15, 'No. of CVs shared',format1)
	worksheet.write(0, 16, 'Feedback Pending',format1)
	worksheet.write(0, 17, 'Screening Rejects/others',format1)
	worksheet.write(0, 18, 'Shortlist',format1)
	worksheet.write(0, 19, 'TR Selects/ Hold',format1)
	worksheet.write(0, 20, 'TR Rejects',format1)
	worksheet.write(0, 21, 'MR Selects/ Hold',format1)
	worksheet.write(0, 22, 'MR Rejects',format1)
	worksheet.write(0, 23, 'HR Selects/ HR Hold',format1)
	worksheet.write(0, 24, 'HR Rejects',format1)
	worksheet.write(0, 25, 'No. of Offers In Process',format1)
	worksheet.write(0, 26, 'No. of Offers Released',format1)
	worksheet.write(0, 27, 'Candidate 1 EP No.',format1)
	worksheet.write(0, 28, 'Candidate 1 Name',format1)
	worksheet.write(0, 29, 'Joining status',format1)
	worksheet.write(0, 30, 'DOJ',format1)
	worksheet.write(0, 31, 'Candidate 2 EP No.',format1)
	worksheet.write(0, 32, 'Candidate 2 Name',format1)
	worksheet.write(0, 33, 'Joining status',format1)
	worksheet.write(0, 34, 'DOJ',format1)

	approvals = Approval.objects.all()
	count=1
	for x in approvals:
		worksheet.write(count,0,x.RGS_ID)
		worksheet.write(count,1,x.RGS_status)
		worksheet.write(count,2,x.role)
		worksheet.write(count,3,x.rqd_skset)
		worksheet.write(count,4,x.tot_exp)
		worksheet.write(count,5,x.branch)
		worksheet.write(count,6,x.IOU)
		worksheet.write(count,7,x.req_IOU)
		worksheet.write(count,8,x.cust_name)
		worksheet.write_datetime(count,9,x.ass_date,date_format)
		worksheet.write(count,10,x.req_branch)
		worksheet.write(count,11,x.staff_branch)
		worksheet.write(count,12,x.recruiter)
		worksheet.write(count,13,x.remarks)
		worksheet.write(count,14,x.status)
		worksheet.write(count,15,x.no_cv_shared)
		worksheet.write(count,16,x.feedback_pending)
		worksheet.write(count,17,x.screen_rejects_others)
		worksheet.write(count,18,x.shortlists)
		worksheet.write(count,19,x.TR_selects_holds)
		worksheet.write(count,20,x.TR_rejects)
		worksheet.write(count,21,x.MR_selects_holds)
		worksheet.write(count,22,x.MR_rejects)
		worksheet.write(count,23,x.HR_selects_holds)
		worksheet.write(count,24,x.HR_rejects)
		worksheet.write(count,25,x.No_offers_processed)
		worksheet.write(count,26,x.No_offers_released)
		worksheet.write(count,27,x.c1_epno)
		worksheet.write(count,28,x.c1_name)
		worksheet.write(count,29,x.c1_joining_status)
		#worksheet.write_datetime(count,30,x.c1_DOJ,date_format)
		worksheet.write(count,31,x.c2_epno)
		worksheet.write(count,32,x.c2_name)
		worksheet.write(count,33,x.c2_joining_status)
		#worksheet.write_datetime(count,34,x.c1_DOJ,date_format)

		count = count +1
    worksheet.set_column('A:AI',20)
    
    workbook.close()
    
    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Approval Master Sheet.xlsx"

    return response

    
