from django.shortcuts import render
from AGEs.forms import PersonSearchForm

#Search後のPerson画面遷移時のView
from AGEs.models import Item
def search_person(request):
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PersonSearchForm(request.POST)
        item_list = Item.objects.get(person_name = form.item_name)[:]
        context_dict = {'items' : item_list}
        
    # TODO: フォームがない場合は、再表示？    
    return render(request, 'AGEs/person.html', context_dict)
