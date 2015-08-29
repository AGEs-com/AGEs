from django.shortcuts import render
from AGEs.models import Category, Item, Picture

#Person画面遷移時のView
def show_person(request):
    context_dict = get_context_dict('Person')
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/person.html', context_dict)

def show_object(request):
    context_dict = get_context_dict('Object')
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/object.html', context_dict)

def get_context_dict(category_name):
    '''
    :param category_name:
        categoryオブジェクトを取得し、context_dictを返す
    :return:
        context_dict
    '''
    object = Category.objects.filter(category_name = category_name)
    item_list = Item.objects.filter(category = object).order_by('-num_of_pictures')[:]
    return {'items' : item_list}
