from django.shortcuts import render

#Person画面遷移時のView
from AGEs.models import Category, Item, Picture
def person(request):
    person = Category.objects.filter(category_name = 'Person')
    item_list = Item.objects.filter(category = person).order_by('-num_of_pictures')[:]
    context_dict = {'items' : item_list}
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/person.html', context_dict)

def object(request):
    object = Category.objects.filter(category_name = 'Object')
    item_list = Item.objects.filter(category = object).order_by('-num_of_pictures')[:]
    context_dict = {'items' : item_list}
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/object.html', context_dict)