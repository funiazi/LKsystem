# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:12:48 2018

@author: lenovo
"""
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=128, label='用户名', widget=forms.TextInput(attrs={'class':'form-control'}))   
    password = forms.CharField(max_length=256, label='密码',  widget=forms.PasswordInput(attrs={'class':'form-control'}))