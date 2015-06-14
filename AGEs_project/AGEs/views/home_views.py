from django.shortcuts import render

# home画面遷移時のView
def home(request):
    #テンプレートエンジンにコンテキストとしてDictionaryを用意する
    context_dict = {'boldmessage' : "Welcome to AGEs!!!"}
    # Client側にレンダリングしたresponseを送る
    return render(request, 'AGEs/home.html', context_dict)
