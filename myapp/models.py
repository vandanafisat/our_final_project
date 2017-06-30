# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from datetime import date
from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.
class Approval(models.Model):
    RGS_ID = models.CharField(primary_key=True,max_length=200)
    RGS_status = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    rqd_skset = models.CharField(max_length=200)
    tot_exp = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    IOU = models.CharField(max_length=200)
    req_IOU = models.CharField(max_length=200)
    cust_name = models.CharField(max_length=200)
    ass_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    req_branch = models.CharField(max_length=200)
    staff_branch = models.CharField(max_length=200)
    recruiter = models.CharField(max_length=200,default='-')
    remarks = models.CharField(max_length=200,default='-')
    status = models.CharField(max_length=200,default='-')
    no_cv_shared = models.IntegerField(default=0)
    feedback_pending = models.CharField(max_length=200,default='-')
    screen_rejects_others = models.CharField(max_length=200,default='-')
    shortlists = models.CharField(max_length=200,default='-')
    TR_selects_holds = models.IntegerField(default=0)
    TR_rejects= models.IntegerField(default=0)
    MR_selects_holds= models.IntegerField(default=0)
    MR_rejects= models.IntegerField(default=0)
    HR_selects_holds= models.IntegerField(default=0)
    HR_rejects = models.IntegerField(default=0)
    No_offers_processed= models.IntegerField(default=0)
    No_offers_released= models.IntegerField(default=0)
    c1_epno= models.CharField(max_length=200,default='-')
    c1_name= models.CharField(max_length=200,default='-')
    c1_joining_status= models.CharField(max_length=200,default='-')
    c1_DOJ= models.DateTimeField(default=datetime.datetime.now)
    c2_epno= models.CharField(max_length=200,default='-')
    c2_name= models.CharField(max_length=200,default='-')
    c2_joining_status= models.CharField(max_length=200,default='-')
    c2_DOJ= models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.RGS_ID


class Source(models.Model):
    RGS_ID = models.ForeignKey(Approval)
    DOT = models.DateTimeField(auto_now=False, auto_now_add=False)
    branch = models.CharField(max_length=200,default='-')
    who_sourced_name= models.CharField(max_length=200,default='-')
    who_sourced_eno= models.CharField(max_length=200,default='-')
    cand_name= models.CharField(max_length=200,default='-')
    epno  = models.CharField(max_length=200,default='-')
    source_dtls= models.CharField(max_length=200,default='-')
    main_skills = models.CharField(max_length=200,default='-')
    ISU_name =  models.CharField(max_length=200,default='-')
    customer_name  = models.CharField(max_length=200,default='-')
    weekend_weekday = models.CharField(max_length=200,default='-')
    dt_of_interview = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=200,default='-')
    contact_number = models.CharField(max_length=200,default='-')
    email_id = models.EmailField(blank=True)
    tot_yrs_exp = models.CharField(max_length=200,default='-')
    R_exp = models.CharField(max_length=200,default='-')
    current_org = models.CharField(max_length=200,default='-')
    current_loc = models.CharField(max_length=200,default='-')
    pref_loc = models.CharField(max_length=200,default='-')
    current_ctc = models.CharField(max_length=200,default='-')
    exp_ctc = models.CharField(max_length=200,default='-')
    notice_period = models.CharField(max_length=200,default='-')
    TR_status = models.CharField(max_length=200,default='-')
    MR_status = models.CharField(max_length=200,default='-')
    HR_status = models.CharField(max_length=200,default='-')
    offers_made = models.CharField(max_length=200,default='-')
    DOJ = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.branch

