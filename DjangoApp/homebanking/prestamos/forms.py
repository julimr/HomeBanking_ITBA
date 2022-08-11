from locale import format_string
from django import forms

from .models import Prestamo


class PrestamosForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_date', 'loan_total', 'customer_id']
        
# def post_new(request):

#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)

#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})