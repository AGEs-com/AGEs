from django.shortcuts import render

# home画面遷移時のView
def home(request):
    #テンプレートエンジンにコンテキストとしてDictionaryを用意する
    context_dict = {'boldmessage' : "Welcome to AGEs!!!"}
    # Client側にレンダリングしたresponseを送る
    return render(request, 'AGEs/home.html', context_dict)

#Person画面遷移時のView
from AGEs.models import Item, Picture
def person(request):
    item_list = Item.objects.order_by('-num_of_pictures')[:]
    context_dict = {'items' : item_list}
    # レンダリングしたレスポンスをクライアント側に送る
    return render(request, 'ages/person.html', context_dict)

def personname(request, item_name_slug):
    # コンテキスト用の辞書を準備
    context_dict = {}
    
    try:
        # itemのslug名がない場合はDoesNotExistをレイズする
        item = Item.objects.get(slug=item_name_slug)
        context_dict['item_name'] = item.item_name
        
        # 関連する写真を全て取得する(同じ項目のものだけ取得する)
        pictures = Picture.objects.filter(item=item)
        # 取得した写真をコンテキストに詰める
        context_dict['pictures'] = pictures
    except Item.DoesNotExist:
        # エラーの場合はなにもしない
        pass
    
    return render(request, 'AGEs/personname.html', context_dict)