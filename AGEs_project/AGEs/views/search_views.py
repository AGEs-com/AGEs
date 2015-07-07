from django.shortcuts import render
from AGEs.forms import PersonSearchForm

#Search後のPerson画面遷移時のView
from AGEs.models import Item
def search_person(request):
    # HTTP POSTの場合
    if request.method == 'POST':
        form = PersonSearchForm(request.POST)

        item_list = None
        # 入力データが適切かどうかを判断
        if form.is_valid():
            name = form.cleaned_data['item_name']
            try:
                # DBから入力された名前から検索(__icontainsでlike検索(大小区別しない)) リスト型では取れない？
                items = Item.objects.filter(item_name__icontains = name).order_by('-num_of_pictures') # おそらくリスト型ではない
                item_list = items
            except Exception: # FIXME: 例外レベルが高いから修正の必要あり
                pass

        context_dict = {'items' : item_list}
        
    # TODO: フォームがない場合は、再表示？    
    return render(request, 'AGEs/person.html', context_dict)
