# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:19:24 2018

@author: lenovo
"""

from django import forms
from .models import Post

class DataForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {
            'workshop': '工作车间',
            'workshift': '工作班次',
            'machine_num': '机器号',
            'order_num': '订单号',
            'product_num': '生产数量',
            'product_units': '生产单位',
            'waste_num': '废料数',            
            'operator': '操作员',
            'remarks': '备注',
        }
        fields =  '__all__'
        widgets = {
            'workshop': forms.Select(attrs={'class': 'form-control select2'}),
            'workshift': forms.Select(attrs={'class': ' form-control select2'}),
            'machine_num': forms.TextInput(attrs={'class': ' form-group'}),
            'order_num': forms.TextInput(attrs={'class': ' form-group'}),
            'product_num': forms.NumberInput(attrs={'class': ' form-group'}),
            'product_units': forms.NumberInput(attrs={'class': ' form-group'}),
            'waste_num': forms.NumberInput(attrs={'class': ' form-group'}),
            'operator': forms.TextInput(attrs={'class': ' form-group'}),
            'remarks': forms.TextInput(attrs={'class': ' form-group'}),
        }