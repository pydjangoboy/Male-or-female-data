from django.shortcuts import render

# Create your views here.
def ShowDetails(request):
    emp_details = {
        "101": {"name": "Rahul", "gender": "Male", "salary": 100000},
        "102": {"name": "Maya", "gender": "Female", "salary": 120000},
        "103": {"name": "Shyam", "gender": "Male", "salary": 150000},
        "104": {"name": "Kaya", "gender": "Female", "salary": 160000},
        "105": {"name": "Ravi", "gender": "Male", "salary": 180000},
        "106": {"name": "Jaya", "gender": "Female", "salary": 200000}

    }
    return render(request,'index.html', {'emp':emp_details})