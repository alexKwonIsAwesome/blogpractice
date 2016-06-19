from django.views.generic import View
from django.shortcuts import redirect

from bitly.models import Bitlink

class BitlinkRedirectView(View):

    def get(self, reqeust, *args, **kwargs):
        bitlink = Bitlink.objects.get(
                shorten_hash=kwargs.get("shorten_hash"),
        )

        return redirect(bitlink.original_url)
