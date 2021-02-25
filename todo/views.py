from django.shortcuts import render,redirect
from .forms import RegisterForm,TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request,'index.html')


@login_required(login_url='login')
def todos(request):
  thetodos = Todo.objects.filter(author = request.user)

  form = TodoForm()
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      # take note of this for related models in modelform
      todo = form.save(commit=False)
      todo.author = request.user
      todo.save()
    
      return redirect('todos')
  context = {
    'form':form,
    'todos':thetodos
  }
  return render(request,'todo.html',context)

def taskcomplete(request):
  if request.method == 'POST':
    todoid = request.POST['todoID']
    thetodo = Todo.objects.get(id=todoid)
    thetodo.task_complete = True
    thetodo.save()
    return redirect('todos')

def deletetask(request):
  if request.method == 'POST':
    todoid = request.POST['todoID']
    thetodo = Todo.objects.get(id=todoid).delete()
   
    return redirect('todos')

# Security
def loginpage(request):
  if request.user.is_authenticated:
    return redirect('todos')
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    theuser = authenticate(request,username=username,password=password)
    if theuser:
      login(request,theuser)
      return redirect('todos')
    else:
      messages.info(request,'Invalid Credentials')
  return render(request,'login.html')

def logoutpage(request):
  logout(request)
  return redirect('index')

def registerpage(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')

  ahmad = {
    'form':form
  }
  return render(request,'register.html',ahmad)
