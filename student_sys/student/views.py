# coding:utf-8
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student

# # class-based view方式
# class IndexView(View):
#     template_name = 'index.html'

#     def get_context(self):
#         students = Students.get_all()
#         context = {
#             'students' : students
#         }
#         return context

#     def get(self, request):
#         context = self.get_context()
#         form = StudentForm()
#         context.update({
#             'form' : form
#         })
#         return render(request, self.template_name, context=context)

#     def post(self, request):
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))
#         context = self.get_context()
#         context.update({
#             'form' : form
#         })

# 手动构建student对象方法保存Student数据
# def方式构建viwe
def index(request):
    students = Student.objects.all()
    # 使用@classmeta对model里objects.all()封装的接口
    # students = Students.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
        # 使用cleaned_data
        #     cleaned_data = form.cleaned_data
        #     student = Student()
        #     student.name = cleaned_data['name']
        #     student.sex = cleaned_data['sex']
        #     student.email = cleaned_data['email']
        #     student.profession = cleaned_data['profession']
        #     student.qq = cleaned_data['qq']
        #     student.phone = cleaned_data['phone']
        #     student.save()
        #     return HttpResponseRedirect(reverse('index'))
            form.save()
            return HttpResponseRedirect(reverse('index'))        
    else:
        form = StudentForm()
    context = {
        'students' : students,
        'form' : form,
    }
    return render(request, 'index.html', context=context)
