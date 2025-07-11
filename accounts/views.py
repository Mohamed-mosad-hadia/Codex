from django.shortcuts import render, redirect
from students.models import Student
from django.db.models import Avg


def login_view(request):
    error = None
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # student = Student.objects.filter(phone=phone, password=password).first()
        password = request.POST.get('password')
        student = Student.objects.filter(phone=phone, password=password).first()
        if student:
            request.session['student_id'] = student.id
            return redirect('dashboard')
        error = 'رقم الهاتف أو كلمة المرور غير صحيحة'
    return render(request, 'login.html', {'error': error})


def dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('login')
    student = Student.objects.get(id=student_id)
    records = student.records.order_by('-date')
    payments = student.payments.order_by('-month')

    total_sessions = records.count()
    attended = records.filter(attendance=True).count()
    attendance_rate = int(attended * 100 / total_sessions) if total_sessions else 0
    avg_grade = records.aggregate(avg=Avg('grade'))['avg'] or 0
    paid_count = payments.filter(is_paid=True).count()

    context = {
        'student': student,
        'records': records,
        'payments': payments,
        'attendance_rate': attendance_rate,
        'avg_grade': round(avg_grade, 1),
        'paid_count': paid_count,
        'total_payments': payments.count(),
    }
    return render(request, 'Student_Dashboard.html', context)


def logout_view(request):
    """Clear the logged in student session and redirect to login."""
    request.session.flush()
    return redirect('login')