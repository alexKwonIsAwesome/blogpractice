from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from bitly.models.bitlink import Bitlink
from hashids import Hashids

class BitlinkCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "bitly/new.html",
                {},
                )

    def post(self, request, *args, **kwargs):

        original_url = request.POST.get("original_url")

        bitlink = request.user.bitlink_set.create(
                original_url=original_url,
            )

        hashids = Hashids(salt="awesome tzuyu", min_length=4) 
        bitlink.shorten_hash = hashids.encode(bitlink.id)

        bitlink.save()

        return redirect(reverse("home"))


