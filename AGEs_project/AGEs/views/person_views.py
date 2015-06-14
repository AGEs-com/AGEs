from django.shortcuts import render

#Person画面遷移時のView
from AGEs.models import Item, Picture
def person(request):
    item_list = Item.objects.order_by('-num_of_pictures')[:]
    context_dict = {'items' : item_list}
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/person.html', context_dict)
