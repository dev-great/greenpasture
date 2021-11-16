from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .models import store


def stores(request):
	stores = store.objects.all().order_by('-list_date').filter(is_published=True)
	paginator = Paginator(stores, 30)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	return render(request,'store/store.html',{'stores' : paged_listings})

def store_listing(request , listing_id):
	store = get_object_or_404(store , pk=listing_id)
	context = {
	  'store' : store
	}
	return render(request,'store/books.html',context)


