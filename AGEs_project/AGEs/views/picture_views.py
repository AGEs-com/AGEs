from django.shortcuts import render
from AGEs.models import Item, Picture

def personname(request, id):
    # コンテキスト用の辞書を準備
    context_dict = {}
    
    try:
        # itemのslug名がない場合はDoesNotExistをレイズする
        item = Item.objects.get(id=id)
        context_dict['item_name'] = item.item_name
        context_dict['id'] = id
        
        # 関連する写真を全て取得する(同じ項目のものだけ取得する)
        pictures = Picture.objects.filter(item=item)
        # 取得した写真をコンテキストに詰める
        context_dict['pictures'] = pictures
    except Item.DoesNotExist:
        # エラーの場合はなにもしない
        pass
    
    return render(request, 'AGEs/personname.html', context_dict)