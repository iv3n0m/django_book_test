from dal import autocomplete
from blog.models import Category, Tag, Post
from django import forms

class PostAdminForm(forms.ModelForm):

    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        widget = autocomplete.ModelSelect2(url='category-autocomplete'), label='分类',
    )

    tag = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all(),
        widget = autocomplete.ModelSelect2Multiple(url='tag-autocomplete'), label='标签',
    )

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'content', 'status')


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        
        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs